from lark import Lark, Transformer, Token
from lark.exceptions import UnexpectedCharacters, UnexpectedToken, LarkError
from lark.reconstruct import Reconstructor

from ShellException import ShellException
from environment.Environment import Environment


class SubstitutionParser:
    """Parse input in order to substitute all variables($var)."""

    def __init__(self):
        substitution_file = 'substitution/Substitution.lark'
        file = open(substitution_file)
        self.parser = Lark(file, parser="lalr")
        file.close()

    def parse(self, env: Environment, string: str) -> str:
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

    def __init__(self, env: Environment):
        super().__init__()
        self.env = env
        self.string_token = 'INTERNAL_STRING'

    def substitution(self, args: list) -> Token:
        name = self.env.get(args[1])
        return Token(self.string_token, name)
