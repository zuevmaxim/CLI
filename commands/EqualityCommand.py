import io

from commands.Command import Command


class EqualityCommand(Command):
    """Set variable value. Example: 'x = $HOME'."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        (name, value) = self.args
        self.environment.set(name, value)
        return 0
