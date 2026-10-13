from contextlib import contextmanager
from pathlib import PureWindowsPath, PurePosixPath

for fail in (False, True):
    events = []
    @contextmanager
    def lifecycle():
        events.append("enter")
        try:
            yield
        finally:
            events.append("exit")
    def build():
        return lifecycle
    def main():
        with build()():
            events.append("work")
            if fail:
                raise ValueError("synthetic application failure")
    try:
        main()
    except ValueError:
        assert fail
    assert events == ["enter", "work", "exit"]
assert PureWindowsPath(".venv/Scripts/python.exe").name == "python.exe"
assert PurePosixPath(".venv/bin/python").name == "python"
print("PASS recovery: synthetic lifecycle success/failure and static path shapes; no native Windows")
