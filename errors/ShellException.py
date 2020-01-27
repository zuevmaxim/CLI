class ShellException(BaseException):
    """Exception indicates error that prevents command execution."""

    def __init__(self, error: str):
        self.error = error
