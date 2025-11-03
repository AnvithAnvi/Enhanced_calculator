from app.operations import OperationFactory
from app.calculation import Calculation
from app.history import History
from app.logger import LoggingObserver, AutoSaveObserver
from app.calculator_config import CalculatorConfig
from app.calculator_memento import Caretaker
from app.input_validators import validate_number
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset colors after each print


# ---------------------------------------------------------------------
# Decorator Pattern for Dynamic Help Menu
# ---------------------------------------------------------------------
def command_info(description):
    """Decorator to attach command descriptions for dynamic help menu."""
    def decorator(func):
        func._help_text = description
        return func
    return decorator


# ---------------------------------------------------------------------
# Calculator Class
# ---------------------------------------------------------------------
class Calculator:
    """Enhanced Calculator implementing Factory, Memento, Observer, and Decorator patterns."""

    def __init__(self):
        # Validate configuration and prepare environment
        CalculatorConfig.validate()

        # Core components
        self.history = History()
        self.caretaker = Caretaker()

        # Observers for logging and auto-saving
        self.observers = [
            LoggingObserver(CalculatorConfig.LOG_DIR),
            AutoSaveObserver(CalculatorConfig.HISTORY_DIR),
        ]

        # Command registry (dynamic)
        self.commands = {}

        # Register core commands
        self.register_command("help", self.help, "Display all available commands")
        self.register_command("history", self.show_history, "Display calculation history")
        self.register_command("clear", self.clear_history, "Clear all history entries")
        self.register_command("undo", self.undo, "Undo the last calculation")
        self.register_command("redo", self.redo, "Redo the last undone calculation")
        self.register_command("exit", exit, "Exit the calculator")

        # Register arithmetic operations dynamically
        operations = [
            ("add", "Add two numbers"),
            ("subtract", "Subtract two numbers"),
            ("multiply", "Multiply two numbers"),
            ("divide", "Divide two numbers"),
            ("power", "Raise one number to the power of another"),
            ("root", "Calculate the nth root of a number"),
            ("modulus", "Find the remainder of division"),
            ("int_divide", "Perform integer division"),
            ("percent", "Calculate percentage (a / b * 100)"),
            ("abs_diff", "Find absolute difference between two numbers"),
        ]
        for name, desc in operations:
            self.register_command(name, lambda op=name: self.perform_operation(op), desc)

    # -----------------------------------------------------------------
    # Helper Methods
    # -----------------------------------------------------------------
    def register_command(self, name, func, description=""):
        """Register a command dynamically with its description."""
        func._help_text = description
        self.commands[name] = func

    def notify_observers(self):
        """Notify all observers about new history updates."""
        for obs in self.observers:
            if hasattr(obs, "update"):
                obs.update(self.history)

    # -----------------------------------------------------------------
    # Operation Execution
    # -----------------------------------------------------------------
    def perform_operation(self, operation):
        """Perform a specific arithmetic operation."""
        try:
            a = validate_number(input(Fore.CYAN + "Enter first number: "))
            b = validate_number(input(Fore.CYAN + "Enter second number: "))

            func = OperationFactory.create(operation)
            result = round(func(a, b), CalculatorConfig.PRECISION)

            calc = Calculation(a, b, operation, result)
            self.caretaker.save(self.history._history)
            self.history.add(calc)

            print(Fore.GREEN + f"✅ Result: {calc}")
            self.notify_observers()

        except Exception as e:
            print(Fore.RED + f"❌ Error: {e}")

    # -----------------------------------------------------------------
    # History Management
    # -----------------------------------------------------------------
    def show_history(self):
        """Display all previous calculations."""
        if not self.history._history:
            print(Fore.YELLOW + "⚠️  No history yet.")
        else:
            print(Fore.CYAN + Style.BRIGHT + "📜 Calculation History:")
            for item in self.history._history:
                print(Fore.CYAN + str(item))

    def clear_history(self):
        """Clear all calculation history."""
        self.history.clear()
        print(Fore.MAGENTA + "🧹 History cleared successfully.")

    # -----------------------------------------------------------------
    # Undo / Redo Operations
    # -----------------------------------------------------------------
    def undo(self):
        """Revert to the previous calculator state."""
        prev_state = self.caretaker.undo(self.history._history)
        self.history._history = prev_state
        print(Fore.BLUE + "↩️  Undo complete.")

    def redo(self):
        """Redo the last undone calculator state."""
        next_state = self.caretaker.redo(self.history._history)
        self.history._history = next_state
        print(Fore.BLUE + "🔁 Redo complete.")

    # -----------------------------------------------------------------
    # Dynamic Help Menu (Decorator Pattern)
    # -----------------------------------------------------------------
    @command_info("Display all available commands dynamically")
    def help(self):
        """Display supported commands dynamically from registered functions."""
        print(Fore.CYAN + Style.BRIGHT + "\n📖 Available Commands:")
        for name, func in sorted(self.commands.items()):
            desc = getattr(func, "_help_text", "")
            print(Fore.CYAN + f" - {name}: {desc}")
        print(Fore.CYAN + "\nTip: Type a command (e.g., add, divide) and follow prompts.\n")
