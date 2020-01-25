import logging

from commands.CommandFactory import CommandFactory
from environment.Environment import Environment
from handlers.Handler import Handler
from parsing.ShellParser import ShellParser


class ParseHandler(Handler):
    """Parse input string to list of commands."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.parser = ShellParser(CommandFactory(environment))

    def run(self, input_string: str) -> None:
        result = self.parser.parse(input_string)
        logging.debug("[ParseHandler] input = " + input_string + ", output = " + str(result))
        self.on_finish(result)
