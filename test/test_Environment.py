import unittest

from ShellException import ShellException
from environment.Environment import Environment
from environment.os_environment import extend_environment


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

    def testOsEnvironment(self):
        extend_environment(self.env)
        self.assertTrue('PATH' in self.env.data)


if __name__ == '__main__':
    unittest.main()
