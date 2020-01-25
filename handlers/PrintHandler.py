import logging

from handlers.Handler import Handler


class PrintHandler(Handler):
    def run(self, request):
        logging.debug("[PrintHandler] input = " + request)
        print(request)
        self.on_finish(request)
