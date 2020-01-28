from lark import Transformer, Token, v_args
from lark.exceptions import UnexpectedCharacters, UnexpectedToken, LarkError
from lark.reconstruct import Reconstructor

from environment.Environment import Environment
from errors.ShellException import ShellException
from parsing.LarkParserLoader import LarkParserLoader


class SubstitutionParser:
    """Parse input in order to substitute all variables($var)."""

    def __init__(self):
        self.parser = LarkParserLoader.create_parser('parsing/substitution/Substitution.lark')

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
