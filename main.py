#!/usr/bin/env python3
"""
Little MVC Framework.
Created by Edgard Decena.
Email: edecena@gmail.com

Main implementation.
"""
from controllers import InitController


if __name__ == "__main__":
    controller = InitController()
    controller.run()