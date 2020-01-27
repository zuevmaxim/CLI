import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.EchoCommand import EchoCommand
from environment.Environment import Environment
from test.CommandTest import CommandTest


class EchoCommandTest(CommandTest):
    @parameterized.expand([
        ('empty', [], '', ''),
        ('one arg', ['hello'], '', 'hello'),
        ('args', ['Hello', 'world', '!'], '', 'Hello world !'),
        ('input', [], 'Hello world', ''),
        ('input with args', ['Hello', 'world'], 'Hello from input', 'Hello world'),
    ])
    def test(self, _, args, input_string, output_string):
        self.command_test(args, input_string, output_string)

    def command(self, args: list, environment: Environment) -> Command:
        return EchoCommand(args, environment)


if __name__ == '__main__':
    unittest.main()
