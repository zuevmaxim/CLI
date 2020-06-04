import unittest

from parameterized import parameterized

from commands.CatCommand import CatCommand
from commands.Command import Command
from environment.Environment import Environment
from files.files_io import os_file_path
from test.CommandTest import CommandTest

file1 = os_file_path('test', 'test_file_1.txt')
file2 = os_file_path('test', 'test_file_2.txt')
fileNotExists = os_file_path('test', 'test_file_0.txt')


class CatCommandTest(CommandTest):
    @parameterized.expand([
        ('empty', [], '', ''),
        ('one arg', [file1], '', 'Hello world!'),
        ('args', [file1, file2], '', 'Hello world!Some string.\nSome other string.'),
        ('input', [], 'Hello from input', 'Hello from input'),
        ('input and args', [file1, file2], 'Hello from input', 'Hello world!Some string.\nSome other string.'),
    ])
    def test(self, _, args, input_string, output_string):
        self.command_test(args, input_string, output_string)

    def command(self, args: list, environment: Environment) -> Command:
        return CatCommand(args, environment)

    def testNoSuchFile(self):
        command = self.create_command([fileNotExists])
        self.executeCheckCode(command, 1)

    def testNoSuchFileSeveral(self):
        command = self.create_command([fileNotExists, file2])
        self.executeCheckCode(command, 1)
        self.assertOutputEquals('Some string.\nSome other string.')


if __name__ == '__main__':
    unittest.main()
