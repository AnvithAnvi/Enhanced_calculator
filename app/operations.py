import math


def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else float("inf")
def power(a, b): return a ** b
def root(a, b): return round(a ** (1 / b), 6)
def modulus(a, b): return a % b


# ✅ Expose dictionary for direct import
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "root": root,
    "modulus": modulus,
}


class OperationFactory:
    """Factory pattern for calculator operations."""
    @staticmethod
    def create(operation_name):
        func = operations.get(operation_name)
        if not func:
            raise ValueError(f"Unknown operation: {operation_name}")
        return func
