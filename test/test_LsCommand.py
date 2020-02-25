import unittest
import os
import io
from commands.LsCommand import LsCommand
from commands.PwdCommand import PwdCommand
from commands.Command import Command
from environment.Environment import Environment
from test.CommandTest import CommandTest


class LsCommandTest(CommandTest):
    def command(self, args: list, environment: Environment) -> Command:
        return LsCommand(args, environment)

    def get_pwd(self):
        pwd = PwdCommand([], os.environ)
        in_str = io.StringIO()
        out_str = io.StringIO()
        pwd.execute(in_str, out_str)
        return out_str.getvalue()

    def run_command(self, args, input_string):
        command = self.command(args, os.environ)
        input_stream = io.StringIO()
        input_stream.write(input_string)
        output_stream = io.StringIO()
        command.execute(input_stream, output_stream)
        return output_stream.getvalue()

    def tests(self):
        self.assertEqual(self.run_command([], ""), self.run_command(["."], ""))
        cur_pwd = self.get_pwd()
        self.assertEqual(self.run_command([], ""), self.run_command([cur_pwd], ""))
        self.assertEqual(self.run_command(["random_unique_folder_name_that_not_exists_nvjbw47r23e"], ""),
                         "Something went wrong")
        self.assertNotEqual(self.run_command([], ""), self.run_command([".."],
                                                                       ""))  # Есть шанс того, что этот тест упадёт, но он очень специфичен. Простите за флакающие тесты. Я просто не понимаю, как ещё тестить вот это вот с помощью вот этого вот


if __name__ == '__main__':
    unittest.main()
