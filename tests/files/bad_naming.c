/* Contains naming violations of different types. Currently contains
** 8
** violations.
*/
#define Pi 3.1416   /* violation */

typedef struct bobStruct { /* violation */
    int thing;
} GoodStruct;

typedef struct Thing {
    int thing;
} Bad_Struct; /* violation */

int A; /* violation */
char a_char; /* violation */

void FunctionBad(void) { /* violation */
}

void functionStuff(void) { /* violation */
}

void struct_var(bobStruct BobStruct) { /* violation  (var naming) */
}
