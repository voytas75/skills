# Reconstruction contract

## Artifact modes

### `snapshot`

A captured page may still depend on the original site's CSS, fonts, images, scripts, or base URL. Record every dependency and whether it loaded. Record omitted scripts/resources and their visual or functional impact. Label the output as a dependent snapshot.

### `standalone_mockup`

The output must not require runtime resources from the original site. Include required assets in the package or disclose substitutions. Test the artifact in its intended local/runtime context. An HTML file with a `<base>` pointing to the source site or remote source styles is not standalone.

### `functional_implementation`

In addition to standalone requirements, define each required interaction, initial state, expected result, negative/error path, and keyboard/focus behavior in scope. Execute tests and preserve results. Untested behavior is `NOT_TESTED`.

## Dependency ledger

Each dependency has:
- `dependency_id`;
- `kind` (`css`, `javascript`, `font`, `image`, `svg`, `api`, `other`);
- `source`;
- `disposition`: `retained`, `reimplemented`, `substituted`, `omitted`, `not_resolved`;
- `runtime_origin`;
- `load_status`;
- `impact`;
- optional evidence IDs.

A `standalone_mockup` fails validation if a retained runtime dependency points to the original site origin. Do not execute source scripts automatically. Treat remote content as untrusted.

## Rendering context

Record viewport, scroll, theme, relevant HTML/body attributes, base URL, assets, component states, JS initialization dependency, browser/engine and DPR when known.
