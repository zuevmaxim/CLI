import sys

from Shell import Shell
from ShellException import ShellException


def enable_debug_logging() -> None:
    import logging
    logging.basicConfig(level=logging.DEBUG)


# enable this for logging DEBUG messages
# enable_debug_logging()


def main():
    shell = Shell()
    while not shell.is_exit():
        try:
            input_string = sys.stdin.readline()[:-1]
            shell.execute(input_string)
        except ShellException as e:
            print(e.error)


if __name__ == "__main__":
    main()
