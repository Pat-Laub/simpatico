import unittest
import simpatico

class TestNaming(unittest.TestCase):
    EXPECTED = [(2, '#define Naming Error (two)'),
                (3, '#define Naming Error (Three)'),
                (7, 'Variable Naming Error (Y)'),
                (11, 'Type Naming Error (lowercase)'),
                (18, 'Variable Naming Error (Array)'),
                (19, 'Variable Naming Error (Five)'),
                (19, 'Variable Naming Error (Six)'),
                (19, 'Variable Naming Error (Seven)'),
                (20, 'Variable Naming Error (AlsoInvalid)'),
                (21, 'Variable Naming Error (UPPERCASE)'),
                (22, 'Variable Naming Error (String)'),
                (23, 'Variable Naming Error (BigNumber)'),
                (25, 'Variable Naming Error (Function)'),
                (28, 'Variable Naming Error (Point2)')]
    def runTest(self):
        lines = simpatico.get_lines('tests/files/names.c')
        errors = simpatico.check_naming(lines)

        self.assertItemsEqual(errors, self.EXPECTED)
