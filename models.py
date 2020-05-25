#!/usr/bin/env python3
"""
Little MVC Framework.
Created by Edgard Decena.
Email: edecena@gmail.com

Models implementation.
"""
import abc


class Model(abc.ABC):

    def __init__(self):
        self.connect()

    def connect(self):
        # raise NotImplementedError
        pass

    def execute(self, command):
        # raise NotImplementedError
        pass

    def disconnect(self):
        # raise NotImplementedError
        pass

    def model_exception(self, message: str) -> None:
        class ModelException(Exception):
            pass
        raise ModelException(self.__class__.__name__ + ": " + message)

# +---------------------------------------------------------------------------+
# |                         YOUR MODELS GO DOWN HERE                          |
# +---------------------------------------------------------------------------+

class TestModel(Model):

    def __init__(self):
        super().__init__()

    def test(self):
        return "Hello TestModel."


if __name__ == "__main__":
    # Testing ...

    model = TestModel()
    print(model.test())