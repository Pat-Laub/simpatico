# DEPRECATED
### Go to [Simon's fork](https://github.com/SJShaw/simpatico) for a totally revamped version of this project.

simpatico
=========

A C source code style checker..

## What is it?

This style marker should enforce the rules outlayed in
the 'csse2310-style-guide.pdf' which was created for the computer
science course 'CSSE2310' at the University of Queensland.

## Motivation

If/when this project becomes more reliable than the previous
implementations of the automarker then the tutors of this 
course will swap over to using 'simpatico' for their marking.

Also, many hours of marking time is quite expensive for such
a menial task, and this project could save money as well 
as time and effort.

## Current method

Currently a C++ program called 'vera++' tokenises the C
source code input and feeds it to a very large tcl script
which generates the errors. 

This script has many issues and is terribly hard to modify.
One of the major problems with the current script is that
it generates a large number of style errors for validly 
styled C code.

After the automarker is complete the course tutors must go
through the generated errors extremely carefully to validate
the process. Very frequently the tutors make mistakes.

## Error Format

Each style error must be declared in the format:
    filename:lineNumber: [CATEGORY] Description

The categories are roughly described below. More details are given in
`rules.md` and in `csse2310-style-guide.pdf`.

### NAMING
- variables
- defines
- functions
- typedefs

### BRACES
- space before brace
- correct placement
- correct alignment

### INDENTATION
- multiples of four spaces
- nesting correctly indented
- line continuation

### WHITESPACE
- grammatical spacing around assignment operators
- correctly spaced vertically

### COMMENTS
- globals
- functions (parameters esp.)
- lengthy or tricky code

### OVERALL
- no function over 50 lines
- modularity / no excessive duplication of code

### LINE-LENGTH
- all lines must be shorter than 80 chars long (including \r)

## Usage

```
./simpatico.py file1.c file2.c
```
