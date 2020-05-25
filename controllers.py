#!/usr/bin/env python3
"""
Little MVC Framework.

Controllers implementation.
"""
import abc
import config
import helpers


class Controller(abc.ABC):

    def __init__(self):
        pass

    @helpers.load_object("models")
    def load_model(self, model, *args, **kwargs):
        pass

    @helpers.load_object("views")
    def load_view(self, view, *args, **kwargs):
        pass

    @helpers.load_object("controllers")
    def load_controller(self, controller, *args, **kwargs):
        pass

    def controller_exception(self, message):
        class ControllerException(Exception):
            pass
        raise ControllerException(self.__class__.__name__ + ": " + message)

    @abc.abstractmethod
    def run(self):
        pass


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