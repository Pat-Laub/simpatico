import unittest
import simpatico

class TestIndents(unittest.TestCase):
    EXPECTED = [(6, 'Indentation error (expected 4, got 8)'),
                (10, 'Indentation error (expected 8, got 7)'),
                (16, 'Indentation error (expected 12, got 8)'),
                (20, 'Indentation error (expected 8, got 4)'),
                (23, 'Indentation error (expected 0, got 4)')]
    def runTest(self):
        lines = simpatico.get_lines('tests/files/indents.c')
        errors = simpatico.check_indents(lines)
        self.assertItemsEqual(errors, self.EXPECTED)
