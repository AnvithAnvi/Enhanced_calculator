from app.exceptions import ValidationError
from app.calculator_config import CalculatorConfig

def validate_number(value):
    try:
        value = float(value)
    except ValueError:
        raise ValidationError("Input must be a number.")
    if abs(value) > CalculatorConfig.MAX_INPUT_VALUE:
        raise ValidationError(f"Value exceeds {CalculatorConfig.MAX_INPUT_VALUE}.")
    return value

def validate_numbers(a, b):
    """Validate that both inputs can be safely converted to floats."""
    try:
        a = float(a)
        b = float(b)
        return a, b
    except ValueError:
        raise ValueError("Inputs must be numeric values.")
