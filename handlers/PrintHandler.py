import logging

from handlers.Handler import Handler


class PrintHandler(Handler):
    """Final handler, that prints result."""

    def run(self, request: str) -> None:
        logging.debug("[PrintHandler] input = " + request)
        print(request)
        self.on_finish(request)
