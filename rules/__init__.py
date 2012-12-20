"""Implementation of rule checking."""

from rules import *

__all__ = ['get_checkers']

_CHECKERS = [NamesChecker, #BracesChecker, IndentationChecker,
        WhitespaceChecker, LineLengthChecker, OverallChecker]

def get_checkers():
    return [c() for c in _CHECKERS]
