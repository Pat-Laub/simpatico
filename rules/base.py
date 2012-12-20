from collections import namedtuple
from abc import ABCMeta, abstractmethod

Violation = namedtuple("Violation",
        ["filename", "line", "category", "description"])

class RuleChecker(object):
    """An abstract class for checking and reporting on rules."""
    __metaclass__ = ABCMeta
    _CATEGORY = NotImplemented

    def __init__(self):
        self._errors = []

    def _error(self, file_line, message):
        """Report an error on the given line number (counting lines from 1)"""
        fname, lnum = file_line
        v = Violation(fname, lnum, self._CATEGORY, message)
        self._errors.append(v)

    @abstractmethod
    def check(self, reader):
        raise NotImplementedError

    def report(self):
        return sorted(self._errors)

