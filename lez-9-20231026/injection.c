void bye1(){ puts("Goodbye!\n"); }

void bye2(){ puts("Farewell!\n"); }

void hello(char *name, void (*bye_func)()){
    printf("Hello %s!\n", name);
    bye_func();
}

int main(int argc, char **argv){
    char name[1024];
    gets(name);
    srand(time(0));
    if(rand() % 2) hello(bye1, name);
    else hello(name, bye2);
}
