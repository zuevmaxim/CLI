import unittest

from environment.Environment import Environment
from substitution.SubstitutionParser import SubstitutionParser


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

    def testWithoutSubstitution(self):
        strings = ['echo hello | wc',
                   'echo "hello"',
                   "echo 'hello'",
                   'x=ghj',
                   'cat file.txt',
                   "cat '$x'",
                   "cat '\"$x\"'",
                   ]
        for string in strings:
            res = self.parser.parse(self.env, string)
            self.assertEqual(string, res)


if __name__ == '__main__':
    unittest.main()
