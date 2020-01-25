from ShellException import ShellException


class Environment:
    def __init__(self):
        self.data = {}
        self.code = 0
        self.exit = False

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise ShellException('No such variable %s' % key)
