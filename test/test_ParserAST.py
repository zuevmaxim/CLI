import unittest

from lark import Tree, Token
from parameterized import parameterized

from commands.CommandFactory import CommandFactory
from environment.Environment import Environment
from errors.ShellException import ShellException
from parsing.parser.ShellParser import ShellParser

start = 'start'
assignment = 'assignment'
NAME = 'NAME'
WORD = 'WORD'
string = 'string'
SINGLE_QUOTE = 'SINGLE_QUOTE'
DOUBLE_QUOTE = 'DOUBLE_QUOTE'
commands = 'commands'
command = 'command'
COMMAND_NAME = 'COMMAND_NAME'
args = 'args'


class ASTParseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = ShellParser(CommandFactory(Environment()))

    def ast(self, input_string):
        return self.parser.get_ast(input_string)

    def testEqualityString(self):
        result = self.ast("x = 3")
        expected = Tree(start, [Tree(assignment, [Token(NAME, 'x'), Tree(string, [Token(WORD, '3')])])])
        self.assertEqual(expected, result)

    def testEqualityVarName(self):
        result = self.ast("var_x = 3")
        expected = Tree(start, [Tree(assignment, [Token(NAME, 'var_x'), Tree(string, [Token(WORD, '3')])])])
        self.assertEqual(expected, result)

    def testEqualitySingleQuoting(self):
        result = self.ast("x = '4 + 3'")
        expected = Tree(start, [Tree(assignment, [Token(NAME, 'x'), Tree(string, [Token(SINGLE_QUOTE, '4 + 3')])])])
        self.assertEqual(expected, result)

    def testEqualityDoubleQuoting(self):
        result = self.ast('x = "4 + 3"')
        expected = Tree(start, [Tree(assignment, [Token(NAME, 'x'), Tree(string, [Token(DOUBLE_QUOTE, '4 + 3')])])])
        self.assertEqual(expected, result)

    def testCommand(self):
        result = self.ast('pwd')
        expected = Tree(start, [Tree(commands, [Tree(command, [Token(COMMAND_NAME, 'pwd'), Tree(args, [])])])])
        self.assertEqual(expected, result)

    def testCustomCommand(self):
        result = self.ast('/bin/echo')
        expected = Tree(start, [Tree(commands, [Tree(command, [Token(COMMAND_NAME, '/bin/echo'), Tree(args, [])])])])
        self.assertEqual(expected, result)

    def testCommandWithOneArg(self):
        result = self.ast('echo 123')
        expected = Tree(start, [Tree(commands, [
            Tree(command, [Token(COMMAND_NAME, 'echo'), Tree(args, [Tree(string, [Token(WORD, '123')])])])])])
        self.assertEqual(expected, result)

    def testCommandWithArgs(self):
        result = self.ast("echo 123 '4 + 87'")
        expected = Tree(start, [Tree(commands, [Tree(command, [Token(COMMAND_NAME, 'echo'), Tree(args, [
            Tree(string, [Token(WORD, '123')]), Tree(string, [Token(SINGLE_QUOTE, '4 + 87')])])])])])
        self.assertEqual(expected, result)

    def testPipeCommands(self):
        result = self.ast("pwd | wc")
        expected = Tree(start, [Tree(commands, [Tree(command, [Token(COMMAND_NAME, 'pwd'), Tree(args, [])]),
                                                Tree(command, [Token(COMMAND_NAME, 'wc'), Tree(args, [])])])])
        self.assertEqual(expected, result)

    def testPipeCommandsWithArgs(self):
        result = self.ast("echo 'Hello world' 7 | wc")
        expected = Tree(start, [Tree(commands, [Tree(command, [Token(COMMAND_NAME, 'echo'), Tree(args, [
            Tree(string, [Token(SINGLE_QUOTE, 'Hello world')]), Tree(string, [Token(WORD, '7')])])]),
                                                Tree(command, [Token(COMMAND_NAME, 'wc'), Tree(args, [])])])])
        self.assertEqual(expected, result)

    def testPipes(self):
        result = self.ast("pwd | wc | wc | wc | wc")
        expected = Tree(start, [Tree(commands, [Tree(command, [Token(COMMAND_NAME, 'pwd'), Tree(args, [])]),
                                                Tree(command, [Token(COMMAND_NAME, 'wc'), Tree(args, [])]),
                                                Tree(command, [Token(COMMAND_NAME, 'wc'), Tree(args, [])]),
                                                Tree(command, [Token(COMMAND_NAME, 'wc'), Tree(args, [])]),
                                                Tree(command, [Token(COMMAND_NAME, 'wc'), Tree(args, [])])])])
        self.assertEqual(expected, result)

    @parameterized.expand([
        ('quotes command', '"echo" 123', 0),
        ('illegal var name', '8 = 3', 0),
    ])
    def testUnexpectedCharacter(self, _, input_string, position):
        try:
            self.parser.parse(input_string)
        except ShellException as e:
            self.assertEqual('[Parser]Unexpected characters at position %d' % position, e.error)
            return
        assert False

    @parameterized.expand([
        ('wrong quotes', 'echo "hello'),
        ('wrong quotes', 'echo \'hello"'),
    ])
    def testParseError(self, _, input_string):
        try:
            self.parser.parse(input_string)
        except ShellException as e:
            self.assertEqual('[Parser]Parse error', e.error)
            return
        assert False


if __name__ == '__main__':
    unittest.main()
