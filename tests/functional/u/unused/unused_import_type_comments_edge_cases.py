"""Test edge cases for type comments and unused imports"""
# pylint: disable=missing-docstring

import collections
import sys

# Valid type comment
data = {}  # type: collections.defaultdict

# Invalid type comment (should be ignored, but import should still be flagged if unused)
bad_data = 42  # type: invalid syntax here!!!

# Type comment that doesn't reference imports 
other_data = []  # type: list

# Use sys to avoid unused import
print(sys.version)