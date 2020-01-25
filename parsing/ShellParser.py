from lark import Lark
from lark.exceptions import LarkError, UnexpectedCharacters, UnexpectedToken

from ShellException import ShellException


class ShellParser:
    def __init__(self):
        grammar_file = 'parsing/ShellGrammar.lark'
        file = open(grammar_file)
        self.parser = Lark(file, parser='earley')
        file.close()

    def parse(self, string):
        try:
            tree = self.get_ast(string)
            return tree
        except (UnexpectedCharacters, UnexpectedToken) as e:
            raise ShellException('Unexpected characters at position %s' % e.pos_in_stream)
        except LarkError:
            raise ShellException('Parse error')

    def get_ast(self, string):
        return self.parser.parse(string)
