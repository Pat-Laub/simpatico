import unittest
import simpatico

class TestLineLength(unittest.TestCase):
    EXPECTED = [(3, 'Line Length Error (82 characters)'),
                (4, 'Line Length Error (82 characters)'),
                (12, "Line Length Error (80 characters)"),
                (17, 'Line Length Error (81 characters)'),
                (22, 'Line Length Error (80 characters)')]
    def runTest(self):
        lines = simpatico.get_lines('tests/files/length.c')
        errors = simpatico.check_line_lengths(lines)
        self.assertItemsEqual(errors, self.EXPECTED)

if __name__ == "__main__":
    unittest.main()
