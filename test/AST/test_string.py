import unittest

from src.AST import string

class TestString(unittest.TestCase):
    def test_string_normal_1(self):
        str_ = "\" \""
        len_ = len(str_)
        self.assertEqual(
            string(str_, 0),
            (" ", len_)
        )

    def test_string_escape_1(self):
        str_ = "'\\''  "
        len_ = len(str_) - 2 # 2: the whitespace's len at end
        self.assertEqual(
            string(str_, 0),
            ("'", len_)
        )

