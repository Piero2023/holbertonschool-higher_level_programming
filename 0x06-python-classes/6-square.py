#!/usr/bin/python3
"""Define the square class"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        """Initilizes the data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int) \
           or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #:
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
