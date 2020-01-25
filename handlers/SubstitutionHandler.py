import logging

from handlers.Handler import Handler
from substitution.SubstitutionParser import SubstitutionParser


class SubstitutionHandler(Handler):
    """Substitute all variables in string from current environment."""

    def __init__(self, environment):
        super().__init__(environment)
        self.parser = SubstitutionParser()

    def run(self, string):
        result = self.parser.parse(self.environment, string)
        logging.debug("[SubstitutionHandler] input = " + string + ", output = " + result)
        self.on_finish(result)
