import os
from dotenv import load_dotenv

load_dotenv()

class CalculatorConfig:
    LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
    HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")
    MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 50))
    AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
    PRECISION = int(os.getenv("CALCULATOR_PRECISION", 2))
    MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 100000))
    DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

    @classmethod
    def validate(cls):
        os.makedirs(cls.LOG_DIR, exist_ok=True)
        os.makedirs(cls.HISTORY_DIR, exist_ok=True)
