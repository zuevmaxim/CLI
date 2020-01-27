import logging

from environment.Environment import Environment
from handlers.Handler import Handler
from substitution.SubstitutionParser import SubstitutionParser


class SubstitutionHandler(Handler):
    """Substitute all variables in string from current environment."""

    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.parser = SubstitutionParser()

    def run(self, string: str) -> None:
        logging.debug("[SubstitutionHandler] input = %s", string)
        result = self.parser.parse(self.environment, string)
        self.on_finish(result)
