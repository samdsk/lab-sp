#include <stdio.h>

int main(){
	char buf[80];
	int cookie;
	printf("buf: %08x cookie: %08x\n",&buf,&cookie);
	gets(buf);
	if(cookie == 0x41424344)
		printf("You Win!\n");
}
