import logging, os
import pandas as pd

class LoggingObserver:
    def __init__(self, log_dir):
        os.makedirs(log_dir, exist_ok=True)
        logging.basicConfig(filename=f"{log_dir}/calculator.log",
                            level=logging.INFO,
                            format="%(asctime)s - %(message)s")

    def update(self, calc):
        logging.info(str(calc))

class AutoSaveObserver:
    def __init__(self, history_dir):
        self.history_dir = history_dir
        os.makedirs(history_dir, exist_ok=True)

    def update(self, history):
        df = history.to_dataframe()
        df.to_csv(f"{self.history_dir}/history.csv", index=False)
