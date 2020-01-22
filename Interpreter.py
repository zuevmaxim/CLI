from environment.Environment import Environment
from substitution.SubstitutionParser import SubstitutionParser


class Interpreter:
    def __init__(self):
        self.env = Environment()
        self.substitution_parser = SubstitutionParser()

    def interpret(self, input_string):
        substituted_string = self.substitution_parser.parse(self.env, input_string)
        print(substituted_string)
