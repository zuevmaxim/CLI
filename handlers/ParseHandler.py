import logging

from commands.CommandFactory import CommandFactory
from handlers.Handler import Handler
from parsing.ShellParser import ShellParser


class ParseHandler(Handler):
    def __init__(self, environment):
        super().__init__(environment)
        self.parser = ShellParser(CommandFactory(environment))

    def run(self, input_string):
        result = self.parser.parse(input_string)
        logging.debug("[ParseHandler] input = " + input_string + ", output = " + str(result))
        self.on_finish(result)
