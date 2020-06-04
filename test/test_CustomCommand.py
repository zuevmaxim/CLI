import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.CustomCommand import CustomCommand
from environment.Environment import Environment
from environment.os_environment import extend_environment
from files.files_io import os_file_path
from test.CommandTest import CommandTest

script = os_file_path('test', 'script.py')


class CustomCommandTest(CommandTest):

    def command(self, args: list, environment: Environment) -> Command:
        extend_environment(environment)
        return CustomCommand(args, environment)

    @parameterized.expand([
        ('python', 'python', [script], '', 'Hello world!\n'),
    ])
    def test(self, _, name, args, input_string, output_string):
        self.command_test([name] + args, input_string, output_string)


if __name__ == '__main__':
    unittest.main()
