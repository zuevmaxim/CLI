from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, args):
        self.args = args

    @abstractmethod
    def execute(self, input_stream, output_stream):
        pass
