import unittest
from subprocess import Popen, PIPE, run


class MinorMock(object):
    """
    The Mock of Minor Programme.

    Use method `input` and `assertOutput` to set the input and the output want. Use
    `assertInputMeetOutput` to check if the input is meet its output by unittest's object.
    """
    def __init__(self, test_obj):
        self.popen = Popen(['python3', 'minor.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
        self.input_text = ''
        self.output_text = ''
        self.test_obj = test_obj

    def input(self, text):
        self.input_text += text
        return self

    def assertOutput(self, text):
        self.output_text += text
        return self
    
    def assertInputMeetOutput(self):
        (out, err) = self.popen.communicate(self.input_text)
        self.test_obj.assertEqual(out, self.output_text)
        self.test_obj.assertEqual(err, '')
        self.popen.kill()


class TestFunc(unittest.TestCase):
    def test_quit(self):
        minor = MinorMock(self)
        minor.assertOutput('>>> ').input('$quit\n').assertOutput('')
        minor.assertInputMeetOutput()

    def test_print(self):
        minor = MinorMock(self)
        minor.assertOutput('>>> ').input("print, 'this'\n").assertOutput('... this\n')
        minor.assertOutput('>>> ').input('$quit\n').assertOutput('')
        minor.assertInputMeetOutput()
