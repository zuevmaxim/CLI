import io
import unittest

from parameterized import parameterized

from Shell import Shell
from files.files_io import os_file_path

file1 = os_file_path('test', 'test_file_1.txt')


class ShellTest(unittest.TestCase):
    @parameterized.expand([
        ('exit', 'exit\n', ''),
        ('echo', 'echo "Hello world!"\nexit\n', 'Hello world!\n'),
        ('substitution', 'x=42\necho "\'$x\'"\nexit\n', "'42'\n"),
        ('pipe', 'echo hello | wc\nexit\n', 'newlines = 1;  words = 1; bytes = 5\n'),
        ('wc', 'wc %s\nexit\n' % file1, 'newlines = 1;  words = 2; bytes = 12 %s\n' % file1),
        ('cat', 'cat %s\nexit\n' % file1, 'Hello world!\n'),
        ('wrong', '8 = 3\nexit\n', ''),
        ('substitution magic', 'x = ex\ny = it\necho $x$y\n$x$y\n', 'exit\n'),
    ])
    def test(self, _, input_string, output_string):
        input_stream = io.StringIO(input_string)
        output_stream = io.StringIO()

        # noinspection PyTypeChecker
        shell = Shell(input_stream, output_stream)

        shell.run()

        self.assertEqual(output_string, output_stream.getvalue())


if __name__ == '__main__':
    unittest.main()
