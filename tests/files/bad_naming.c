/* Contains naming violations of different types. Currently contains
** 7
** violations.
*/

typedef struct bobStruct { /* violation */
    int thing;
} GoodStruct;

typedef struct Thing {
    int thing;
} badStruct; /* violation */

int A; /* violation */
char a_char; /* violation */

void FunctionBad(void) { /* violation */
}

void functionStuff(void) { /* violation */
}

void struct_var(bobStruct BobStruct) { /* violation  (var naming) */
}
