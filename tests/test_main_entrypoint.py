import runpy
from unittest.mock import patch
import pytest

def test_repl_entrypoint(monkeypatch):
    """Safely covers the __main__ entry point of app/repl.py."""
    # Mock input() so REPL immediately receives 'exit' and quits
    monkeypatch.setattr("builtins.input", lambda _: "exit")

    # runpy will execute the module like a CLI run
    with pytest.raises(SystemExit):
        runpy.run_module("app.repl", run_name="__main__")
