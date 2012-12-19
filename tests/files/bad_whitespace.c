/* Whitespace errors on lines 4, 8, 9, 10, 11, 11, 11, 12, 12 */

#include <stdio.h>
int foo,bar;                      // no space after ,

int zero() {
    return 0;
}                                 // no blank line
int main(int argc,char** argv) {  // no space after ,
    int x=1;                      // no space around =
    int y= 3;x <<=y;              // no space before = or after ; or after <<=
    for (;;) {                    // no space after ; (2 errors)
        continue;
    }
    return 0;
}
