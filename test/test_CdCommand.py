import unittest
import os
import io
from commands.CdCommand import CdCommand
from commands.PwdCommand import PwdCommand
from commands.Command import Command
from environment.Environment import Environment
from test.CommandTest import CommandTest


class CdCommandTest(CommandTest):
    def command(self, args: list, environment: Environment) -> Command:
        return CdCommand(args, environment)

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
        start_pwd = self.get_pwd()
        self.run_command([], "")  # should go to $HOME
        home_pwd = self.get_pwd()
        self.assertEqual(home_pwd, os.environ.get("HOME"))
        self.run_command([".."], "")  # should go to up by 1 level TODO think about root
        parent_home_pwd = self.get_pwd()
        self.run_command([home_pwd], "")
        self.assertEqual(self.get_pwd(), home_pwd)
        self.run_command([".."], "")
        self.assertEqual(self.get_pwd(), parent_home_pwd)
        self.assertEqual(self.run_command(["random_unique_folder_name_that_not_exists_nvjbw47r"], ""),
                         "Something went wrong")
        self.run_command([start_pwd], "")


if __name__ == '__main__':
    unittest.main()
