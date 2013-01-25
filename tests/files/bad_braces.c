/* Contains bad brace violations of different types, including mixes of
** good and bad. Currently contains
** 18 (or 20?)
** violations.
*/

/* 1 violation (or 2?) (open brace not at end of line, close not at start of a line) */
void badfunc(void) { return; }

/* 3 violations */
int fa(int a) {
    if (a)
    { //violation (open brace not on same line)
        a++;
    } //violation (the whole line of } else if {)
    else if (a+1)
    {
        a /= 2;
    } //violation (the whole line of } else {)
    else
    {
        a--;
    }
    return fb(a);
}

/* 4 violations */
int fb(int a) {
    if (a) 
    { //violation
        a++;
    } else if (a + 1)
    { //violation
        a--;
    } else
    { //violation
        return 0; } // violation (close brace not at start of line)
    return a;
}

/* 3 violations */
void missing_braces(void) {
    int a;
    if (a) //violation
        return 0;
    else if (a - 1) //violation
        return 1;
    else //violation
        return 2;
}

/* 4 (or 5?) violations */
void bad_loops(void) {
    for (int i = 0; i < 10; i++) 
    { //violation
        a = i;
    }
    for (;;) { break; } //violation (or 2?)
    do
    { //violation
        a++;
    }
    while (!a); // violation (not on same line as })
}


/* 3 violations */
int main () {
    int a;
    switch (a){ //violation (no space before open brace)
    case 0:
        return 0;
    default:
        break;
    }
    if (fa(a)) {
        a = 1;
    } //violation
    else if (fb(b)) {
        a = 2;
    } //violation
    else {
        a = 3;
    }
}
