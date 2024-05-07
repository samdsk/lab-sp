#include <stdio.h>
int x=0;
int function(){
    int * ret;
    x=x+13;
    ret = (int *) &ret + 16 // or 8
    (*ret) = (*ret) + 8; // numero da trovare
}
int main(){
    x=function();
    x=10;
    printf("Value of x = %d\n",x);
}