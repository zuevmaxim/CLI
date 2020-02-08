import io
import unittest

from parameterized import parameterized

from Shell import Shell


class ShellTest(unittest.TestCase):
    @parameterized.expand([
        ('exit', 'exit\n', ''),
        ('echo', 'echo "Hello world!"\nexit\n', 'Hello world!\n'),
        ('substitution', 'x=42\necho "\'$x\'"\nexit\n', "'42'\n"),
        ('pipe', 'echo hello | wc\nexit\n', 'newlines = 1;  words = 1; bytes = 5\n'),
        ('wc', 'wc test/test_file_1.txt\nexit\n', 'newlines = 1;  words = 2; bytes = 12 test/test_file_1.txt\n'),
        ('cat', 'cat test/test_file_1.txt\nexit\n', 'Hello world!\n'),
        ('grep', 'grep other test/test_file_2.txt\nexit\n', 'Some other string.\n'),
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
