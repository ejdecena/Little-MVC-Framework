#!/usr/bin/env python3
"""
Little MVC Framework.
Created by Edgard Decena.
Email: edecena@gmail.com

Helpers implementation.
"""

def load_object(module: str) -> callable:
    """
    Returns a method that returns an object in the module file.

    Args:
    module: module from where the object is imported.
    """
    def decorator(function: callable) -> callable:
        def wrapper(self, obj: callable, *args, **kwargs) -> object:
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

# +---------------------------------------------------------------------------+
# |                         YOUR HELPERS GO DOWN HERE                         |
# +---------------------------------------------------------------------------+


if __name__ == "__main__":
    # Testing ...

    pass