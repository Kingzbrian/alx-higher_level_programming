#!/usr/bin/python3
"""
This module implements  a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Method for comparing object classes
    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.
    Return:
        True if obj isinstance of a_class/ class that inherits from it.
        otherwise False
    """
    if isinstance(obj, a_class) and obj.__class__ is not a_class:
        return True
    return False
