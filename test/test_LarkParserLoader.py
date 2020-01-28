import unittest

from errors.ShellError import ShellError
from parsing.LarkParserLoader import LarkParserLoader


class LarkParserLoaderTest(unittest.TestCase):
    def testSuccess(self):
        parser = LarkParserLoader.create_parser('parsing/parser/ShellGrammar.lark')
        self.assertIsNotNone(parser)

    def testFailNoFile(self):
        file = 'no_such_file.lark'
        try:
            LarkParserLoader.create_parser(file)
        except ShellError as e:
            self.assertEqual(e.error, '[Parser] Cannot load grammar file %s' % file)
            return
        assert False

    def testFailWrongGrammar(self):
        file = 'test/test_file_1.txt'
        try:
            LarkParserLoader.create_parser(file)
        except ShellError as e:
            self.assertTrue(e.error.startswith('[Parser] Error while creating parser: '))
            return
        assert False


if __name__ == '__main__':
    unittest.main()
