import logging
import os
import pandas as pd


def get_logger():
    """Return a configured calculator logger."""
    logger = logging.getLogger("calculator")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        os.makedirs("logs", exist_ok=True)
        handler = logging.FileHandler("logs/calculator.log")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


class LoggingObserver:
    """Observer that logs calculations into calculator.log."""
    def __init__(self, log_dir="."):
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = os.path.join(log_dir, "calculator.log")
        open(self.log_file, "a").close()  # Ensure file exists
        logging.basicConfig(filename=self.log_file, level=logging.INFO)

    def update(self, calculation):
        logging.info(f"Calculation performed: {calculation}")


class AutoSaveObserver:
    """Observer that saves the current history into history.csv."""
    def __init__(self, save_dir="."):
        os.makedirs(save_dir, exist_ok=True)
        self.file_path = os.path.join(save_dir, "history.csv")

    def update(self, history):
        """Write the history dataframe to CSV."""
        df = getattr(history, "history_df", None)
        if isinstance(df, pd.DataFrame):
            df.to_csv(self.file_path, index=False)
