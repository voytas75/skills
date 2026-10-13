from unittest.mock import patch
from types import SimpleNamespace
import boundary

class Fake:
    def fetch(self) -> object:
        return {"items": ["synthetic"]}

missing = ModuleNotFoundError("synthetic missing", name="draft_optional_sdk")
with patch.object(boundary, "import_module", side_effect=missing):
    assert boundary.build() is None
with patch.object(boundary, "import_module", return_value=SimpleNamespace(Client=Fake)):
    c = boundary.build()
    assert c is not None and boundary.normalize(c.fetch()) == {"items": ["synthetic"]}
for error in [ModuleNotFoundError("synthetic transitive", name="draft_transitive"), ImportError("synthetic broken"), RuntimeError("synthetic init")]:
    with patch.object(boundary, "import_module", side_effect=error):
        try:
            boundary.build()
        except type(error) as actual:
            assert actual is error
        else:
            raise AssertionError("broken import suppressed")
for sdk in [SimpleNamespace(), SimpleNamespace(Client=3), SimpleNamespace(Client=lambda: object())]:
    with patch.object(boundary, "import_module", return_value=sdk):
        try:
            boundary.build()
        except (AttributeError, TypeError):
            pass
        else:
            raise AssertionError("invalid factory accepted")
for payload in [None, [], {1: []}, {"items": "bad"}, {"items": [1]}]:
    try:
        boundary.normalize(payload)
    except TypeError:
        pass
    else:
        raise AssertionError("malformed payload accepted")
print("PASS optional: absent/present/broken imports/factories/normalization; synthetic only")
