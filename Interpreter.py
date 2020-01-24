from environment.Environment import Environment
from environment.os_environment import extend_environment
from substitution.SubstitutionParser import SubstitutionParser


class Interpreter:
    def __init__(self):
        self.env = Environment()
        extend_environment(self.env)
        self.substitution_parser = SubstitutionParser()

    def interpret(self, input_string):
        substituted_string = self.substitution_parser.parse(self.env, input_string)
        print(substituted_string)
