import pandas as pd

class History:
    def __init__(self):
        self._history = []

    def add(self, calc):
        self._history.append(calc)

    def clear(self):
        self._history.clear()

    def to_dataframe(self):
        return pd.DataFrame([{
            "operand1": c.operand1,
            "operation": c.operation,
            "operand2": c.operand2,
            "result": c.result,
            "timestamp": c.timestamp
        } for c in self._history])

    def load_from_csv(self, path):
        try:
            df = pd.read_csv(path)
            self._history = df.to_dict("records")
        except FileNotFoundError:
            print("No history file found.")
