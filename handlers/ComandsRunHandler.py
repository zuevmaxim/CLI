import io
import logging

from handlers.Handler import Handler


class CommandsRunHandler(Handler):
    """Runs commands one by one passing data."""

    def run(self, commands: list) -> None:
        input_stream = io.StringIO()
        output_stream = io.StringIO()
        for command in commands:
            self.environment.code = command.execute(input_stream, output_stream)
            if self.environment.exit or self.environment.code != 0:
                return
            input_stream = output_stream
            output_stream = io.StringIO()
        result = input_stream.getvalue()
        logging.debug("[CommandsRunHandler] input = " + str(commands) + ", output = " + str(result))
        self.on_finish(result)
