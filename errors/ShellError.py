class ShellError(BaseException):
    """Error raised when shell is wrong configured."""

    def __init__(self, error: str):
        self.error = error
