import io
import logging
import os

from commands.ArgParser import ArgParser
from commands.Command import Command


class CdArgsParser(ArgParser):
    """Parser for cd command arguments."""

    def __init__(self):
        super().__init__()
        self.add_argument('path', nargs='?', help='path to move. Default: \'$HOME\'',
                          default=os.path.expanduser("~"))


class CdCommand(Command):
    """Change working directory command."""

    parser = CdArgsParser()

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        args = CdCommand.parser.parse_args(self.args)
        path = args.path
        logging.debug("[CdCommand] path=%s", path)
        try:
            os.chdir(path)
        except FileNotFoundError:
            output_stream.write("Directory not found!")
            return 2
        except PermissionError:
            output_stream.write("Permission Error1")
            return 3
        except NotADirectoryError:
            output_stream.write("It is not a directory!")
            return 4
        except OSError:
            output_stream.write("Something went wrong")
            return 1
        return 0
