import unittest
from commands.LsCommand import LsCommand
from commands.PwdCommand import PwdCommand
from commands.Command import Command
from environment.Environment import Environment
from test.CommandTest import CommandTest


class LsCommandTest(CommandTest):
    def command(self, args: list, environment: Environment) -> Command:
        return LsCommand(args, environment)

    def tests(self):
        self.assertEqual(self.execute_input([], ""), self.execute_input(["."], ""))
        cur_pwd = PwdCommand.pwd()
        self.assertEqual(self.execute_input([], ""), self.execute_input([cur_pwd], ""))
        self.assertEqual(self.execute_input(["random_unique_folder_name_that_not_exists_nvjbw47r23e"], ""),
                         "Something went wrong")
        self.assertNotEqual(self.execute_input([], ""), self.execute_input([".."], ""))


if __name__ == '__main__':
    unittest.main()
