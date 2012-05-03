#include <stdio.h>

    int one = 1;

int main() {
    int sum = 0;
        int i;

    for (i = 0; i <= 4; ++i) {
        printf("sum is now %d\n", sum);
       sum += i;
    }

    // A really long statement that has to cover lots of lines
    if (sum == 1 || sum == 2 || sum == 3 || sum == 4 || sum == 5 ||
            sum == 6 || sum == 7 || sum == 8 || sum == 9 || sum == 11 ||
        sum == 12 || sum > 12) {
        printf("something went wrong!\n");
        printf("oh noes!\n");
    } else {
    printf("the sum is %d!\n", sum);
    }

    int x = 2, y;
    switch(x) {
        case 0:
                y = 0;
                break;
        case 1:
        y = 1;
        case 2:
            y = 2;
            break;
        case 3:
        case 4:
            y = 4;
            break;
        default:
            x = 0;
        y = -1;
            break;
    }

    }
