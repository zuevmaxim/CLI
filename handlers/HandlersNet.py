from io import TextIOBase

from environment.Environment import Environment
from handlers.ComandsRunHandler import CommandsRunHandler
from handlers.InputHandler import InputHandler
from handlers.OutputHandler import OutputHandler
from handlers.ParseHandler import ParseHandler
from handlers.SubstitutionHandler import SubstitutionHandler


class HandlersNet:
    """A net contains all handlers attached in correct order."""

    def __init__(self, environment: Environment, input_stream: TextIOBase, output_stream: TextIOBase):
        self.input_handler = InputHandler(environment, input_stream)
        self.substitution_handler = SubstitutionHandler(environment)
        self.parse_handler = ParseHandler(environment)
        self.commands_run_handler = CommandsRunHandler(environment)
        self.output_handler = OutputHandler(environment, output_stream)

        self.init_net()

    def init_net(self) -> None:
        self.input_handler.add_next(self.substitution_handler)
        self.substitution_handler.add_next(self.parse_handler)
        self.parse_handler.add_next(self.commands_run_handler)
        self.commands_run_handler.add_next(self.output_handler)

    def run(self) -> None:
        """Start processing of inputs."""
        self.input_handler.run(None)
