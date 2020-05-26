#!/usr/bin/env python3
"""
Little MVC Framework.
Created by Edgard Decena.
Email: edecena@gmail.com

Helpers implementation.
"""
import sqlite3
import typing


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
    """Singleton class decorator.
    
    Use:
        @Singleton
        class Test:
            def __init__(self, text):
                self.text = text

        a = Test("Hello")
        b = Test("World")

        print("id(a):", id(a), "id(b):", id(b), "Diff:", id(a)-id(b))
    """
    def __init__(self, cls):
        self.__cls = cls
        self.__obj = None

    def __call__(self, *args, **kwargs):
        if not self.__obj:
            self.__obj = self.__cls(*args, **kwargs)
        return self.__obj


def execute_db_query(db_filename: str, query: str, parameters: tuple=()) \
                    -> typing.Any:
    """Execute a query in a SQLite-type database.
    
    Args:
        db_filename: string with the name of the SQLite file.
        query: strig with the SQL query.
        parameters: tupla with the query parameters.

    Returns:
        a tuple of data in case of SELECT queries or an integer with the number of affected rows.

    Use:
        query      = "INSERT INTO contacts VALUES (NULL, ?, ?);"
        parameters = (namefield, numfield)
        result     = execute_db_query(query, parameters)
    """
    with sqlite3.connect(db_filename) as conn:
        cursor       = conn.cursor()
        query_result = cursor.execute(query, parameters)
        conn.commit()
    return query_result

# +---------------------------------------------------------------------------+
# |                         YOUR HELPERS GO DOWN HERE                         |
# +---------------------------------------------------------------------------+


if __name__ == "__main__":
    # Testing ...

    pass