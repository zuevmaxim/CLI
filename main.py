import sys

from Shell import Shell
from errors.ShellError import ShellError
from errors.ShellException import ShellException


def enable_debug_logging() -> None:
    import logging
    logging.basicConfig(level=logging.DEBUG)


# enable this for logging DEBUG messages
# enable_debug_logging()


def main():
    try:
        shell = Shell()
    except ShellError as e:
        print(e.error)
        return 1
    while not shell.is_exit():
        try:
            input_string = sys.stdin.readline()[:-1]
            shell.execute(input_string)
        except ShellException as e:
            print(e.error)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
