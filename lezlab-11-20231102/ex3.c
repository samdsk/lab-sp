#include <stdio.h>
int x = 0;

int function(){
    int * ret;
    x = x + 13;
    ret = (int *) &ret + 4; // 4 = 4 = 4 = 4 = 16 bytes
    (*ret) = (*ret) + 16; // XX numero da trovare
}
int main(){
    x = function();
    x = 10;
    printf("Value of x = %d\n", x); // deve stampare 13
}

// rsp @ ret -> 7fffffffde48
// return address 0x55555178
// correct address to jump to print x = 13 is -> 0x5188 - 0x5178 = 16 bytes
// skipping x = 10
