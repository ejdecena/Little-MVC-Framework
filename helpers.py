#!/usr/bin/env python3
"""
Little MVC Framework.

Helpers implementation.
"""

def load_object(module):
    """
    Returns a method that returns an object in the module file.

    Args:
    module: module from where the object is imported.
    """
    def decorator(function):
        def wrapper(self, obj, *args, **kwargs):
            try:
                mod = __import__(module)
            except ImportError:
                exit("Error: \"{}\" module does not exist.".format(module))
            try:
                return eval("mod.{}(*args, **kwargs)".format(obj))
            except AttributeError:
                exit("Error: \"{}\" class does not exist in {}."\
                     .format(obj, module))
        return wrapper
    return decorator


class Singleton:
    """Singleton class decorator."""

    def __init__(self, cls):
        self.__cls = cls
        self.__obj = None

    def __call__(self, *args, **kwargs):
        if not self.__obj:
            self.__obj = self.__cls(*args, **kwargs)
        return self.__obj


if __name__ == "__main__":
    # Testing ...

    pass