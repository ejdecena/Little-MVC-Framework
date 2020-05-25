# Little MVC Framework.

*Little MVC Framework* is a small framework for software development. The framework is built following the *Model-View-Controller* architecture [(MVC)](https://en.wikipedia.org/wiki/Model-view-controller-view-controller).

<img src="https://img.shields.io/badge/Python-3.5-blue" />

## Developer.

* Edgard Decena, edecena@gmail.com

## Description and Settings.

The framework is based on the *Model-View-Controller* design pattern. It is structured in six files: `controllers.py`, `models.py` and `views.py`, where the controllers, models and views classes are placed, respectively. In the `helpers.py` file are the framework's complementary functions and classes. The `config.py` file will have the constants and parameter declarations, and finally the `main.py` file will be the framework executor file.

### The Models.

The models of the development are located in the file `models.py`. The first adjustment that has to be done before starting the development is to set the *origin* and *access* to the data source, this is done in the `Model` class implemented in the `models.py` file. The following *methods* in the class `Model` **should be implemented** according to the data source to establish the *origin* and *access* to the data:

1. `def __init__(self)`: Constructor method of the `Model` class.
1. `def connect(self)`: Method of connecting to the data source.
1. `def execute(self, command)`: Method that executes a instruction in the data source.
1. `def disconnect(self)`: Method of disconnecting to the data source.

All models should be placed in the `models.py` file, implemented in a single class inherited from the base `Model` class. Each model will have at its disposal the `connect()` `execute()`, `disconnect()` and `model_exception()` methods inherited from the base `Model` class.

### The Views.

All the views should be placed in the `views.py` file, implemented in a single class and inherited from the base `View` class. Each view will have to implement the `show()` method to show the view, and will have at its disposal the `view_exception()` method inherited from the base `View` class.

### The Controllers.

All the controllers of the development must be located in the file `controllers.py`, will be implemented in a single class and inherit from the base class `Controller`. Each controller must implement the `run()` method to execute it. Each controller will have at its disposal the `load_model()`, `load_view()`, `load_controller()`, `run()` and `controller_exception()` methods inherited from the base `Controller` class.

## Use.

1. Set the origin and access to the development data in the `Model` class implemented in the `models.py` file.
2. Create the models, controllers and views in the `controllers.py`, `models.py` and `views.py` files, respectively.
1. Run the `main.py` and see the framework display.

## Contributions.

Any doubt or problem about the framework should be reported by opening an [**issue**](https://github.com/ejdecena/Little-MVC-Framework/issues).