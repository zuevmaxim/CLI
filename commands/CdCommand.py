import io
import logging
import os
import argparse

from commands.Command import Command


class CdCommand(Command):
    """change working directory command."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        parser = argparse.ArgumentParser(prog='cd')
        parser.add_argument('path', nargs='?', help='path to move. Default: \'$HOME\'',
                            default=os.path.expanduser("~"))
        try:
            args = vars(parser.parse_args(self.args))
        except SystemExit:
            output_stream.write("Bad arguments")
            return 1

        path = args.get('path')
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
