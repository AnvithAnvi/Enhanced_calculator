from app.calculator import Calculator

def test_calculator_help_and_clear(monkeypatch):
    calc = Calculator()
    # Call help (prints text)
    calc.help()
    # Add dummy data, clear it
    calc.history._history = [1, 2, 3]
    calc.clear_history()
    assert calc.history._history == []

def test_undo_redo_empty():
    calc = Calculator()
    calc.undo()
    calc.redo()
