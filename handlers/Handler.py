from abc import ABCMeta, abstractmethod

from environment.Environment import Environment


class Handler(metaclass=ABCMeta):
    """Abstract handler is a node in a chain of handlers. Each handler solves a specific task and passes result
    forward."""

    def __init__(self, environment: Environment):
        self.environment = environment
        self.next = []

    @abstractmethod
    def run(self, request) -> None:
        """
        Process request and pass forward result by calling on_finish.
        :param request: request data required for processing
        Should call on_finish(result) when completed.
        """
        pass

    def add_next(self, handler) -> None:
        """Added handlers would be called after this handler."""
        self.next.append(handler)

    def on_finish(self, result) -> None:
        """Should be called after finishing processing."""
        for handler in self.next:
            handler.run(result)
