from handlers.PrintHandler import PrintHandler
from handlers.SubstitutionHandler import SubstitutionHandler


class HandlersNet:
    def __init__(self, environment):
        self.substitution_handler = SubstitutionHandler(environment)
        self.print_handler = PrintHandler(environment)

        self.init_net()

    def init_net(self):
        self.substitution_handler.add_next(self.print_handler)

    def run(self, string):
        self.substitution_handler.run(string)
