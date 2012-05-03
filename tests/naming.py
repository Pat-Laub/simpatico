import unittest
import simpatico

class TestNaming(unittest.TestCase):
    def test_1(self):
        expected = [(2, '#define Naming Error (two)'),
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

        lines = simpatico.get_lines('tests/files/names.c')
        errors = simpatico.check_naming(lines)
        self.assertItemsEqual(errors, expected)

    def test_good(self):
        lines = simpatico.get_lines('tests/files/good_naming.c')
        errors = simpatico.check_naming(lines)
        self.assertEqual(errors, [])

    def test_bad(self):
        expected = [(6, "Type Naming Error (struct bobStruct)"),
                    (12, "Type Naming Error (badStruct)"),
                    (14, "Variable Naming Error (A)"),
                    (15, "Variable Naming Error (a_char)"),
                    (23, "Variable Naming Error (BobStruct)")]
        lines = simpatico.get_lines('tests/files/bad_naming.c')
        errors = simpatico.check_naming(lines)
        self.assertItemsEqual(errors, expected)

class TestFunctionNames(unittest.TestCase):
    def test_good(self):
        lines = simpatico.get_lines('tests/files/good_naming.c')
        errors = simpatico.check_function_lengths_names(lines)
        self.assertEqual(errors, [])

    def test_bad(self):
        expected = [(17, "Function Naming Error (FunctionBad contains uppercase)"),
                    (20, "Function Naming Error (functionStuff contains uppercase)")]
        lines = simpatico.get_lines('tests/files/bad_naming.c')
        errors = simpatico.check_function_lengths_names(lines)
        self.assertItemsEqual(errors, expected)
