import io
import logging

from commands.Command import Command


class EchoCommand(Command):
    """Echo command prints it's arguments. Input stream is ignored."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        logging.debug("[EchoCommand] args = %s", str(self.args))
        output_stream.write(" ".join(self.args))
        return 0
