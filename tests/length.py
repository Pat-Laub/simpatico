import unittest
import simpatico

class TestLineLength(unittest.TestCase):
    EXPECTED = [(2, 'Line Length Error (82 characters)'),
                (3, 'Line Length Error (82 characters)'),
                (11, "Line Length Error (80 characters)"),
                (16, 'Line Length Error (81 characters)'),
                (21, 'Line Length Error (80 characters)')]
    def runTest(self):
        lines = simpatico.get_lines('tests/files/length.c')
        errors = simpatico.check_line_lengths(lines)
        self.assertItemsEqual(errors, self.EXPECTED)
