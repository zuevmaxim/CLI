from lark import Transformer, Token, v_args
from lark.exceptions import UnexpectedCharacters, UnexpectedToken, LarkError
from lark.reconstruct import Reconstructor

from environment.Environment import Environment
from errors.ShellException import ShellException
from files.files_io import os_file_path
from parsing.LarkParserLoader import LarkParserLoader


class SubstitutionParser:
    """Parse input in order to substitute all variables($var)."""

    parser_path = os_file_path('parsing', 'substitution', 'Substitution.lark')

    def __init__(self):
        self.parser = LarkParserLoader.create_parser(self.parser_path)

    def parse(self, env: Environment, string: str) -> str:
        """Parse input, substitute variable and return the result."""
        try:
            tree = self.parser.parse(string)

            transformer = SubstitutionTransformer(env)
            tree = transformer.transform(tree)

            reconstructor = Reconstructor(self.parser)
            return reconstructor.reconstruct(tree)
        except (UnexpectedCharacters, UnexpectedToken) as e:
            raise ShellException('[Substitution]Unexpected characters at position %s' % e.pos_in_stream)
        except LarkError:
            raise ShellException('[Substitution]Parse error')


class SubstitutionTransformer(Transformer):
    """Replace all substitution tokens by variable value."""

    string_token = 'STRING'
    internal_string_token = 'INTERNAL_STRING'

    def __init__(self, env: Environment):
        super().__init__()
        self.env = env

    @v_args(inline=True)
    def substitution(self, name: str) -> Token:
        value = self.env.get(name)
        return Token(self.string_token, value)

    @v_args(inline=True)
    def internal_substitution(self, name: str) -> Token:
        value = self.env.get(name)
        return Token(self.internal_string_token, value)
