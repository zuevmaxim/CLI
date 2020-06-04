import unittest

from parameterized import parameterized

from commands.CatCommand import CatCommand
from commands.CommandFactory import CommandFactory
from commands.CustomCommand import CustomCommand
from commands.EchoCommand import EchoCommand
from commands.AssignmentCommand import AssignmentCommand
from commands.ExitCommand import ExitCommand
from commands.PwdCommand import PwdCommand
from commands.WcCommand import WcCommand
from environment.Environment import Environment
from parsing.parser.ShellParser import ShellParser


class ShellTransformerTest(unittest.TestCase):
    command_factory = CommandFactory(Environment())

    def setUp(self) -> None:
        self.parser = ShellParser(ShellTransformerTest.command_factory)

    def parse(self, string):
        return self.parser.parse(string)

    def testEmpty(self):
        result = self.parse('')
        self.assertEqual(0, len(result))

    def testEcho(self):
        result = self.parse('echo 123 | echo "hey" | echo 7')
        self.assertEqual(3, len(result))
        args = ['123', 'hey', '7']
        for command, arg in zip(result, args):
            self.assertTrue(isinstance(command, EchoCommand))
            self.assertEqual([arg], command.args)

    def testExit(self):
        result = self.parse('exit')
        self.assertEqual(1, len(result))
        command = result[0]
        self.assertTrue(isinstance(command, ExitCommand))

    @parameterized.expand([
        ('echo', 'echo 123', EchoCommand, ['123']),
        ('exit', 'exit', ExitCommand, []),
        ('cat', 'cat main.py', CatCommand, ['main.py']),
        ('custom command', '/bin/sh main.sh', CustomCommand, ['/bin/sh', 'main.sh']),
        ('equality', 'x = 3', AssignmentCommand, ['x', '3']),
        ('pwd', 'pwd', PwdCommand, []),
        ('wc', 'wc main.py', WcCommand, ['main.py']),
    ])
    def test(self, _, string, command_type, args):
        result = self.parse(string)
        self.assertEqual(1, len(result))
        command = result[0]
        self.assertTrue(isinstance(command, command_type))
        self.assertEqual(args, command.args)


if __name__ == '__main__':
    unittest.main()
