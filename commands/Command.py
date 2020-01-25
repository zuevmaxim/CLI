from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, args, environment):
        self.args = args
        self.environment = environment

    @abstractmethod
    def execute(self, input_stream, output_stream):
        pass
