#include<sys/mman.h>
#include<unistd.h>
int main(void){
    void *page = mmap(0x1337000, 0x1000, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANON, 0, 0); // riserva 1000 byte in cui disabilita tutte le protezioni
    read(0, page, 0x1000); //legge da stdin fino a 1000 byte in questa zona (o al primo EOF)
    ((void(*)())page)(); //manda in esecuzione 
    return 0;
}
