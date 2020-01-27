import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.WcCommand import WcCommand, WcStatistics
from environment.Environment import Environment
from test.CommandTest import CommandTest

file1 = 'test/test_file_1.txt'
file2 = 'test/test_file_2.txt'
fileNotExists = 'test/test_file_0.txt'


class WcCommandTest(CommandTest):
    @parameterized.expand([
        ('empty', [], '', 'newlines = 0;  words = 0; bytes = 0'),
        ('one arg', [file1], '', 'newlines = 1;  words = 2; bytes = 12 %s' % file1),
        ('args', [file1, file2], '',
         "newlines = 1;  words = 2; bytes = 12 %s\n"
         "newlines = 2;  words = 5; bytes = 31 %s\n"
         "newlines = 3;  words = 7; bytes = 43 total" % (file1, file2)),
        ('input', [], 'Hello from input', 'newlines = 1;  words = 3; bytes = 16'),
        ('input', [], 'Hello from input\nHello again', 'newlines = 2;  words = 5; bytes = 28'),
        ('input and args', [file1], 'Hello from input', 'newlines = 1;  words = 2; bytes = 12 %s' % file1),
    ])
    def test(self, _, args, input_string, output_string):
        self.command_test(args, input_string, output_string)

    def command(self, args: list, environment: Environment) -> Command:
        return WcCommand(args, environment)

    def testNoSuchFile(self):
        command = self.create_command([fileNotExists])
        self.executeCheckCode(command, 1)

    def testNoSuchFileSeveral(self):
        command = self.create_command([fileNotExists, file2])
        self.executeCheckCode(command, 1)
        self.assertOutputEquals(
            'newlines = 2;  words = 5; bytes = 31 %s\n'
            'newlines = 2;  words = 5; bytes = 31 total' % file2)

    @parameterized.expand([
        ('empty', '', WcStatistics(0, 0, 0)),
        ('one word', 'Hello_world', WcStatistics(1, 1, 11)),
        ('one line', 'Hello world', WcStatistics(1, 2, 11)),
        ('multi line', 'Hello world\nHello again', WcStatistics(2, 4, 23))
    ])
    def testWcCalculateStatistics(self, _, string: str, statistics: WcStatistics):
        self.assertEqual(statistics, WcCommand.calculate_statistics(string))


if __name__ == '__main__':
    unittest.main()
