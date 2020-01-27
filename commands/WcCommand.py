import io
import logging

from commands.Command import Command
from files.files_io import read_from_file_log_errors


class WcStatistics:
    """Contains statistics: lines, words, bytes."""

    def __init__(self, newlines=0, words=0, byte=0):
        self.newlines = newlines
        self.words = words
        self.bytes = byte

    def __add__(self, others):
        return WcStatistics(self.newlines + others.newlines,
                            self.words + others.words,
                            self.bytes + others.bytes)

    def __str__(self):
        return "newlines = %d;  words = %d; bytes = %d" % (self.newlines, self.words, self.bytes)

    def __eq__(self, other):
        return self.newlines == other.newlines and \
               self.words == other.words and \
               self.bytes == other.bytes


class WcCommand(Command):
    """Wc command calculates files or input statistics: lines, words, bytes."""

    def execute(self, input_stream: io.StringIO, output_stream: io.StringIO) -> int:
        logging.debug("[WcCommand] args = %s", str(self.args))
        if len(self.args) > 0:
            statistics = []
            success = True
            for file_name in self.args:
                content = io.StringIO()
                current_success = read_from_file_log_errors(file_name, content, 'wc')
                success &= current_success
                if current_success:
                    stats = self.calculate_statistics(content.getvalue())
                    statistics.append((stats, file_name))
            if len(self.args) > 1:
                stats_sum = sum(map(lambda p: p[0], statistics), WcStatistics())
                statistics.append((stats_sum, 'total'))

            def stats_and_file_to_string(pair: (WcStatistics, str)) -> str:
                (stat, name) = pair
                return "%s %s" % (str(stat), name)

            output_stream.write('\n'.join(map(stats_and_file_to_string, statistics)))
            return 0 if success else 1
        else:
            stats = self.calculate_statistics(input_stream.getvalue())
            output_stream.write(str(stats))
            return 0

    @staticmethod
    def calculate_statistics(string: str) -> WcStatistics:
        """Calculate input_string statistics: lines, words, bytes."""
        return WcStatistics(len(string.splitlines()), len(string.split()), len(string.encode()))
