import inspect
import os.path


def readlines(filename: str):
    """Reads lines from a filename relative to the caller's working directory"""
    stack = inspect.stack()
    file = os.path.join(
        os.path.dirname(stack[1].filename),
        filename
    )

    with open(file) as f:
        return f.readlines()
