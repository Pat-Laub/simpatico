int main(int argc, char** argv) {
    goto foo;
    1 / 0;
    foo:
    return 0;
}
