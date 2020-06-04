import os
import unittest
import io
from commands.CdCommand import CdCommand
from commands.Command import Command
from commands.PwdCommand import PwdCommand
from environment.Environment import Environment
from test.CommandTest import CommandTest


class CdCommandTest(CommandTest):
    def command(self, args: list, environment: Environment) -> Command:
        return CdCommand(args, environment)

    @unittest.skip("cannot be run in parallel with other tests")
    def tests(self):
        def pwd():
            return PwdCommand.pwd()

        start_pwd = pwd()
        self.execute_input([], "")  # should go to $HOME
        home_pwd = pwd()
        self.assertEqual(home_pwd, os.environ.get("HOME"))
        self.execute_input([".."], "")  # should go to up by 1 level
        parent_home_pwd = pwd()
        self.execute_input([home_pwd], "")
        self.assertEqual(pwd(), home_pwd)
        self.execute_input([".."], "")
        self.assertEqual(pwd(), parent_home_pwd)
        self.assertEqual(self.execute_input(["random_unique_folder_name_that_not_exists_nvjbw47r"], ""),
                         "Directory not found!")
        self.execute_input([start_pwd], "")


if __name__ == '__main__':
    unittest.main()
