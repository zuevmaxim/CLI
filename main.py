import sys

from Shell import Shell
from ShellException import ShellException


def main():
    shell = Shell()
    while True:
        try:
            input_string = sys.stdin.readline()[:-1]
            shell.execute(input_string)
        except ShellException as e:
            print(e.error)


if __name__ == "__main__":
    main()
