from io import TextIOBase

from environment.Environment import Environment
from errors.ShellException import ShellException
from handlers.Handler import Handler


class InputHandler(Handler):
    """Reads line by line from input_stream."""

    def __init__(self, environment: Environment, input_stream: TextIOBase):
        super().__init__(environment)
        self.input_stream = input_stream

    def run(self, _) -> None:
        while not self.environment.exit:
            try:
                input_string = self.input_stream.readline()[:-1]
                self.on_finish(input_string)
            except ShellException as e:
                print(e.error)
            except Exception as e:
                print(e)
