
__all__ = ['get_checkers']

class RuleChecker(object):
    """An abstract class for checking and reporting on rules."""
    _CATEGORY = NotImplemented

    def __init__(self):
        self._errors = []

    def _error(self, linenum, message):
        """Report an error on the given line number (counting lines from 1)"""
        self._errors.append((linenum, self._CATEGORY, message))

    def check(self, reader):
        raise NotImplementedError

    def report(self):
        return sorted(self._errors)

class NamesChecker(RuleChecker):
    """Checker for naming conventions."""
    _CATEGORY = "Naming"

    def _check_variable(self, name):
        # variable names are in camelCase
        return name[0].islower() and '_' not in name

    def _check_define(self, name):
        # #defines are in ALL_CAPS
        return name.isupper() or name in {'true', 'false'}

    def _check_function(self, name):
        # function names are in all_lowercase
        return name.islower()

    def _check_type(self, name):
        # type names are in UpperCamelCase
        return name[0].isupper() and '_' not in name

    def check(self, reader):
        # TODO: know what kind of identifier each identifier is.
        while not reader.end():
            token = reader.next_tok()
            if token.type != 'identifier':
                continue
            
            if not self._check_variable(token.value):
                self._error(reader.linenum(), "Invalid variable " + token.value)

class BracesChecker(RuleChecker):
    _CATEGORY = "Braces"
    # TODO

class IndentationChecker(RuleChecker):
    _CATEGORY = "Indentation"
    # TODO

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

class LineLengthChecker(RuleChecker):
    """Checker for line length rules."""
    _CATEGORY = "Line Length"

    def check(self, reader):
        # Lines > 79 characters are in error.
        while not reader.end_lines():
            line = reader.next_line().rstrip('\n')
            if len(line) > 79:
                self._error(reader.linenum(),
                        "Line is {0} characters".format(len(line)))

class OverallChecker(RuleChecker):
    _CATEGORY = "Overall"

    def check(self, reader):
        # TODO function length (if strict)
        while not reader.end():
            token = reader.next_tok()
            if token.type == 'goto':
                self._error(reader.linenum(), 'goto')

_CHECKERS = [NamesChecker, #BracesChecker, IndentationChecker,
        WhitespaceChecker, LineLengthChecker, OverallChecker]

def get_checkers():
    return [c() for c in _CHECKERS]
