/* No whitespace errors here, vertical or horizontal. */

#include <stdio.h>
int foo, bar;
int zero()
{
    return 0;
}

int main(int argc, char** argv) {
    int x = 1, y = x;
    y += 2; x <<= y;    // can have multiple statements on the same line

    if(0) {
        ;
    }

    for(int i = zero(); i<10; i++) {
        printf("%d\n", i); // prints i
    }

    return y-3;
}
