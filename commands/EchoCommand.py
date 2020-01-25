import logging

from commands.Command import Command


class EchoCommand(Command):
    def execute(self, input_stream, output_stream):
        logging.debug("[EchoCommand] args = " + str(self.args))
        output_stream.write(" ".join(self.args))
        return 0
