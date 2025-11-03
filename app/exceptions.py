class OperationError(Exception):
    """Raised when an invalid operation is requested."""
    pass

class ValidationError(Exception):
    """Raised when input validation fails."""
    pass
