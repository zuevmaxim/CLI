import io
import logging

from commands.Command import Command
from files.files_io import read_from_file_log_errors


class CatCommand(Command):
    """Cat command concatenates files given as arguments."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        logging.debug("[CatCommand] args = " + str(self.args))
        if len(self.args) > 0:
            success = True
            for file_name in self.args:
                success &= read_from_file_log_errors(file_name, output_stream, 'cat')
            return 0 if success else 1
        else:
            output_stream.write(input_stream.getvalue())
            return 0
