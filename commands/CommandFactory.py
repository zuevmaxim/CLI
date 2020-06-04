from commands.CatCommand import CatCommand
from commands.Command import Command
from commands.CustomCommand import CustomCommand
from commands.EchoCommand import EchoCommand
from commands.AssignmentCommand import AssignmentCommand
from commands.ExitCommand import ExitCommand
from commands.GrepCommand import GrepCommand
from commands.PwdCommand import PwdCommand
from commands.WcCommand import WcCommand
from commands.LsCommand import LsCommand
from commands.CdCommand import CdCommand
from environment import Environment


class CommandFactory:
    """Creates command instance by name."""

    assignment_command_name = "#assignment"

    def __init__(self, environment: Environment):
        self.environment = environment
        self.switcher = {
            "echo": self.create_echo,
            "exit": self.create_exit,
            CommandFactory.assignment_command_name: self.create_assignment,
            "pwd": self.create_pwd,
            "cat": self.create_cat,
            "wc": self.create_wc,
            "grep": self.create_grep,
            "ls": self.create_ls,
            "cd": self.create_cd,
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

    def create_assignment(self, args: list) -> AssignmentCommand:
        return AssignmentCommand(args, self.environment)

    def create_pwd(self, args: list) -> PwdCommand:
        return PwdCommand(args, self.environment)

    def create_cat(self, args: list) -> CatCommand:
        return CatCommand(args, self.environment)

    def create_wc(self, args: list) -> WcCommand:
        return WcCommand(args, self.environment)

    def create_ls(self, args: list) -> LsCommand:
        return LsCommand(args, self.environment)

    def create_cd(self, args: list) -> LsCommand:
        return CdCommand(args, self.environment)

    def create_grep(self, args: list) -> GrepCommand:
        return GrepCommand(args, self.environment)

    def create_custom_command(self, args: list) -> CustomCommand:
        return CustomCommand(args, self.environment)
