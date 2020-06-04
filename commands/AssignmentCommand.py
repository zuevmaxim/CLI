import io
import logging

from commands.Command import Command


class AssignmentCommand(Command):
    """Set variable value. Example: 'x = $HOME'."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        (name, value) = self.args
        logging.debug("[AssignmentCommand] %s=%s", name, value)
        self.environment.set(name, value)
        return 0
