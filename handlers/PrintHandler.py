from handlers.Handler import Handler


class PrintHandler(Handler):
    def run(self, request):
        print(request)
        self.on_finish(request)
