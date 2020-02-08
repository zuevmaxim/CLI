from commands.CatCommand import CatCommand
from commands.Command import Command
from commands.CustomCommand import CustomCommand
from commands.EchoCommand import EchoCommand
from commands.EqualityCommand import EqualityCommand
from commands.ExitCommand import ExitCommand
from commands.GrepCommand import GrepCommand
from commands.PwdCommand import PwdCommand
from commands.WcCommand import WcCommand
from environment import Environment


class CommandFactory:
    """Creates command instance by name."""

    equality_command_name = "#equality"

    def __init__(self, environment: Environment):
        self.environment = environment
        self.switcher = {
            "echo": self.create_echo,
            "exit": self.create_exit,
            CommandFactory.equality_command_name: self.create_equality,
            "pwd": self.create_pwd,
            "cat": self.create_cat,
            "wc": self.create_wc,
            "grep": self.create_grep,
        }

    def create_command(self, command_name: str, args: list) -> Command:
        """
        Create command by name.
        :param command_name: command name, if command is unknown CustomCommand created.
        :param args: command arguments
        """
        if command_name in self.switcher:
            getter = self.switcher[command_name]
            return getter(args)
        else:
            return self.create_custom_command([command_name] + args)

    def create_echo(self, args: list) -> EchoCommand:
        return EchoCommand(args, self.environment)

    def create_exit(self, args: list) -> ExitCommand:
        return ExitCommand(args, self.environment)

    def create_equality(self, args: list) -> EqualityCommand:
        return EqualityCommand(args, self.environment)

    def create_pwd(self, args: list) -> PwdCommand:
        return PwdCommand(args, self.environment)

    def create_cat(self, args: list) -> CatCommand:
        return CatCommand(args, self.environment)

    def create_wc(self, args: list) -> WcCommand:
        return WcCommand(args, self.environment)

    def create_grep(self, args: list) -> GrepCommand:
        return GrepCommand(args, self.environment)

    def create_custom_command(self, args: list) -> CustomCommand:
        return CustomCommand(args, self.environment)
