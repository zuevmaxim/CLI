import io
import unittest
from abc import ABCMeta, abstractmethod

from commands.Command import Command
from environment.Environment import Environment


class CommandTest(unittest.TestCase, metaclass=ABCMeta):
    @abstractmethod
    def command(self, args: list, environment: Environment) -> Command:
        pass

    def setUp(self) -> None:
        self.environment = Environment()
        self.input_stream = io.StringIO()
        self.output_stream = io.StringIO()

    def execute(self, command: Command) -> int:
        return command.execute(self.input_stream, self.output_stream)

    def executeCheckCode(self, command: Command, expected_code=0) -> None:
        code = self.execute(command)
        self.assertEqual(expected_code, code)

    def assertOutputEquals(self, expected: str):
        self.assertEqual(expected, self.output_stream.getvalue())

    def command_test(self, args: list, input_string='', output_string=''):
        command = self.create_command(args)
        self.input_stream.write(input_string)
        self.executeCheckCode(command)
        self.assertOutputEquals(output_string)

    def create_command(self, args: list) -> Command:
        return self.command(args, self.environment)

    def execute_input(self, args, inp: str) -> str:
        command = self.create_command(args)
        self.input_stream.write(inp)
        self.execute(command)
        out = self.output_stream.getvalue()
        self.setUp()
        return out
