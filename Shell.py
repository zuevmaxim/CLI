from environment.Environment import Environment
from environment.os_environment import extend_environment
from handlers.HandlersNet import HandlersNet


class Shell:
    """Shell is an entry point to commands execution."""

    def __init__(self):
        self.env = Environment()
        extend_environment(self.env)
        self.handlers_net = HandlersNet(self.env)

    def execute(self, input_string: str) -> None:
        """Start command processing."""
        self.handlers_net.run(input_string)

    def is_exit(self) -> bool:
        """Check exit flag."""
        return self.env.exit
