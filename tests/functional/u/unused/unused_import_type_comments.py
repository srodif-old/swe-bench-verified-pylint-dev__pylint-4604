"""Test for type comments and unused imports"""
# pylint: disable=missing-docstring

import abc
from abc import ABC
import typing
from typing import List, Dict

# Test basic type comments
X = ...  # type: abc.ABC
Y = ...  # type: ABC

# Test complex type comments with nested references  
Z = {}  # type: Dict[str, abc.ABC]
W = []  # type: List[ABC]

# Test fully qualified typing module usage
V = None  # type: typing.Optional[abc.ABC]