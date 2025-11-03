class OperationError(Exception):
    """Raised when an invalid operation is requested."""
    pass

class ValidationError(Exception):
    """Raised when input validation fails."""
    pass

class CalculationError(Exception):
    """Custom exception for calculator errors."""
    def __init__(self, message="An error occurred during calculation."):
        super().__init__(message)
