import os


def extend_environment(environment):
    os_vars = os.environ
    for key, value in os_vars.items():
        environment.set(key, value)
