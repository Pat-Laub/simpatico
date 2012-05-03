/* Contains no brace violations of any type.*/

int array[] = {1, 2, 3, 4};
int another[] = {
    1,
    2,
    3,
    4
};
int yetAnother[] = {1, 2, 3,
        4};
int anotherStill[] = {1, 2, 3, \
        4};

void if_continutation(void) {
    if (1 && 2 &&
            3 && 4) {
        return;
    }
}

int fa(int a) {
    if (a) {
        a++;
    } else if (a+1) {
        a /= 2;
    } else {
        a--;
    }
    return fb(a);
}

int fb(int a) {
    if (a) {
        a++;
    } else if (a + 1) {
        a--;
    } else {
        return 0;
    }
    return a;
}

int main () {
    int a;
    switch (a) {
        case 0:
            return 0;
        default:
            return 1;
    }
    for (int i = 0; i < 10; i++) {
        a = i;
    }
    while (!a)  {
        a++;
    }
    if (fa(a)) {
        a = 1;
    } else if (fb(b)) {
        a = 2;
    } else {
        a = 3;
    }

}
