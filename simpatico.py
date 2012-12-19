#!/usr/bin/env python

import file_reader
import rules

PRINT_FORMAT = "{fname}:{line}: [{category}] {desc}"

def report(errors):
    for e in errors:
        print PRINT_FORMAT.format(fname=e.filename, line=e.line,
                category=e.category.upper(), desc=e.description)

    print
    print "Total number of violations:", len(errors)

def main(args):
    checkers = rules.get_checkers()
    errors = []
    for fname in args.files:
        reader = file_reader.FileReader(fname)
        for c in checkers:
            reader.reset()
            c.check(reader)

    for c in checkers:
        errors.extend(c.report())

    errors.sort()
    report(errors)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    main(args)

'''
INDENT = 4
def check_indents(tokens):
    """Check the indentation of a file.

    """
    nesting = [] # Keep track of what we are nested in
    controls = 
    while not tokens.end():
        t = tokens.next()
        if t.type
'''
