import logging
from io import TextIOBase

from environment.Environment import Environment
from handlers.Handler import Handler


class OutputHandler(Handler):
    """Final handler, that outputs result."""

    def __init__(self, environment: Environment, output_stream: TextIOBase):
        super().__init__(environment)
        self.output_stream = output_stream

    def run(self, request: str) -> None:
        logging.debug("[OutputHandler]")
        if len(request) > 0:
            self.output_stream.write(request + '\n')
            self.output_stream.flush()
        self.on_finish(request)
