from errors.ShellException import ShellException


class Environment:
    """Environment contains state of shell."""

    def __init__(self):
        self.data = {}
        self.code = 0
        self.exit = False

    def set(self, key: str, value: str) -> None:
        """Set key variable to value."""
        self.data[key] = value

    def get(self, key: str) -> str:
        """
        Get variable key value
        :raises  ShellException if key variable is undefined
        """
        if key in self.data:
            return self.data[key]
        else:
            raise ShellException('No such variable %s' % key)
