import io
import logging
import os
import argparse

from commands.Command import Command


class LsCommand(Command):
    """List files and directories command."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        # TODO for Maxim: improve code for windows()
        # https://stackoverflow.com/questions/20590704/use-python-to-reproduce-bash-command-ls-a-output
        # @user596374: don't mix Unicode and bytestrings. You could use
        # curdir = lambda path: fsdecode(os.curdir) if isinstance(path, unicode) else os.curdir
        parser = argparse.ArgumentParser(prog='ls')
        parser.add_argument('path', nargs='?', help='path, where we should list files and directories. Default=\'.\'',
                            default='.')
        try:
            args = vars(parser.parse_args(self.args))
        except SystemExit:
            output_stream.write("Bad arguments")
            return 1

        path = args.get('path')
        logging.debug("[LsCommand] path=%s", path)
        try:
            nodes = [os.curdir, os.pardir] + os.listdir(path)
        except OSError:
            output_stream.write("Something went wrong")
            return 1
        output_stream.write(str(' '.join(sorted(nodes))))
        return 0
