import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.ExitCommand import ExitCommand
from environment.Environment import Environment
from test.CommandTest import CommandTest


class ExitCommandTest(CommandTest):
    @parameterized.expand([
        ('empty', [], '', ''),
        ('one arg', ['hello'], '', ''),
        ('args', ['Hello', 'world', '!'], '', ''),
        ('input', [], 'Hello world', ''),
        ('input with args', ['Hello', 'world'], 'Hello from input', ''),
    ])
    def test(self, _, args, input_string, output_string):
        self.command_test(args, input_string, output_string)
        self.assertTrue(self.environment.exit)

    def command(self, args: list, environment: Environment) -> Command:
        return ExitCommand(args, environment)

    def testEnvironmentWithoutExit(self):
        self.assertFalse(self.environment.exit)


if __name__ == '__main__':
    unittest.main()
