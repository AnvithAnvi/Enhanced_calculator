import builtins
import pytest
from unittest.mock import patch
from app import repl
from app.calculator import Calculator


# -----------------------------
# REPL TESTS
# -----------------------------
def test_repl_exit():
    """Simulate typing 'exit' immediately in REPL (expect SystemExit)."""
    with patch("builtins.input", side_effect=["exit"]):
        with pytest.raises(SystemExit):
            repl.main()


def test_repl_help():
    """Simulate typing 'help' then 'exit' (expect SystemExit)."""
    with patch("builtins.input", side_effect=["help", "exit"]):
        with pytest.raises(SystemExit):
            repl.main()


def test_invalid_command():
    """Simulate invalid command followed by exit (expect SystemExit)."""
    with patch("builtins.input", side_effect=["xyz", "exit"]):
        with pytest.raises(SystemExit):
            repl.main()


# -----------------------------
# CALCULATOR TESTS
# -----------------------------
def test_perform_operation_success(monkeypatch):
    """Covers the operation logic inside calculator.py (happy path)."""
    calc = Calculator()
    monkeypatch.setattr(builtins, "input", lambda _: "2")  # both operands
    calc.perform_operation("add")


def test_perform_operation_error(monkeypatch):
    """Forces an input validation error to cover exception branch."""
    calc = Calculator()

    def bad_input(prompt):
        if "first" in prompt:
            return "not_a_number"
        return "5"

    monkeypatch.setattr(builtins, "input", bad_input)
    calc.perform_operation("add")


def test_show_history_empty():
    """Covers empty history print branch."""
    calc = Calculator()
    calc.history._history = []
    calc.show_history()


def test_clear_undo_redo_paths():
    """Covers undo/redo/clear branches when no history is available."""
    calc = Calculator()
    calc.undo()
    calc.redo()
    calc.clear_history()
