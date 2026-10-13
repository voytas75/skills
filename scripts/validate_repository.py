"""Check skill metadata, tracked JSON, workflow YAML syntax, and local links.

Uses yaml.safe_load, not a full GitHub Actions schema validator. Markdown is a
practical subset: inline links/images with simple or one-level nested parentheses,
angle-bracket destinations, optional quoted titles, and single-line reference
definitions. Fenced, indented, and backtick inline code are excluded. Complex
CommonMark nesting, HTML links, and reference-use resolution are not supported.
Only file existence and repository containment are checked; external schemes,
protocol-relative URLs, and heading anchors are skipped, never fetched. Tracked
Markdown/JSON and skills are checked in the working tree; the workflow is checked
explicitly so it also works before that new file is tracked.
"""

import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DESTINATION = r'(?:<[^>\n]*>|(?:[^\s()\\]|\\.|\([^()\n]*\))+)'
TITLE = r'''(?:\s+(?:"[^"\n]*"|'[^'\n]*'|\([^()\n]*\)))?'''
INLINE_LINK = re.compile(r'!?\[(?:[^\[\]\\\n]|\\.)*\]\(\s*(' + DESTINATION + ')' + TITLE + r'\s*\)')
REFERENCE = re.compile(r'^ {0,3}\[[^\]\n]+\]:\s*(' + DESTINATION + ')' + TITLE + r'\s*$', re.MULTILINE)


def prose_only(text):
    """Blank code while retaining line boundaries for reference definitions."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\n'))
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            lines.append('\n')
        elif marker:
            fence = marker[1]
            lines.append('\n')
        elif line.startswith(('    ', '\t')):
            lines.append('\n')
        else:
            lines.append(line)
    return re.sub(r'(`+)(?!`)([\s\S]*?)(?<!`)\1(?!`)', lambda m: '\n' * m[0].count('\n'), ''.join(lines))


def check_frontmatter(path):
    lines = path.read_text(encoding='utf-8').splitlines()
    if not lines or lines[0] != '---':
        raise ValueError('missing YAML frontmatter')
    try:
        end = lines.index('---', 1)
    except ValueError:
        raise ValueError('unclosed YAML frontmatter') from None
    metadata = yaml.safe_load('\n'.join(lines[1:end]))
    if not isinstance(metadata, dict):
        raise ValueError('frontmatter must be a mapping')
    name = metadata.get('name')
    if not isinstance(name, str) or not 1 <= len(name) <= 64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        raise ValueError('name must be 1..64 lowercase ASCII letters/digits with single internal hyphens')
    if name != path.parent.name:
        raise ValueError('name must match the skill folder')
    description = metadata.get('description')
    if not isinstance(description, str) or not description.strip() or not 1 <= len(description) <= 1024:
        raise ValueError('description must be a nonblank string of 1..1024 characters')


def check_links(path):
    text = prose_only(path.read_text(encoding='utf-8'))
    for pattern in (INLINE_LINK, REFERENCE):
        for match in pattern.finditer(text):
            destination = match[1]
            if destination.startswith('<'):
                destination = destination[1:-1]
            destination = re.sub(r'\\([!"#$%&\'()*+,\-./:;<=>?@\[\]\\^_`{|}~])', r'\1', destination)
            url = urlsplit(destination)
            if url.scheme or url.netloc or destination.startswith('//') or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT):
                raise ValueError(f'local link escapes repository: {destination}')
            if not target.exists():
                raise ValueError(f'missing local link target: {destination}')


def main():
    tracked = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    errors = []
    checks = []
    for name in filter(None, tracked):
        path = ROOT / name
        if path.suffix.lower() == '.json':
            checks.append((path, lambda p: json.loads(p.read_text(encoding='utf-8'))))
        if path.suffix.lower() == '.md':
            checks.append((path, check_links))
        if path.name == 'SKILL.md' and name.startswith('skills/'):
            checks.append((path, check_frontmatter))
    checks.append((ROOT / '.github/workflows/validate.yml', lambda p: yaml.safe_load(p.read_text(encoding='utf-8'))))
    for path, check in checks:
        try:
            check(path)
        except (OSError, ValueError, yaml.YAMLError) as error:
            errors.append(f'{path.relative_to(ROOT)}: {error}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS repository validation: {len(checks)} checks (workflow YAML syntax only)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
