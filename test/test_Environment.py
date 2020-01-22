import unittest

from environment.Environment import Environment
from ShellException import ShellException


class EnvironmentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.env = Environment()

    def testEmpty(self):
        self.assertRaises(ShellException, lambda: self.env.get('x'))

    def testExisting(self):
        self.env.set('x', 'y')
        self.assertEqual('y', self.env.get('x'))

    def testNonExisting(self):
        self.env.set('x', 'y')
        self.assertRaises(ShellException, lambda: self.env.get('y'))


if __name__ == '__main__':
    unittest.main()
