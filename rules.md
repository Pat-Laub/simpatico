# Style Guide Summary

This is an unofficial, extensive list of style rules implemented
(or, to implement).
For the full set of official rules, consult the style guide itself.

## Naming

1. Variable names start with a lowercase letter, do not contain underscores.
2. File names start with a lowercase letter, do not contain underscores.
3. #defined constants don't contain lowercase letters, except `true` and `false`.
4. Function names don't contain uppercase letters.
5. Type/struct/union names start with an uppercase letter, do not contain underscores.

### Examples

Example code:

    #define DEFAULT_SPEED 10

    int book, newCount, setWordLength;

    int main();
    void reset_secret_string();

    typedef int Number;
    struct Point { int x; int y; }

Example filenames: `hello.c`, `stringRoutines.c`

## Comments

No comment rules are implemented in simpatico.

## Braces

1. Use braces around the body of control statements (except `case` and `default`
   within a switch statement).
2. The open brace should be on the same line as the control statement with at
   least one space before.
3. The close brace should be at the start of a line.
4. `else` and `else if` clauses, and the `while` part of a `do`-`while` loop,
   should be on the same line as the close brace before it.
5. The open brace for a function definition may be at the end of the line or
   at the start of the next line (with no indentation).
6. Structure declarations and array initialisations don't need to follow these rules.

Note indentation rule 5.1 implies that the close brace should have the same
indentation as the open brace.

### Examples

    if (...) {
        ...
    } else if (...) {
        ...
    } else {
        ...
    }

    for (...; ...; ...) {
        ...
    }

    while (...) {
        ...
    }

    do {
        ...
    } while (...);

    switch (...) {
        case ...:
            ...
        default:
            ...
    }

## Vertical Whitespace

1. Functions are separated by blank lines.

Example:

    void foo() {
        ...
    }

    void bar() {
        ...
    }

## Indentation

1. Each indentation level is 4 spaces.
2. A tab character is equivalent to 8 spaces.
3. Indent level increases by 1 for subsequent lines when one of the following occurs:
 1. A control strutcure, or `case` or `default` statement is found. Indentation
    increases after the statement is complete (in case
    it spans over multiple lines).
 2. The open brace `{` at the start of a function definition is found.
    (See the TODO notes below)
4. Indent level should increase by 2 for subsequent lines when:
 1. a statement that began on the current line did not finish on the current line
    (Either it is not a control statement which does not end in a `;`, or it is
    a control statement that has not yet ended).
5. Indent level should decrease by 1 when:
 1. a close brace `}` is found ending a code block.
    If the `}` is the first non-whitespace token of
    the line, the indentation level should decrease for that line, otherwise the
    indentation should decrease only for subsequent lines.
 2. directly in a `case` or `default` body, and a `case` or `default` line
    is found, indentation should decrease for that line.
 3. a control structure which does not have its body in braces has reached the
    end of its body statement.
6. Indent level should decrease by 2 for subsequent lines when:
 1. a statement that has continued over multiple lines (cf. rule 4.1) has finished.
 2. directly in a `case`/`default` body, and the end of the `switch` statement
    is detected (cf. rules 5.1 and 5.3).

### Examples and Notes

    void foo()
    {                       // Rule 3.2: +1 indent after this line
        int a[] = {2, 3,    // Rule 4.1: +2 indents after this
                1, 0};      // Rule 6.1: -2 indents after this
        if (1) {            // Rule 3.1: +1 indents after this
            bar();
        } else {            // } - Rule 5.1 (-1 indents). { - Rule 3.1 (+1 after this)
            baz(); }        // Rule 5.1: -1 after this. Note this is an error in braces.
        baz(a + b + c +     // Rule 4.1: +2 indents after this.
                d + e +
                f);         // Rule 6.1: -2 indents after this.
        while (1)
            baz();          // Rule 5.3: -1 after this. Note this is an error in braces.
    }                       // Rule 5.1: -1 from here.

* For switch statements, rules 5.2 and 3.1 combine to provide the expected behaviour.
  Rule 5.2 makes sure that the `case` and `default` statements are always one indent
  behind the body above, and 3.1 makes sure that the body below is one indent ahead:

        switch(x) {
            case 1:
                ...
            case 2:   // Rule 5.2: -1 indents on this line; Rule 3.1: +1 indents after this.
                ...
        }             // Rule 6.2: -2 indents on this line.

* Multiple rules can be applied in the same line. For instance, at the end of
  a control statement which spans multiple lines, rules 6.1 and 3 both apply,
  giving a net loss of one indentation level:

        if (a && b && ...
                && x && y && z) {
            ...
        }

* Rule 5.3, and the wording of 3.1 (emphasis on the control structure, not the
  open brace), is necessary to avoid applying double penalties for misuse of braces.

## Horizontal Whitespace

1. Space (or a newline) must be added after each comma `,` and semicolon `;`.
2. Space must be added before and after assignment operator `=`, `+=`, etc.

### Examples

    for(a; b; c) {      // Spaces after each ;
        foo(x, y, z);   // Spaces after each , and newline after ;
        x *= y;         // Spaces around the *=
    }

## Line Length

1. Line length must be &lt;= 79 characters, including comments and spaces.
   Recall that a tab character is equivalent to 8 spaces.

## Overall

1. Functions should be "about 50 lines maximum".
2. Don't use `goto`.

## Manual checks

This section lists style points which are impractical for simpatico to check,
and so must be checked by hand.

1. Names are appropriate, source files end with .c
2. Comments
3. Vertical Whitespace
4. Readability
5. Modularity
6. Code repetition
7. Compiler warnings and errors
8. Code with syntax errors (which could confuse the tokeniser and give incorrect
   output)


## Thoughts and TODOs

* Indentation - should indentation increase when an open brace is found, or
  when a control structure is found?
  * If indentation is done when a brace is found, it's easier to code, but is
   susceptible to breaking when the control structure is missing a brace, or a
   brace occurs that isn't used for a code block (e.g. initialising an array).
  * If indentation is done when a control structure is found, it will be necessary
   to code in _all_ possible control structures, including function definitions.
* Vertical whitespace - should separate statements be separated by newlines?
  * It makes sense to insert newlines after statements, but it's not mentioned in
   the style guide.
* What are all possible control statements?
  * `if`
  * `else`
  * `else if` (keeping sure not to count this as both `else` and `if`)
  * `for`
  * `while` (but not the `while` part of a `do`-`while`)
  * `do`
  * `switch`
  * `case`
  * `default`
  * `struct` (no need to treat `typedef struct` separately)
  * `union`
  * function definitions.
  * more?
