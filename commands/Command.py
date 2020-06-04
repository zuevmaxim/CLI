import io
from abc import ABCMeta, abstractmethod

from environment import Environment


class Command(metaclass=ABCMeta):
    """Abstract command."""

    def __init__(self, args: list, environment: Environment):
        self.args = args
        self.environment = environment

    @abstractmethod
    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        """
        Execute a command.
        :return: execution status code, zero if OK
        """
        pass
