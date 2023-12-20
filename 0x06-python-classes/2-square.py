#!/usr/bin/python3
"""
defines a class square
"""
class Square:
    """Represents a square"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

