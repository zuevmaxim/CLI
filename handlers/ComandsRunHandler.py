import io
import logging

from handlers.Handler import Handler


class CommandsRunHandler(Handler):
    """Runs commands one by one passing data."""

    def run(self, commands: list) -> None:
        logging.debug("[CommandsRunHandler] input = %s", str(commands))
        input_stream = io.StringIO()
        output_stream = io.StringIO()
        for command in commands:
            self.environment.code = command.execute(input_stream, output_stream)
            if self.environment.exit:
                return
            input_stream, output_stream = output_stream, input_stream
            output_stream.flush()
        result = input_stream.getvalue()
        self.on_finish(result)
