import unittest

from src import run

class TestPrint(unittest.TestCase):
    def test_print_1(self):
        """
        I hope it can work like this:
        >>> print, "this is the string..."
        ... this is the string...
        """
        self.assertEqual(
            run('print, "this is the string..."'),
            "this is the string..."
        )
        # the white space do not make the result different
        self.assertEqual(
            run('     print   ,     "this is the string..."       '),
            "this is the string..."
        )
        # but endiff result if in string:
        self.assertEqual(
            run('print, "this    is the string..."'),
            "this     is the string..."
        )

    def test_print_2(self):
        """
        There is two way to show the string: "xxx" and 'xxx', like python.
        """
        self.assertEqual(
            run('''print, "this is the 'string'!" '''),
            "this is the 'string'!"
        )
        self.assertEqual(
            run('''print, 'this is the "string"!' '''),
            "this is the 'string'!"
        )

    def test_print_3(self):
        """
        It can escape some characters: \" or \' and \\
        """
        self.assertEqual(
            run(r'print, "\"\""'),
            '""'
        )
        self.assertEqual(
            run(r"print, '\'\''"),
            "''"
        )
        self.assertEqual(
            run(r"print, '\\'"),
            "\\"
        )

    def test_print_4(self):
        # if the character is after `\` sign, just output what it is.
        self.assertEqual(
            run("print, '\a\b\c'"),
            'abc'
        )
