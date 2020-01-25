from commands.Command import Command
from commands.EchoCommand import EchoCommand
from commands.EqualityCommand import EqualityCommand
from commands.ExitCommand import ExitCommand
from environment import Environment


class CommandFactory:
    """Creates command instance by name."""

    equality_command_name = "#equality"

    def __init__(self, environment: Environment):
        self.environment = environment
        self.switcher = {
            "echo": self.create_echo,
            "exit": self.create_exit,
            CommandFactory.equality_command_name: self.create_equality
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
            exit(1)  # TODO create CustomCommand

    def create_echo(self, args: list) -> EchoCommand:
        return EchoCommand(args, self.environment)

    def create_exit(self, args: list) -> ExitCommand:
        return ExitCommand(args, self.environment)

    def create_equality(self, args: list) -> EqualityCommand:
        return EqualityCommand(args, self.environment)
