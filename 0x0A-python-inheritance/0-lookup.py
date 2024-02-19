#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of attributes and methods available for a given object."""
    return dir(obj)
