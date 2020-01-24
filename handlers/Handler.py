from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    def __init__(self, environment):
        self.environment = environment
        self.next = []

    @abstractmethod
    def run(self, request):
        pass

    def add_next(self, handler):
        self.next.append(handler)

    def on_finish(self, result):
        for handler in self.next:
            handler.run(result)
