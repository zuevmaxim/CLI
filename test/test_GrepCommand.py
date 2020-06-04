import unittest

from parameterized import parameterized

from commands.Command import Command
from commands.GrepCommand import GrepCommand, GrepArgsParser
from environment.Environment import Environment
from errors.ShellException import ShellException
from test.CommandTest import CommandTest

file = 'test/test_file_3.txt'
fileNotExists = 'test/test_file_0.txt'


class GrepCommandTest(CommandTest):
    @parameterized.expand([
        ('simple', ['hello'], 'hello', 'hello'),
        ('multiline', ['hello'], 'hello there\nhey\nhello world', 'hello there\nhello world'),
        ('regexp *', ['he.*'], 'hello there\nhey\nhello world', 'hello there\nhey\nhello world'),
        ('regexp ^$', ['^a*$'], '\naa\na \nabba', '\naa\n'),
        ('ignore case', ['-i', 'heLlO'], 'hello there\nhey\nhello world', 'hello there\nhello world'),
        ('words only', ['-w', 'hell'], 'hello there\nhey\nhello world\nhello from hell', 'hello from hell'),
        ('several flags', ['-iw', 'hELl'], 'hello there\nhey\nhello world\nhello from hell', 'hello from hell'),
        ('add lines', ['-A', '1', 'hello'], 'hello there\nhey\nhello world', 'hello there\nhey\nhello world'),
        ('from file', ['Some', file], '', 'Some string.\nSome other string.\nSomeone\n')
    ])
    def test(self, _, args, input_string, output_string):
        self.command_test(args, input_string, output_string)

    def command(self, args: list, environment: Environment) -> Command:
        return GrepCommand(args, environment)

    def testNoSuchFile(self):
        command = self.create_command(['some string', fileNotExists])
        self.executeCheckCode(command, 1)

    def testError(self):
        command = self.create_command(['-r', 'some string', fileNotExists])
        self.executeCheckCode(command, 1)


class ArgParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = GrepArgsParser()

    @parameterized.expand([
        ('unknown flag', ['-r', 'some']),
        ('empty', []),
        ('pattern missing', ['-i']),
        ('expected number', ['-A', 'some']),
        ('unknown argument', ['a', 'b', 'c']),
        ('negative number', ['-A', '-1', 'some'])
    ])
    def test(self, _, args):
        self.assertRaises(ShellException, lambda: self.parser.parse(args))

    @parameterized.expand([
        ('default', ['some'], False, False, 0),
        ('ignore', ['-i', 'some'], True, False, 0),
        ('words', ['-w', 'some'], False, True, 0),
        ('add', ['-A', '10', 'some'], False, False, 10),
        ('add ignore', ['-A', '10', '-i', 'some'], True, False, 10),
        ('add words', ['-A', '10', '-w', 'some'], False, True, 10),
        ('ignore words', ['-i', '-w', 'some'], True, True, 0),
        ('all', ['-i', '-w', '-A', '10', 'some'], True, True, 10),
    ])
    def test(self, _, args, ignore, words, add):
        res = self.parser.parse(args)
        self.assertEqual(ignore, res.i)
        self.assertEqual(words, res.w)
        self.assertEqual(add, res.A)


if __name__ == '__main__':
    unittest.main()
