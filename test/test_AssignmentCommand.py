import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.AssignmentCommand import AssignmentCommand
from environment.Environment import Environment
from test.CommandTest import CommandTest


class AssignmentCommandTest(CommandTest):
    @parameterized.expand([
        ('empty', ['x', ''], ''),
        ('with value', ['var', 'val'], ''),
        ('var_name', ['var_name', 'val'], ''),
        ('input', ['var', 'val'], 'hello from input'),
    ])
    def test(self, _, args, input_string):
        self.command_test(args, input_string, '')
        self.assertEqual(args[1], self.environment.get(args[0]))

    def command(self, args: list, environment: Environment) -> Command:
        return AssignmentCommand(args, environment)


if __name__ == '__main__':
    unittest.main()
