/* This currently contains
   13
   indentation violations (as well as some brace violations, which shouldn't
   affect the correctness of the indentation checker).
*/
struct Foo {
    int foo1;
        int foo2;       // violation
      int foo3;         // violation - not a multiple of 4 spaces
}

void function(void) {
int x;   // violation
return;  // another violation ?
}

int main(int argc, char** argv)
{
    int x = 0;
    if (x == 0 ||
        x == 1) {       // violation - should indent by +2 not +1
        switch (x) {
            case 0:
                x = 2;
                case 1:     // violation - should decrease indent by 1
                x = 3;
            }           // violation - should decrease indent by 2 not 1
    }

        if (x == 2) {       // violation - should be at 1 indent
            x = 4;          // violation - should be at 2 indents
        x = 5 + 0 + 0 + 0 + 0 + 0 +
        0 + 0 + 0 +         // violation - should indent by 2
        0 + 0;              // violation - should stay indented by 2
    }


    if (x == 2)
    x = 3;          // violation - should be indented by +1
    x = 4;
    

    }       // violation - should decrease indent by 1.
