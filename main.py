import sys

from Interpreter import Interpreter
from ShellException import ShellException


def main():
    interpreter = Interpreter()
    while True:
        try:
            input_string = sys.stdin.readline()[:-1]
            interpreter.interpret(input_string)
        except ShellException as e:
            print(e.error)


if __name__ == "__main__":
    main()
