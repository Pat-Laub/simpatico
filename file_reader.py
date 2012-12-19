import tokenizer

__all__ = ['FileReader']

class FileReader(object):
    """Keeps track of the tokens and lines in the file."""
    def __init__(self, filename):
        self._filename = filename
        with open(filename, 'rU') as f:
            self._lines = f.readlines()
        self._tokens = tokenizer.tokenize(filename)
        self._len_tokens = len(self._tokens)
        self._len_lines = len(self._lines)
        # internally index tokens and lines from 0
        self._pos = self._linenum = -1

    def reset(self):
        """Reset back to the start so that it can be used again."""
        self._pos = self._linenum = -1

    def next_line(self):
        """Advance to the next line."""
        self._linenum += 1
        line = self._lines[self._linenum]

        # Advance the tokens until we are past the next newline
        while (self._pos < self._len_tokens and
                self._tokens[self._pos].linenum != self._linenum + 1):
            self._pos += 1
        
        return line

    def next_tok(self):
        """Advance to the next token."""
        self._pos += 1
        tok = self._tokens[self._pos]

        # Advance the line number if necessary
        if self._linenum < 0 or (self._pos < self._len_tokens and
                self._tokens[self._pos].type == 'newline'):
            self._linenum += 1

        return tok

    def file_line(self):
        """Return the filename and  line number of the current line"""
        return self._filename, self._tokens[self._pos].linenum

    def end(self):
        """Have we reached the end of the tokens?"""
        return self._pos >= self._len_tokens - 1

    def end_lines(self):
        """Have we reached the last line?"""
        return self._linenum >= self._len_lines - 1

    def back(self, n):
        """Look at the n-th previous token. Watch out for IndexErrors."""
        return self._tokens[self._pos - n]

    def forward(self, n):
        """Look at the n-th following token. Watch out for IndexErrors."""
        return self._tokens[self._pos + n]

