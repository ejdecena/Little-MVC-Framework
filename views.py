#!/usr/bin/env python3
"""
Little MVC Framework.
Created by Edgard Decena.
Email: edecena@gmail.com

Views implementation.
"""
import abc


class View(abc.ABC):

    def __init__(self, data_in=None):
        """View Class Constructor.

        Args:
        data_in: data passed to the view for rendering and functionality.
        """
        self.data_in = data_in

    @property
    def data_in(self):
        return self.__data_in

    @data_in.setter
    def data_in(self, value):
        self.__data_in = value

    @abc.abstractmethod
    def show(self):
        """Method of rendering the view.

        Subclasses inheriting from View should implement this method.
        """
        pass

    def view_exception(self, message: str) -> None:
        class ViewException(Exception):
            pass
        raise ViewException(self.__class__.__name__ + ": " + message)

# +---------------------------------------------------------------------------+
# |                          YOUR VIEWS GO DOWN HERE                          |
# +---------------------------------------------------------------------------+

class TestView(View):

    def __init__(self, data_in):
        super().__init__(data_in)

    def show(self):
        print("Hello View {}".format(self.__class__.__name__))


if __name__ == "__main__":
    # Testing ...

    view = TestView(data_in=None)
    view.show()