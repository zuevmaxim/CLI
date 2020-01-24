from environment.Environment import Environment
from environment.os_environment import extend_environment
from handlers.HandlersNet import HandlersNet


class Interpreter:
    def __init__(self):
        self.env = Environment()
        extend_environment(self.env)
        self.handlers_net = HandlersNet(self.env)

    def interpret(self, input_string):
        self.handlers_net.run(input_string)
