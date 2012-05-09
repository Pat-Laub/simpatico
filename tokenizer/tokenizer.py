import subprocess
import re

def tokenize(filename):
    """Read and tokenise a C file, and return a list of tokens.

    Tokens are of the form (linenum, col, type, value), representing the
    line and column number of the start of the token in the file (as ints),
    the type of token as a string, and the actual text itself.

    """
    # Run vera++, and pass the output through re.findall
    tokenstring = subprocess.check_output(['tokenizer/vera++', '-rule', 'DUMP', filename])
    tokens = re.findall("(?m)^(\d+)/(\d+)\\t(\w+)\\t(.+|\n)$", tokenstring)

    # Convert line and column numbers to ints
    tokens = [(int(a), int(b), c, d) for a, b, c, d in tokens]
    return tokens

if __name__ == "__main__":
    # sample usage
    import sys, pprint
    for filename in sys.argv[1:]:
        pprint.pprint(tokenize(filename))

