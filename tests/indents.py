import unittest
import simpatico

class TestIndents(unittest.TestCase):
    EXPECTED = [(3, 'Indentation error (expected 0, got 4)'),
                (7, 'Indentation error (expected 4, got 8)'),
                (11, 'Indentation error (expected 8, got 7)'),
                (17, 'Indentation error (expected 12, got 8)'),
                (21, 'Indentation error (expected 8, got 4)'),
                (24, 'Indentation error (expected 0, got 4)')]
    def runTest(self):
        lines = simpatico.get_lines('tests/files/indents.c')
        errors = simpatico.check_indents(lines)
        self.assertItemsEqual(errors, self.EXPECTED)
