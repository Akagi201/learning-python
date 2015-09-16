
// gcc -fPIC -shared -o segfault.so segfault.c

int fault(void) {
    char *s = "hello world";
    *s = 'H';
    return 0;
}