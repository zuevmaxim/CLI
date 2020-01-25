import io
import logging
import os

from commands.Command import Command


class PwdCommand(Command):
    """PrintWorkingDirectory command."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        path = os.getcwd()
        logging.debug("[PwdCommand] wd=%s" % path)
        output_stream.write(path)
        return 0
