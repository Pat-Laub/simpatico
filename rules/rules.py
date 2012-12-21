from base import RuleChecker

__all__ = ['NamesChecker', 'BracesChecker', 'IndentationChecker',
        'WhitespaceChecker', 'LineLengthChecker', 'OverallChecker']

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
                self._error(reader.file_line(), "Invalid variable " + token.value)

class BracesChecker(RuleChecker):
    _CATEGORY = "Braces"

    def check(self, reader):
        # TODO (braces checking):
        # braces around control statements (except case/default)
        # { on same line as control statement followed by newline
        # } at the start of a new line (including for function definitions)
        # else / else if / do-while have stuff after the }
        # { ... } on the same line counts as one violation, not 2
        # mistakes in } else { and } else if { count as one violation, not 2
        
        # keep track of:
        # - whether we are in a control statement (to look for the { in the right spot)
        # - control structure, array, struct, etc nesting (as a stack)
        # - violations that shouldn't be double-counted
        pass

class IndentationChecker(RuleChecker):
    _CATEGORY = "Indentation"
    _INDENT = 4

    def check(self, reader):
        # TODO: (indentation checking)
        # start of body after control structure: +1 indent
        # { after function definition: +1 indent
        # newline in a statement: +2 indent on first encounter
        # end of code block: -1 indent
        #   -> } when code block started with {
        #   -> end of statement when code block didn't start with {
        #   -> `case` or `default` when code block is a case/default
        #   -> end of switch within case/default: apply twice (-2)
        # multi-line statement finishes: -2 indent

        # Keep track of:
        # - control structure nesting (as a stack)
        # - whether we are in a control statement (to look for the \n at the end)
        # - whether we are in a statement (so we can detect \n in a statement)
        # - whether we are in a multi-line statement (so we only count it once)

        # a non-control statement ends with a ;
        # the end of a control statement depends on the statement.
        pass


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
        whitespace = {"space", "newline", "eof"}

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
                self._error(reader.file_line(), message)

class LineLengthChecker(RuleChecker):
    """Checker for line length rules."""
    _CATEGORY = "Line Length"

    def check(self, reader):
        # Lines > 79 characters are in error.
        while not reader.end_lines():
            line = reader.next_line().rstrip('\n')
            if len(line) > 79:
                self._error(reader.file_line(),
                        "Line is {0} characters".format(len(line)))

class OverallChecker(RuleChecker):
    _CATEGORY = "Overall"

    def check(self, reader):
        # TODO function length (if strict)
        while not reader.end():
            token = reader.next_tok()
            if token.type == 'goto':
                self._error(reader.file_line(), 'goto')

