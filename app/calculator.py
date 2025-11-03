import pandas as pd
from app.calculation import Calculation
from app.history import History
from app.operations import operations, OperationFactory
from app.calculator_memento import Caretaker
from app.logger import get_logger
from app.input_validators import validate_numbers


class Calculator:
    """Main calculator class handling operations, history, undo/redo."""

    def __init__(self):
        self.history = History()
        self.memento = Caretaker()
        self.memento.save(self.history.history_df)
        self.logger = get_logger()

    def perform_operation(self, operation_name):
        """Perform an operation interactively using input()."""
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            func = OperationFactory.create(operation_name)
            result = func(a, b)
            calc = Calculation(a, b, operation_name, result)
            self.history.add(calc)
            self.memento.save(self.history.history_df)
            print(f"Result: {result}")
            return result
        except Exception as e:
            print(f"Error: {e}")

    def undo(self):
        """Undo last operation."""
        prev_state = self.memento.undo()
        if prev_state is not None:
            self.history.history_df = prev_state
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    def redo(self):
        """Redo previously undone operation."""
        next_state = self.memento.redo()
        if next_state is not None:
            self.history.history_df = next_state
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    def clear_history(self):
        """Clear all history records."""
        self.history.clear()
        self.memento.save(self.history.history_df)
        print("History cleared.")

    def show_history(self):
        """Display stored calculation history."""
        if getattr(self.history, "history_df", pd.DataFrame()).empty:
            print("No history available.")
        else:
            print(self.history.history_df.to_string(index=False))

    def help(self):
        """Show available commands."""
        print("\nAvailable Commands:\n")
        print("help       - Display all available commands")
        print("clear      - Clear calculation history")
        print("undo       - Undo the last operation")
        print("redo       - Redo the last undone operation")
        print("history    - Show calculation history")
        print("exit       - No description available.\n")
