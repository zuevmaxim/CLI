import os

from environment.Environment import Environment


def extend_environment(environment: Environment) -> None:
    """Load variable from real environment."""
    os_vars = os.environ
    for key, value in os_vars.items():
        environment.set(key, value)
