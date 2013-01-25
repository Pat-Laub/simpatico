/* This file doesn't have indentation errors. It does have brace errors,
   which should not break the indentation checker. */

struct Foo {
    int x;
    int y;
}

int main(int argc, char** argv)
{
    int x = 0;
    
    if (x == 1) {
        return 1;
    } else if (x == 2) {
	x = 2; // tab character (equivalent to 8 spaces)
    }
    else
    {
        x = 3; }

    // Try for some non-brace code blocks
    if (x == 0 || x == 1 || x == 2 ||
            x == 3 || x == 4 ||
            x == 5 || x == 6 ||
            x == 7)
        for (int i = 0; i < 10; ++i)
            x += i;

    x = 0 + 0 + 0 + 0 + 0 +
            0 + 0 + 0 + x;
    x = x;

    // The next line has lots of spaces in it.
             

    // nesting
    if (x == 0) {
        do {
            switch (x) {
                case 0:
                case 1:
                    x++;
                    if (x == 1) {
                        x = x;
                    }
                    break;
                default:
                    x++;
            }
        } while (x == 0);
    }

    return 0;
}
