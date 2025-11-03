import pytest
from app.operations import OperationFactory
from app.history import History

def test_invalid_operation():
    """Covers unsupported operation branch."""
    with pytest.raises(Exception):
        OperationFactory.create("not_real_op")

def test_load_history_file_not_found(tmp_path, capsys):
    """Covers FileNotFoundError in load_from_csv."""
    h = History()
    missing_file = tmp_path / "missing.csv"
    h.load_from_csv(missing_file)  # should print a message
    captured = capsys.readouterr()
    assert "No history file found." in captured.out
