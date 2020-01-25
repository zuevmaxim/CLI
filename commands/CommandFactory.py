from commands.EchoCommand import EchoCommand


class CommandFactory:
    equality_command_name = "#equality"

    def __init__(self):
        self.switcher = {
            "echo": self.create_echo
        }

    def create_command(self, command_name, args):
        if command_name in self.switcher:
            getter = self.switcher[command_name]
            return getter(args)
        else:
            exit(1)

    @staticmethod
    def create_echo(args):
        return EchoCommand(args)
