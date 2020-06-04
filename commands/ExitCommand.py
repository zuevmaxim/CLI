import io
import logging

from commands.Command import Command


class ExitCommand(Command):
    """Exit command finishes shell execution."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        logging.debug("[ExitCommand]")
        self.environment.exit = True
        return 0
