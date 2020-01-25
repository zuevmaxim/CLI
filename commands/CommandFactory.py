from commands.EchoCommand import EchoCommand
from commands.ExitCommand import ExitCommand


class CommandFactory:
    equality_command_name = "#equality"

    def __init__(self, environment):
        self.environment = environment
        self.switcher = {
            "echo": self.create_echo,
            "exit": self.create_exit,
        }

    def create_command(self, command_name, args):
        if command_name in self.switcher:
            getter = self.switcher[command_name]
            return getter(args)
        else:
            exit(1)

    def create_echo(self, args):
        return EchoCommand(args, self.environment)

    def create_exit(self, args):
        return ExitCommand(args, self.environment)
