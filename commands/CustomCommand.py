import io
import logging
import subprocess

from commands.Command import Command


class CustomCommand(Command):
    """
    Custom command is used when no build-in command found.
    Command name is being found in file system and in PATH.
    """

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        command, args = self.args[0], self.args[1:]
        logging.debug("[CustomCommand, %s] args = %s", command, str(args))
        process = subprocess.Popen(self.args, universal_newlines=True,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out_str, err_str) = process.communicate(input_stream.getvalue())
        output_stream.write(out_str)
        if len(err_str) > 0:
            logging.error("[Custom command, %s] %s", command, err_str)
        return process.returncode
