#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
  FILE *f = fopen("shel.txt","rb");
  fseek(f,0,SEEK_END);
  long file_n = ftell(f);
  rewind(f);

  char *buffer = (char*) malloc(file_n * sizeof(char));
  fread(buffer,file_n,1,f);
  fclose(f);
  printf("EGG=%x\n",buffer);

  setenv("EGG","buffer",1);
  return 0;
}
