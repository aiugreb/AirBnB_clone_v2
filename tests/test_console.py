#!/usr/bin/python3
"""Console test module"""
import unittest
import console


class test_Console(unittest.TestCase):
    """TEst test"""

    def test_documentation(self):
        """Test test"""
        self.assertIsNotNone(console.__doc__)
