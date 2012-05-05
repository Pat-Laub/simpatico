/* Contains bad brace violations of different types, including mixes of
** good and bad. Currently contains
** 17
** violations.
*/

/* 1 violation */
void badfuncA(void)
{
    return;
}

/* 1 violation */
void badfuncB(void) { return; }

/* 3 violations */
int fa(int a) {
    if (a)
    { //violation
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

/* 3 violations */
int fb(int a) {
    if (a) 
    { //violation
        a++;
    } else if (a + 1)
    { //violation
        a--;
    } else
    { //violation
        return 0;
    }
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

/* 3 violations */
void bad_loops(void) {
    for (int i = 0; i < 10; i++) 
    { //violation
        a = i;
    }
    for (;;) { break; } //violation
    while (!a)  
    { //violation
        a++;
    }
}


/* 3 violations */
int main () {
    int a;
    switch (a)
    { //violation
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
