from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    """Abstract handler is a node in a chain of handlers. Each handler solves a specific task and passes result
    forward."""

    def __init__(self, environment):
        self.environment = environment
        self.next = []

    @abstractmethod
    def run(self, request):
        """
        Process request and pass forward result by calling on_finish.
        :param request: request data required for processing
        Should call on_finish(result) when completed.
        """
        pass

    def add_next(self, handler):
        """Added handlers would be called after this handler."""
        self.next.append(handler)

    def on_finish(self, result):
        for handler in self.next:
            handler.run(result)
