#!/usr/bin/env python3
"""
Little MVC Framework.

Views implementation.
"""
import abc


class View(abc.ABC):

    def __init__(self, data_in):
        self.data_in = data_in

    @property
    def data_in(self):
        return self.__data_in

    @data_in.setter
    def data_in(self, value):
        self.__data_in = value

    @abc.abstractmethod
    def show(self):
        pass

    def view_exception(self, message):
        class ViewException(Exception):
            pass
        raise ViewException(self.__class__.__name__ + ": " + message)


class TestView(View):

    def __init__(self, data_in):
        super().__init__(data_in)

    def show(self):
        print("Hello View {}".format(self.__class__.__name__))


if __name__ == "__main__":
    # Testing ...

    view = TestView(data_in=None)
    view.show()