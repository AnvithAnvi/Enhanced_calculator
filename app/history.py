import pandas as pd
import os


class History:
    """Handles storing and managing calculation history."""
    def __init__(self):
        self._history = []
        self.history_df = pd.DataFrame(
            columns=["operand1", "operand2", "operation", "result"]
        )

    def add(self, calculation):
        """Add a new calculation to history."""
        self._history.append(calculation)
        new_row = {
            "operand1": calculation.operand1,
            "operand2": calculation.operand2,
            "operation": calculation.operation,
            "result": calculation.result,
        }
        self.history_df = pd.concat(
            [self.history_df, pd.DataFrame([new_row])], ignore_index=True
        )

    def clear(self):
        """Clear the entire history."""
        self._history = []
        self.history_df = pd.DataFrame(
            columns=["operand1", "operand2", "operation", "result"]
        )

    def load_from_csv(self, file_path):
        """Load history data from a CSV file."""
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError
            self.history_df = pd.read_csv(file_path)
            self._history = self.history_df.to_dict("records")
            print("History loaded successfully.")
        except FileNotFoundError:
            print("No history file found.")
        except Exception as e:
            print(f"Error loading file: {e}")

    def to_dataframe(self):
        """Return the history dataframe."""
        return self.history_df
