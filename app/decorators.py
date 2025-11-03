def command_info(description):
    """Decorator to tag a function with its help text."""
    def decorator(func):
        func._help_text = description
        return func
    return decorator
