from lark import Transformer, v_args, Tree
from lark.exceptions import LarkError, UnexpectedCharacters, UnexpectedToken

from commands.Command import Command
from commands.CommandFactory import CommandFactory
from errors.ShellException import ShellException
from parsing.LarkParserLoader import LarkParserLoader


class ShellParser:
    """Parse input string to list of commands."""

    def __init__(self, command_factory: CommandFactory):
        self.parser = LarkParserLoader.create_parser('parsing/parser/ShellGrammar.lark')
        self.shell_transformer = ShellTransformer(command_factory)

    def parse(self, string: str) -> list:
        try:
            tree = self.get_ast(string)
            commands = self.shell_transformer.transform(tree)
            return commands
        except (UnexpectedCharacters, UnexpectedToken) as e:
            raise ShellException('[Parser]Unexpected characters at position %s' % e.pos_in_stream)
        except LarkError:
            raise ShellException('[Parser]Parse error')

    def get_ast(self, string: str) -> Tree:
        """Returns input string AST representation."""
        return self.parser.parse(string)


class ShellTransformer(Transformer):
    """
    Converts AST to list of commands.
    Methods represent mappers from AST node to it's content.
    """

    def __init__(self, command_factory: CommandFactory):
        super().__init__(visit_tokens=True)
        self.command_factory = command_factory

    NAME = str
    COMMAND_NAME = str
    SINGLE_QUOTE = str
    DOUBLE_QUOTE = str
    WORD = str

    @staticmethod
    @v_args(inline=True)
    def string(arg: str) -> str:
        return arg

    @staticmethod
    def args(args: list) -> list:
        return args

    @v_args(inline=True)
    def command(self, name: str, args: list) -> Command:
        return self.command_factory.create_command(name, args)

    @staticmethod
    def commands(args: list) -> list:
        return args

    def equality(self, args: list) -> list:
        return [self.command_factory.create_command(self.command_factory.equality_command_name, args)]

    @staticmethod
    def eps(_) -> list:
        return []

    @staticmethod
    @v_args(inline=True)
    def start(commands_list: list) -> list:
        return commands_list
