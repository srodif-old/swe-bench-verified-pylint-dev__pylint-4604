"""Test for type comments and unused imports"""
# pylint: disable=missing-docstring

import abc
from abc import ABC

X = ...  # type: abc.ABC
Y = ...  # type: ABC