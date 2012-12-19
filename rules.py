
__all__ = ['get_checkers']

class RuleChecker(object):
    """An abstract class for checking and reporting on rules."""
    _CATEGORY = None

    def __init__(self):
        self._errors = []

    def _error(self, linenum, message):
        """Report an error on the given line number (counting lines from 1)"""
        self._errors.append((linenum, self._CATEGORY, message))

    def check(self, reader):
        pass

    def report(self):
        return sorted(self._errors)

class LineLengthChecker(RuleChecker):
    """Check line length rules."""
    _CATEGORY = "Line Length"

    def check(self, reader):
        # Lines > 79 characters are in error.
        while not reader.end_lines():
            line = reader.next_line().rstrip('\n')
            if len(line) > 79:
                self._error(reader.linenum(),
                        "Line is {0} characters".format(len(line)))

class WhitespaceChecker(RuleChecker):
    """Checker for horizontal and vertical whitespace rules."""
    _CATEGORY = "Whitespace"

    def check(self, reader):
        # TODO: (>= ?) 2 newlines needed after a function's }
        # space before and after = &= |= ^= += -= *= /= %= <<= >>=
        # space after , ;
        assignments = {"assign", "andassign", "orassign", "xorassign",
                "plusassign", "minusassign", "starassign", "divideassign",
                "percentassign", "shiftleftassign", "shiftrightassign"}
        commas = {"comma", "semicolon"}
        whitespace = {"space", "newline"}

        while not reader.end():
            token = reader.next_tok()
            correct = True
            message = ""
            if token.type in assignments:
                correct = (reader.back(1).type in whitespace and
                        reader.forward(1).type in whitespace)
                message = "No space around {0}".format(token.value)
            elif token.type in commas:
                correct = reader.forward(1).type in whitespace
                message = "No space after {0}".format(token.value)

            if not correct:
                self._error(reader.linenum(), message)

_CHECKERS = [LineLengthChecker, WhitespaceChecker]

def get_checkers():
    return [c() for c in _CHECKERS]
