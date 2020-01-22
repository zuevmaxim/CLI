from lark import Lark, Transformer, Token
from lark.exceptions import UnexpectedCharacters, UnexpectedToken, LarkError
from lark.reconstruct import Reconstructor

from ShellException import ShellException


class SubstitutionParser:
    def __init__(self):
        substitution_file = 'substitution/Substitution.lark'
        file = open(substitution_file)
        self.parser = Lark(file, parser="lalr")
        file.close()

    def parse(self, env, string):
        try:
            tree = self.parser.parse(string)

            transformer = SubstitutionTransformer(env)
            tree = transformer.transform(tree)

            reconstructor = Reconstructor(self.parser)
            return reconstructor.reconstruct(tree)
        except (UnexpectedCharacters, UnexpectedToken) as e:
            raise ShellException('Unexpected characters at position %s' % e.pos_in_stream)
        except LarkError:
            raise ShellException('Parse error')


class SubstitutionTransformer(Transformer):
    def __init__(self, env):
        super().__init__()
        self.env = env
        self.string_token = "INTERNAL_STRING"

    def substitution(self, args):
        name = self.env.get(args[1])
        return Token(self.string_token, name)
