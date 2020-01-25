import io
import logging
from os import path

from commands.Command import Command


class CatCommand(Command):
    """Cat command concatenates files given as arguments."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        if len(self.args) > 0:
            success = True
            for file_name in self.args:
                success &= self.read_from_file(file_name, output_stream)
            return 0 if success else 1
        else:
            output_stream.write(input_stream.getvalue())
            return 0

    @staticmethod
    def read_from_file(file_name: str, output_stream: io.StringIO) -> bool:
        """
        Reads file content into output_stream.
        :return: True on success
        """
        success = True
        if not path.exists(file_name):
            success = False
            logging.error('[cat] No such file %s' % file_name)
        elif not path.isfile(file_name):
            success = False
            logging.error('[cat] %s is not a file' % file_name)
        else:
            file = open(file_name)
            if file.mode == 'r':
                output_stream.write(file.read())
            else:
                success = False
                logging.error('[cat] Cannot read from file %s' % file_name)
            file.close()
        return success
