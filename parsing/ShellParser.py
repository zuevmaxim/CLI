from lark import Lark, Transformer, v_args
from lark.exceptions import LarkError, UnexpectedCharacters, UnexpectedToken

from ShellException import ShellException


class ShellParser:
    def __init__(self, command_factory):
        grammar_file = 'parsing/ShellGrammar.lark'
        file = open(grammar_file)
        self.parser = Lark(file, parser='earley')
        file.close()
        self.shell_transformer = ShellTransformer(command_factory)

    def parse(self, string):
        try:
            tree = self.get_ast(string)
            commands = self.shell_transformer.transform(tree)
            return commands
        except (UnexpectedCharacters, UnexpectedToken) as e:
            raise ShellException('Unexpected characters at position %s' % e.pos_in_stream)
        except LarkError:
            raise ShellException('Parse error')

    def get_ast(self, string):
        return self.parser.parse(string)


class ShellTransformer(Transformer):
    """Converts AST to list of commands."""

    def __init__(self, command_factory):
        super().__init__(visit_tokens=True)
        self.command_factory = command_factory

    NAME = str
    COMMAND_NAME = str
    SINGLE_QUOTE = str
    DOUBLE_QUOTE = str
    WORD = str

    @staticmethod
    @v_args(inline=True)
    def string(arg):
        return arg

    @staticmethod
    def args(args):
        return args

    @v_args(inline=True)
    def command(self, name, args):
        return self.command_factory.create_command(name, args)

    @staticmethod
    def commands(args):
        return args

    def equality(self, args):
        return [self.command_factory.create_command(self.command_factory.equality_command_name, args)]

    @staticmethod
    @v_args(inline=True)
    def start(commands_list):
        return commands_list
