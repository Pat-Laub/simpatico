import unittest
import simpatico

class TestNaming(unittest.TestCase):
    EXPECTED = [(2, '#define Naming Error (two)'),
                (3, '#define Naming Error (Three)'),
                (7, 'Variable Naming Error (Y)'),
                (11, 'Type Naming Error (lowercase)'),
                (20, 'Variable Naming Error (Invalid)'),
                (21, 'Variable Naming Error (AlsoInvalid)'),
                (22, 'Variable Naming Error (UPPERCASE)'),
                (23, 'Variable Naming Error (String)'),
                (24, 'Variable Naming Error (BigNumber)'),
                (27, 'Variable Naming Error (Point2)')]
    def runTest(self):
        lines = simpatico.get_lines('tests/files/names.c')
        errors = simpatico.check_naming(lines)

        self.assertItemsEqual(errors, self.EXPECTED)
