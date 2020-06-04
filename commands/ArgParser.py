from argparse import ArgumentParser, Namespace

from errors.ShellException import ShellException


class ArgParser(ArgumentParser):
    """Commands argument parser."""
    def __init__(self):
        super().__init__(add_help=False)

    def error(self, message):
        raise ShellException(message)

    def parse(self, arg_list: list) -> Namespace:
        return self.parse_args(arg_list)
