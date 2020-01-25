import logging

from handlers.Handler import Handler


class PrintHandler(Handler):
    """Final handler, that prints result."""

    def run(self, request: str) -> None:
        logging.debug("[PrintHandler]")
        if len(request) > 0:
            print(request)
        self.on_finish(request)
