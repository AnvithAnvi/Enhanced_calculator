import os
import time
import logging
from app.logger import LoggingObserver, AutoSaveObserver
from app.history import History
from app.calculation import Calculation

def test_logging_observer(tmp_path):
    """
    Tests that LoggingObserver correctly writes a log file.
    """

    # Remove any existing handlers so basicConfig reconfigures properly
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Initialize logger and create a calculation
    log = LoggingObserver(tmp_path)
    calc = Calculation(2, 3, "add", 5)

    # Log the calculation and force the log to flush
    log.update(calc)
    for handler in logging.root.handlers:
        handler.flush()
    logging.shutdown()

    # Log file should exist and have content
    log_file = tmp_path / "calculator.log"

    # Retry loop to handle macOS filesystem delay
    for _ in range(5):
        if log_file.exists() and log_file.stat().st_size > 0:
            break
        time.sleep(0.1)

    assert log_file.exists(), f"Expected log file not found: {log_file}"
    assert log_file.stat().st_size > 0, "Log file is empty"

def test_autosave_observer(tmp_path):
    """
    Tests that AutoSaveObserver correctly writes a CSV file with history data.
    """

    # Create a simple history with one calculation
    h = History()
    h.add(Calculation(2, 3, "add", 5))

    # Initialize the AutoSaveObserver and trigger save
    obs = AutoSaveObserver(tmp_path)
    obs.update(h)

    # Verify that a history.csv file was created and has data
    file_path = tmp_path / "history.csv"
    assert file_path.exists(), f"Expected CSV file not found: {file_path}"
    assert file_path.stat().st_size > 0, "CSV file is empty"
