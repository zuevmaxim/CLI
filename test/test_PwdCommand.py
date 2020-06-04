import os
import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.PwdCommand import PwdCommand
from environment.Environment import Environment
from test.CommandTest import CommandTest

wd = os.getcwd()


class PwdCommandTest(CommandTest):
    @parameterized.expand([
        ('empty', [], '', wd),
        ('args', ['unexpected arg'], '', wd),
        ('input', [], 'unexpected input', wd),
        ('input and args', ['unexpected arg'], 'unexpected input', wd),
    ])
    def test(self, _, args, input_string, output_string):
        self.command_test(args, input_string, output_string)

    def command(self, args: list, environment: Environment) -> Command:
        return PwdCommand(args, environment)


if __name__ == '__main__':
    unittest.main()
