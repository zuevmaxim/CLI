import io
import logging
import os

from commands.ArgParser import ArgParser
from commands.Command import Command


class LsArgsParser(ArgParser):
    """Parser for ls command arguments."""

    def __init__(self):
        super().__init__()
        self.add_argument('path', nargs='?', help='path, where we should list files and directories. Default=\'.\'',
                          default='.')


class LsCommand(Command):
    """List files and directories command."""

    parser = LsArgsParser()

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        args = LsCommand.parser.parse_args(self.args)
        path = args.path
        logging.debug("[LsCommand] path=%s", path)
        try:
            nodes = [os.curdir, os.pardir] + os.listdir(path)
        except OSError:
            output_stream.write("Something went wrong")
            return 1
        output_stream.write(str(' '.join(sorted(nodes))))
        return 0
