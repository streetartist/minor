import unittest

# add src folder into `sys.path` to import it easily
import sys
from pathlib import Path
SRC_FOLDER = str(Path(__file__).parent.parent.parent)
sys.path.append(SRC_FOLDER)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromNames([
        'print.TestPrint',
    ]))
    return suite

if __name__ == "__main__":
    # use `make test` to run test
    runner = unittest.TextTestRunner()
    runner.run(suite())