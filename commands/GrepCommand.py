import io
import logging
import re
from argparse import ArgumentTypeError

from commands.ArgParser import ArgParser
from commands.Command import Command
from errors.ShellException import ShellException
from files.files_io import read_from_file_log_errors


class GrepArgsParser(ArgParser):
    """Parser for grep command arguments."""
    def __init__(self):
        super().__init__()
        self.add_argument("-i", action="store_true")
        self.add_argument("-w", action="store_true")
        self.add_argument("-A", metavar="N", type=self.check_positive, default=0)
        self.add_argument("pattern", type=str)
        self.add_argument("file", type=str, nargs="?")

    @staticmethod
    def check_positive(value):
        """Positive int type checker."""
        x = int(value)
        if x <= 0:
            raise ArgumentTypeError("%s is an invalid positive int value" % value)
        return x


class GrepCommand(Command):
    """
    Grep find matches in lines of input or file.
    Usage: grep [ARGS] PATTERN [FILE]
    Args:
        -i = ignore case
        -w = find complete-word matches
        -A N = print N lines after matched line
    if no file provided searches in input_stream
    """

    parser = GrepArgsParser()

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        logging.debug("[GrepCommand]")
        try:
            args = GrepCommand.parser.parse(self.args)
            return GrepCommand.grep(input_stream, output_stream, args.pattern, args.file, args.i, args.w, args.A)
        except ShellException as e:
            logging.error(e.error)
            return 1

    @staticmethod
    def grep(input_stream: io.StringIO,
             output_stream: io.StringIO,
             pattern: str,
             file: str = None,
             ignore_case: bool = False,
             words_only: bool = False,
             add_lines: int = 0) -> int:
        if file is None:
            text = input_stream.getvalue()
        else:
            stream = io.StringIO()
            if not read_from_file_log_errors(file, stream, "grep"):
                return 1
            text = stream.getvalue()
        if words_only:
            pattern = "\\b%s\\b" % pattern

        def contains_pattern(line: str) -> bool:
            return (re.search(pattern, line, re.IGNORECASE)
                    if ignore_case else re.search(pattern, line)) is not None

        lines = text.splitlines(keepends=True)
        matched_ids = [i for i, line in enumerate(lines) if contains_pattern(line)]
        matched = set()
        for i in matched_ids:
            matched.add((i, lines[i]))
            for j in range(i + 1, min(len(lines), i + 1 + add_lines)):
                matched.add((j, lines[j]))
        for _, line in sorted(matched):
            output_stream.write(line)
        return 0
