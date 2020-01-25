import unittest

from commands.CommandFactory import CommandFactory
from commands.EchoCommand import EchoCommand
from commands.ExitCommand import ExitCommand
from environment.Environment import Environment
from parsing.ShellParser import ShellParser


class ShellTransformerTest(unittest.TestCase):
    command_factory = CommandFactory(Environment())

    def setUp(self) -> None:
        self.parser = ShellParser(ShellTransformerTest.command_factory)

    def parse(self, string):
        return self.parser.parse(string)

    def testSingleEcho(self):
        result = self.parse('echo 123')
        self.assertEqual(1, len(result))
        command = result[0]
        self.assertTrue(isinstance(command, EchoCommand))
        self.assertEqual(['123'], command.args)

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


if __name__ == '__main__':
    unittest.main()
