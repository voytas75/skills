"""Synthetic lifecycle example; no application or native-host qualification."""
from contextlib import contextmanager
from pathlib import PureWindowsPath, PurePosixPath


for application_fails in (False, True):
    for cleanup_fails in (False, True):
        events = []
        application_error = ValueError("synthetic application failure")
        cleanup_error = RuntimeError("synthetic cleanup failure")

        @contextmanager
        def lifecycle():
            events.append("enter")
            primary_error = None
            try:
                yield
            except BaseException as error:
                primary_error = error
                raise
            finally:
                events.append("exit")
                try:
                    if cleanup_fails:
                        raise cleanup_error
                except Exception as error:
                    if primary_error is None:
                        raise
                    primary_error.add_note(f"Cleanup also failed: {error}")

        def build():
            return lifecycle

        def main():
            with build()():
                events.append("work")
                if application_fails:
                    raise application_error

        expected = application_error if application_fails else cleanup_error if cleanup_fails else None
        try:
            main()
        except (ValueError, RuntimeError) as actual:
            assert actual is expected, "primary error was replaced"
            if application_fails and cleanup_fails:
                assert actual.__notes__ == ["Cleanup also failed: synthetic cleanup failure"]
        else:
            assert expected is None, "failure was suppressed"
        assert events == ["enter", "work", "exit"]

assert PureWindowsPath(".venv/Scripts/python.exe").name == "python.exe"
assert PurePosixPath(".venv/bin/python").name == "python"
print("PASS recovery: success, application failure, cleanup failure, double failure preserving primary error; static paths only, no native Windows")
