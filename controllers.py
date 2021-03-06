#!/usr/bin/env python3
"""
Little MVC Framework.
Created by Edgard Decena.
Email: edecena@gmail.com

Controllers implementation.
"""
import abc
import config
import helpers


class Controller(abc.ABC):

    def __init__(self):
        pass

    @helpers.load_object("models")
    def load_model(self, model: str, *args, **kwargs) -> object:
        pass

    @helpers.load_object("views")
    def load_view(self, view: str, *args, **kwargs) -> object:
        pass

    @helpers.load_object("controllers")
    def load_controller(self, controller: str, *args, **kwargs) -> object:
        pass

    def controller_exception(self, message: str) -> None:
        class ControllerException(Exception):
            pass
        raise ControllerException(self.__class__.__name__ + ": " + message)

    @abc.abstractmethod
    def run(self):
        pass

# +---------------------------------------------------------------------------+
# |                         YOUR CONTROLLERS GO DOWN HERE                     |
# +---------------------------------------------------------------------------+

class InitController(Controller):

    def __init__(self):
        super().__init__()

    def run(self):
        model = self.load_model("TestModel")
        print(model.test())

        controller = self.load_controller("TestController")
        print(controller.run())

        view = self.load_view("TestView", data_in=None)
        view.show()


class TestController(Controller):
    def __init__(self):
        super().__init__()

    def run(self):
        return "Hello TestController."


if __name__ == "__main__":
    # Testing ...

    controller = InitController()
    controller.run()