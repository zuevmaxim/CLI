from io import TextIOBase

from environment.Environment import Environment
from environment.os_environment import extend_environment
from handlers.HandlersNet import HandlersNet


def enable_debug_logging() -> None:
    import logging
    logging.basicConfig(level=logging.DEBUG)


class Shell:
    """Shell is an entry point to commands execution."""

    def __init__(self, input_stream: TextIOBase, output_stream: TextIOBase, debug=False):
        self.env = Environment()
        extend_environment(self.env)
        self.handlers_net = HandlersNet(self.env, input_stream, output_stream)
        if debug:
            enable_debug_logging()

    def run(self) -> None:
        """Start command processing."""
        self.handlers_net.run()
