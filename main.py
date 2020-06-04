import sys

from Shell import Shell
from errors.ShellError import ShellError


def main():
    try:
        shell = Shell(sys.stdin, sys.stdout)
    except ShellError as e:
        print(e.error)
        return 1
    shell.run()


if __name__ == "__main__":
    main()
