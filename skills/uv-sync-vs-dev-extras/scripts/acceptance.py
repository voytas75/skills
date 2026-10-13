"""Offline wheels and scratch-only uv demo. No existing environment is touched."""
import base64
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

parent = Path(sys.argv[1]).resolve(strict=True)
root = Path(tempfile.mkdtemp(prefix="uv-draft-", dir=parent))
env = {k: v for k, v in os.environ.items() if not k.startswith("UV_") and k not in ("VIRTUAL_ENV", "PYTHONPATH", "PYTHONHOME")}
env.update(UV_CACHE_DIR=str(root/"cache"), UV_PYTHON_DOWNLOADS="never", TMPDIR=str(root))

def wheel(name):
    files = {f"{name}/__init__.py": b"", f"{name}-1.0.dist-info/METADATA": f"Metadata-Version: 2.1\nName: {name}\nVersion: 1.0\n".encode(), f"{name}-1.0.dist-info/WHEEL": b"Wheel-Version: 1.0\nGenerator: synthetic-draft\nRoot-Is-Purelib: true\nTag: py3-none-any\n"}
    rows = [[p, "sha256="+base64.urlsafe_b64encode(hashlib.sha256(b).digest()).decode().rstrip("="), str(len(b))] for p,b in files.items()]
    rec=f"{name}-1.0.dist-info/RECORD"; rows.append([rec,"",""])
    s=io.StringIO(); csv.writer(s).writerows(rows); files[rec]=s.getvalue().encode()
    path=root/f"{name}-1.0-py3-none-any.whl"
    with zipfile.ZipFile(path,"w") as z:
        for p,b in files.items(): z.writestr(p,b)
    return path.name
sources = {n:wheel(n) for n in ("draft_group", "draft_extra", "draft_other")}
(root/"pyproject.toml").write_text('[project]\nname="draft-demo"\nversion="0.0.0"\nrequires-python=">=3.11"\ndependencies=[]\n[project.optional-dependencies]\ndev=["draft-extra"]\n[dependency-groups]\ndev=["draft-group"]\nother=["draft-other"]\n[tool.uv]\npackage=false\n[tool.uv.sources]\n'+''.join(f'{n.replace("_","-")}={{path="{p}"}}\n' for n,p in sources.items()))
log=[]
def run(args):
    p=subprocess.run(["uv",*args,"--offline","--no-python-downloads"],cwd=root,env=env,text=True,capture_output=True)
    log.append({"args":args,"exit":p.returncode,"stdout":p.stdout,"stderr":p.stderr})
    if p.returncode: raise RuntimeError("scratch uv command failed; see receipt")
    return p.stdout

def sync(*flags): run(["sync","--python",sys.executable,*flags])
def members():
    python=root/".venv"/("Scripts/python.exe" if os.name=="nt" else "bin/python")
    p=subprocess.run([str(python),"-I","-c",'import importlib.metadata,json; print(json.dumps(sorted(d.metadata["Name"] for d in importlib.metadata.distributions())))'],env=env,cwd=root,text=True,capture_output=True,check=True)
    return set(json.loads(p.stdout))
try:
    sync(); assert members()=={"draft_group"}
    sync("--extra","dev"); assert members()=={"draft_group","draft_extra"}
    run(["run","--python",sys.executable,"python","-c","pass"]); assert "draft_extra" in members()
    run(["run","--exact","--python",sys.executable,"python","-c","pass"]); assert members()=={"draft_group"}
    sync("--extra","dev"); sync(); assert members()=={"draft_group"}
    sync("--only-group","other"); assert members()=={"draft_other"}
    sync("--no-default-groups"); assert members()==set()
    sync("--extra","dev"); sync("--inexact"); assert "draft_extra" in members()
    sync("--group","other","--no-group","other"); assert members()=={"draft_group"}
    text=(root/"pyproject.toml").read_text().replace('package=false','package=false\ndefault-groups=["other"]')
    (root/"pyproject.toml").write_text(text); sync(); assert members()=={"draft_other"}
    run(["run","--no-sync","--python",sys.executable,"python","-c","pass"]); assert members()=={"draft_other"}
    print("PASS uv: offline synthetic membership checks (groups/extras/default overrides/exclusions/exactness/no-sync)")
finally:
    (root/"receipt.json").write_text(json.dumps(log,indent=2))
    print("Scratch evidence:",root)
