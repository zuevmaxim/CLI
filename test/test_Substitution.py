import unittest

from parameterized import parameterized

from environment.Environment import Environment
from errors.ShellException import ShellException
from parsing.substitution.SubstitutionParser import SubstitutionParser


class SubstitutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = SubstitutionParser()
        self.env = Environment()

    def testSubstitution(self):
        self.env.set('x', 'x_value')
        res = self.parser.parse(self.env, '$x')
        self.assertEqual('x_value', res)

    def testSubstitutionInSingleQuotes(self):
        self.env.set('x', 'x_value')
        res = self.parser.parse(self.env, "'$x'")
        self.assertEqual("'$x'", res)

    def testSubstitutionInDoubleQuotes(self):
        self.env.set('x', 'x_value')
        res = self.parser.parse(self.env, '"hello $x"')
        self.assertEqual('"hello x_value"', res)

    def testSubstitutionInDoubleAndSingleQuotes(self):
        self.env.set('x', 'x_value')
        res = self.parser.parse(self.env, '"\'hello $x\'"')
        self.assertEqual('"\'hello x_value\'"', res)

    def testExit(self):
        self.env.set('x', 'ex')
        self.env.set('y', 'it')
        res = self.parser.parse(self.env, '$x$y')
        self.assertEqual('exit', res)

    @parameterized.expand([
        'echo hello | wc',
        'echo "hello"',
        "echo 'hello'",
        'x=ghj',
        'cat file.txt',
        "cat '$x'",
        "cat '\"$x\"'",
        'echo      hello',
        'echo \t hello     \t',
        '   ',
        '',
    ])
    def testWithoutSubstitution(self, string):
        res = self.parser.parse(self.env, string)
        self.assertEqual(string, res)

    @parameterized.expand([
        ('illegal var name', '$67', 1),
        ('wrong quotes', 'echo \'hello"', 5),
        ('wrong quotes', "echo 'hello", 5),
    ])
    def testUnexpectedCharacter(self, _, input_string, position):
        try:
            self.parser.parse(self.env, input_string)
        except ShellException as e:
            self.assertEqual('[Substitution]Unexpected characters at position %d' % position, e.error)
            return
        assert False

    @parameterized.expand([
        ('wrong quotes', 'echo "hello'),
        ('wrong quotes', 'echo "hello\''),
    ])
    def testParseError(self, _, input_string):
        try:
            self.parser.parse(self.env, input_string)
        except ShellException as e:
            self.assertEqual('[Substitution]Parse error', e.error)
            return
        assert False


if __name__ == '__main__':
    unittest.main()
