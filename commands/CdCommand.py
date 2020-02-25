import io
import logging
import os
import argparse

from commands.Command import Command


class CdCommand(Command):
    """change working directory command."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        parser = argparse.ArgumentParser()
        parser.add_argument('path', nargs='?', help='path to move. Default: \'$HOME\'',
                            default=self.environment.get('HOME'))
        args = vars(parser.parse_args(self.args))
        path = args.get('path')
        logging.debug("[LsCommand] path=%s", path)
        try:
            os.chdir(path)
        except OSError:
            output_stream.write("Something went wrong")
            return 1
        return 0
