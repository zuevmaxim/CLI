from handlers.PrintHandler import PrintHandler
from handlers.SubstitutionHandler import SubstitutionHandler


class HandlersNet:
    """A net contains all handlers attached in correct order."""

    def __init__(self, environment):
        self.substitution_handler = SubstitutionHandler(environment)
        self.print_handler = PrintHandler(environment)

        self.init_net()

    def init_net(self):
        self.substitution_handler.add_next(self.print_handler)

    def run(self, input_string):
        """Start processing of input."""
        self.substitution_handler.run(input_string)
