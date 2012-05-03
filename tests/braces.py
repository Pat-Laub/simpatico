import unittest
import simpatico

class TestBraces(unittest.TestCase):
    def test_good(self):
        lines = simpatico.get_lines('tests/files/good_braces.c')
        errors = simpatico.check_braces(lines)
        self.assertEqual(errors, [])

    def test_bad(self):
        # Line numbers could be arguably different for errors that
        # span multiple lines
        expected = [(9, "Braces Error (spacing)"),
                    (14, "Braces Error (spacing)"),
                    (19, "Braces Error (spacing)"),
                    (22, "Braces Error (else placement)"),
                    (26, "Braces Error (else placement)"),
                    (36, "Braces Error (spacing)"),
                    (39, "Braces Error (spacing)"),
                    (42, "Braces Error (spacing)"),
                    (51, "Braces Error (missing braces)"),
                    (53, "Braces Error (missing braces)"),
                    (55, "Braces Error (missing braces)"),
                    (62, "Braces Error (spacing)"),
                    (65, "Braces Error (spacing)"),
                    (67, "Braces Error (spacing)"),
                    (77, "Braces Error (spacing)"),
                    (86, "Braces Error (else placement)"),
                    (89, "Braces Error (else placement)")]
        lines = simpatico.get_lines('tests/files/bad_braces.c')
        errors = simpatico.check_braces(lines)
        self.assertItemsEqual(errors, expected)

if __name__ == "__main__":
    unittest.main()
