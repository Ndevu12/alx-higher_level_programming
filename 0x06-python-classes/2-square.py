#!/usr/bin/python3
"""a class Square that defines a square"""

class Square:
    """Inside the square class"""

    def __init__(self, size=0):
        """quare class defined by geometric shap"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

