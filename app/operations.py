from app.exceptions import OperationError

class OperationFactory:
    @staticmethod
    def create(operation):
        ops = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: a / b if b != 0 else float("inf"),
            "power": lambda a, b: a ** b,
            "root": lambda a, b: a ** (1/b),
            "modulus": lambda a, b: a % b,
            "int_divide": lambda a, b: a // b,
            "percent": lambda a, b: (a / b) * 100,
            "abs_diff": lambda a, b: abs(a - b),
        }
        if operation not in ops:
            raise OperationError(f"Unsupported operation '{operation}'")
        return ops[operation]
