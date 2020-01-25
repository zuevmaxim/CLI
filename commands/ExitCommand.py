import logging

from commands.Command import Command


class ExitCommand(Command):
    def execute(self, input_stream, output_stream):
        logging.debug("[ExitCommand]")
        self.environment.exit = True
