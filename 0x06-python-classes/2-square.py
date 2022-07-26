#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a Square."""

    def __init__(self, size=0):
        """
        Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size






let binaryN = (N  >> 0).toString(2);
let maxGap = 0;

for (let i=0; i < binaryN.length; i==){
    for 
}