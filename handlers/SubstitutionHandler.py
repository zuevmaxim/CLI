from handlers.Handler import Handler
from substitution.SubstitutionParser import SubstitutionParser


class SubstitutionHandler(Handler):
    def __init__(self, environment):
        super().__init__(environment)
        self.parser = SubstitutionParser()

    def run(self, string):
        result = self.parser.parse(self.environment, string)
        self.on_finish(result)
