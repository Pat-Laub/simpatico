# Style Guide Summary

This is a list of implementation details. For the full set of official rules,
consult the style guide itself.

## Indentation

1. Each indentation level is 4 spaces.
2. A tab character is equivalent to 8 spaces.
3. Indent level increases by 1 for subsequent lines when one of the following occurs:
 1. an open brace `{` is found.
 2. a `case` or `default` statement is found.
 3. a control structure is found which does not have its body in braces.
4. Indent level should increase by 2 for subsequent lines when:
 1. a statement that began on the current line did not finish on the current line
    (Either it is not a control statement which does not end in a `;`, or it is
    a control statement that has not yet ended).
5. Indent level should decrease by 1 when:
 1. a close brace `}` is found. If the `}` is the first non-whitespace token of
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

### Notes

* For switch statements, rules 5.2 and 3.2 combine to provide the expected behaviour.
  Rule 5.2 makes sure that the `case` and `default` statements are always one indent
  behind the body above, and 3.2 makes sure that the body below is one indent ahead:
  ```
    switch(x) {
        case 1:
            ...
            ... // Indentation must decrease after this
        case 2: // Indentation must increase after this
            ...
    }```
* Multiple rules can be applied in the same line. For instance, at the end of
  a control statement which spans multiple lines, rules 6.1 and 3 both apply,
  giving a net loss of one indentation level:
  ```
    if (a && b && ...
            && x && y && z) {
        ...
    }```
* Rules 3.3 and 5.3 are necessary to avoid applying double penalties for misuse
  of braces.

## Thoughts and TODOs

* Indentation - should indentation increase when an open brace is found, or
  when a control structure is found?
** If indentation is done when a brace is found, it's easier to code, but is
   susceptible to breaking when the control structure is missing a brace.
** If indentation is done when a control structure is found, it will be necessary
   to hard-code all possible control structures, including function definitions.
