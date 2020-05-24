#!/usr/bin/env python3
"""
Little MVC Framework.

Main implementation.
"""
from controllers import InitController


if __name__ == "__main__":
    controller = InitController()
    controller.run()