# Pwn college Embryoio  

## lvl 1
```sh
bash
/challenge/...
```
## lvl 2
```sh
bash
echo "pass" | /challenge/...
```
## lvl 3
```sh
bash
/challenge/... password
```
## lvl 4
```sh
bash
export key=value
/cha...
```
## lvl 5
```sh
bash
echo "password" > /tmp/...
/cha... < /tmp/...
```
## lvl 6

```sh
bash
/cha.. > /tmp/...
cat /tmp/...
```

## lvl 7

    env -i ./emb...

env = to print env variables, option -i for run it as ignoring env vars.


## lvl 8
create shell script that calls embr... lvl 8 file

## lvl 9
create shell script that calls embr... lvl 9 file then type password in terminal

## lvl 10
create shell script that calls embryoio_level10 with password as first arg.

## lvl 11 
export VAR=string
create shell script that calls embryoio_level11 

## lvl 12
/challenge/embryoio_level12 < /tmp/eaiuxe

## lvl 13
/challenge/embryoio_level13 > /tmp/ovyngy

## lvl 14
env -i /challenge/embryoio_level14

## lvl 15
~~~py
    # run bash script from ipython
    # run ipython 
    import subprocess; \
    subprocess.run("/challenge/embryoio_level15")
~~~
~~~py
    # run bash script from ipython
    # run ipython 
    from pwn import *; \
    p = process("/challenge/embryoio_level15")
    p.interactive()
~~~

## lvl 16
same as lvl 15

## lvl 17
~~~py
    # run bash script from ipython
    # run ipython 
    import subprocess; \
    subprocess.run(["/challenge/embryoio_level17","yixpnqntuu"])
~~~
## lvl 18
~~~py
    # run bash script from ipython
    # run ipython 
    import subprocess; \
    import os; \
    os.environ["var"]="str"; \
    subprocess.run(["/challenge/embryoio_level17","yixpnqntuu"])
~~~
~~~py
    # run bash script from ipython
    # run ipython 
    from pwn import *
    p = process(["/challenge/embryoio_level18"],env={"key":"value"})
    p.interactive()
~~~
 

## lvl 19

~~~py
import subprocess; \
file = open("/tmp/jkibzf","r"); \
subprocess.run(["/challenge/embryoio_level19"],stdin=file);
~~~
~~~py
    # run bash script from ipython
    # run ipython 
    from pwn import *;\
    p = process(["/challenge/embryoio_level19"],stdin=open('/tmp/..','r'));\
    p.interactive()
~~~
 

## lvl 20

~~~py
import subprocess; \
file = open("/tmp/jkibzf","w"); \
subprocess.run(["/challenge/embryoio_level19"],stdout=file);
~~~

    cat /tmp/file

 

## lvl 21

    env -i python
    # rest is same as lvl 20
 

## lvl 22
~~~py
#!/user/bin/python
import subprocess
subprocess.run("/challenge/embryoio_level22")
~~~
 

## lvl 23

same as 22

 

## lvl 24
same as lvl 17
 

## lvl 25
same as lvl 18
 

## lvl 26
same as lvl 19
 

## lvl 27
same as 20
 

## lvl 28
same as 21

```python
from pwn import *

p = process('/challenge/embryoio_level28',env={})
p.interactive()
```

## lvl 29

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


void pwncollege(){
        pid_t pid = fork();

        if(pid == 0){
                char *path = "/challenge/embryoio_level29";
                char *args[] = {path,NULL};
                char *evn[] = {NULL};
                execve(path,args,evn);
        }else wait(NULL);
}


int main(){
        pwncollege();
        exit(0);
}
~~~

## lvl 30
same as 29

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


void pwncollege(){
        pid_t pid = fork();

        if(pid == 0){
                char *path = "/challenge/embryoio_level30";
                char *args[] = {path,NULL};
                char *evn[] = {NULL};
                execve(path,args,evn);
        }else wait(NULL);
}


int main(){
        pwncollege();
        exit(0);
}
```

## lvl 31
~~~c
#include <stdio.h>           
                             
void pwncollege(){ 
    int pid = fork();        
                            
    if(pid<0)                
        printf("Error! \n");                               
                                
                                
    if(pid==0){              
        char *prog = "/challenge/embryoio_level30";
        char *args[] = {prog,"zxwzemwbyv"};       
        execve("/challenge/embryoio_level31", args,NULL);
                            
    }else waitpid(pid);            
}                            
                            
int main(){                  
    pwncollege();
    return 0;                
}
~~~ 

## lvl 32

    export var=str

~~~c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


void pwncollege(){}

int main(int argc, char** args, char** env){
        pid_t pid = fork(); 

        if(pid == 0){
                char *path = "/challenge/embryoio_level32";
                char *args[] = {path,NULL};
                execve(path,args,env);
        }else wait(NULL);

        exit(0);
}       
~~~ 

 

## lvl 33

    echo "psw" > /tmp/file

~~~c
#include <stdio.h>      
      
void pwncollege(char** argv, char** envp){
    int pid = fork();
        
    if(pid<0)
        printf("Error while forking! \n");    
        
        if(pid==0){
            char *prog = "/challenge/embryoio_level33";
            char *args[] = {prog};
            
            execve(prog, argv,envp);
            
        }else waitpid(pid);
}     
    
int main(int argc, char** argv, char** envp){
    pwncollege(argv, envp); 
    return 0;
}     
~~~ 

    ./file < /tmp/file

 
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/stat.h>

void pwncollege(){}

int main(int argc, char** args, char** env){
        pid_t pid = fork();

        if(pid == 0){
                char *path = "/challenge/embryoio_level33";
                char *args[] = {path,NULL};
                char *env[] = {NULL};
                int fd = open("/tmp/brxhzr",O_RDONLY);
                dup2(fd,0);
                execve(path,args,env);
        }else wait(NULL);

        exit(0);
}
```

## lvl 34
same as 33

    ./binary > /tmp/file
 

## lvl 35
same as 33
env -i ./binaryfile
 

## lvl 36
    bash
    /embryoio_level36 | cat
 

## lvl 37
    bash
    /embryoio_level37 | grep ""
 

## lvl 38
    bash
    /embryoio_level38 | sed ""
 

## lvl 39
    bash
    /challenge/embryoio_level39 | rev | rev
 

## lvl 40
    bash
    cat | /challenge/embryoio_level40
 

## lvl 41
    rev | rev | /challenge/embryoio_level41 
 

## lvl 42 -> 47
    just put previous sols inside a .sh file

## lvl 48
~~~py
import subprocess; \ 
p1 = subprocess.Popen(["/challenge/embryoio_level48"], stdout=subprocess.PIPE); \
subprocess.run(["cat"],stdin=p1.stdout);

# use subprecess.PIPE to pipe stdin and stdout between subprocs
~~~

alternative with pwntools
```python
from pwn import * ;\
cat = process(['cat']) ;\
p = process(["/challenge/embryoio_level48"], stdout=cat.stdin) ;\
cat.interactive()
```
 

## lvl 51
~~~py
import subprocess; \
p1 = subprocess.Popen(["/challenge/embryoio_level51"], stdout=subprocess.PIPE); \
p2 = subprocess.Popen(["rev"],stdin=p1.stdout, stdout=subprocess.PIPE); \
subprocess.run(["rev"],stdin=p2.stdout);
~~~
 

## lvl 52
~~~py
import subprocess; \
p1 = subprocess.Popen(["cat"], stdout=subprocess.PIPE); \
p2 = subprocess.run(["/challenge/embryoio_level52"],stdin=p1.stdout); \
p1.stdout.close();
~~~
 

## lvl 53
~~~py
# the challenge checks for a specific parent process : ipython
# the challenge checks for a specific process at the other end of stdin : rev
# the challenge will check for a hardcoded password over stdin : bpryrntd

import subprocess; \
p1 = subprocess.Popen(["rev"], stdout=subprocess.PIPE); \
p2 = subprocess.Popen(["rev"], stdout=subprocess.PIPE,stdin=p1.stdout); \
p3 = subprocess.run(["/challenge/embryoio_level53"],stdin=p2.stdout); \
p1.stdout.close();\
p2.stdout.close();
~~~
 

## lvl 54 -> 59
    same as ipython challenges

## lvl 60
~~~c
#include <fcntl.h>
#include <stdio.h>  
#include <unistd.h>     
      
void pwncollege(char** argv, char** envp){
    pid_t pid = fork();
        
    if(pid<0)
        printf("Error while forking! \n");    
        
    if(pid==0){
        char *prog = "/challenge/embryoio_level60";
        char *args[] = {prog};
        
        execve(prog, argv, envp);
        
    }else waitpid(pid);
}     
    
int main(int argc, char** argv, char** envp){
    pwncollege(argv, envp);
    return 0;
}
~~~

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>

void pwncollege(){}

int main(){
    int fd[2];

    if(pipe(fd) == -1){
        perror("pipe error\n");
        exit(EXIT_FAILURE);
    }

    pid_t p = fork();

    if(p == 0){
        dup2(fd[1],1);
        close(fd[0]);
        close(fd[1]);
        char *prog = "/challenge/embryoio_level60";
        execlp(prog,prog,NULL);
    }
    
    pid_t c = fork();

    if(c == 0){
        dup2(fd[0],0);
        close(fd[0]);
        close(fd[1]);

        execlp("cat","cat",NULL);
    }
    
    close(fd[0]);
    close(fd[1]);

    waitpid(p,NULL,0);
    waitpid(c,NULL,0);

    exit(0);
}
```

## lvl 64
~~~c
// the challenge checks for a specific parent process : binary
// the challenge checks for a specific process at the other end of stdin : cat

#include <fcntl.h>
#include <stdio.h>  
#include <unistd.h>     
      
void pwncollege(char** argv, char** envp){
    pid_t pid = fork();
        
    if(pid<0)
        printf("Error while forking! \n");    
        
    if(pid==0){
        char *prog = "/challenge/embryoio_level64";
        char *args[] = {prog};
        
        execve(prog, argv, envp);
        
    }else waitpid(pid);
}     
    
int main(int argc, char** argv, char** envp){
    pwncollege(argv, envp);
    return 0;
}

// gcc file.c -o file
// cat | ./file
~~~
```c
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <fcntl.h>

void pwncollege(){}

int main(){
    int fd[2];
    pipe(fd);

    pid_t cat = fork();

    if(cat == 0){
        dup2(fd[1],1);
        close(fd[0]);
        close(fd[1]);

        execlp("cat","cat",NULL);
    }
    
    pid_t p = fork();

    if(p == 0){
        dup2(fd[0],0);
        close(fd[0]);
        close(fd[1]);
        char* prog = "/challenge/embryoio_level64";

        execlp(prog,prog,NULL);
    }
    
    close(fd[0]);
    close(fd[1]);

    waitpid(p,NULL,0);
    waitpid(cat,NULL,0);

    exit(0);
}
```

## lvl 66
    # parent process : find
    find -type f -name embryoio_level66 -exec ./embryoio_level66 {} \;
    find -type f -name embryoio_level66 -exec ./embryoio_level66 {} +

## lvl 67 

    find /challenge/  -type f -name "embryoio*" -exec {}  xmuqgzzfqn  \;
    # {} is the file like foreach found files execute "-exec commands"

## lvl 68

    # parent process : shellscript
    # argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 48:lxckkspssc

~~~sh
#!/bin/bash        
# str concatenation                 
str="a "           
for index in {0..45}
do                 
    str="${str}a " 
done               
str="${str}"lxckkspssc
                   
/challenge/embryoio_level68 $str
~~~

## 70
~~~sh
#!/bin/bash
# numeric enviroment key name
# parent process : shellscript
# environment is empty
# env[KEY] holds value VALUE (listed to the right as KEY:VALUE) : 101:spoudwaumn
env -i 101=spoudwaumn /challenge/embryoio_level70  
~~~

## 71
```sh
  1 #!/bin/bash
  2 STR=$( python -c "print('1 '*218+'sfjtqttgfa')")                                                    
  3 env -i 172=imndahteji /challenge/embryoio_level71 $STR 
```
## 72

    # create dir 
    mkdir /tmp/nqfdgp
    # enter
    cd /tmp/nqfdgp
    # create the file
    touch asvyeq

```s
  1 #!/bin/bash                         
  2 /challenge/embryoio_level72 < asvyeq 
```
Task: 
- the challenge checks for a specific parent process : shellscript
- the challenge will check that input is redirected from a specific file path : asvyeq
- the challenge will check that it is running in a specific current working directory : /tmp/nqfdgp

## 73
```sh
  1 #!/bin/bash                  
  2 cd /tmp/kcdoym               
  3 /challenge/embryoio_level73 &
  4 cd ~   
  5 sleep 1   
```
Task: 
- the challenge checks for a specific parent process : shellscript
- the challenge will check that it is running in a specific current working directory : /tmp/kcdoym
- the challenge will check to make sure that the parent's parent CWD to be different than the challenge's CWD

## 74
```py
  1 import subprocess
  2 c = ["1"]*280          
  3 c[279]="sbujygveya"
  4 c[0]="/challenge/embryoio_level74"
  5         
  6 subprocess.run(c)
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 279:sbujygveya

## 78
```py
  1 import subprocess
  2 file = open("mwypan","r")
  3 subprocess.run(["/challenge/embryoio_level78"],stdin=file) 
```
Task: 
- the challenge checks for a specific parent process : python
- the challenge will check that input is redirected from a specific file path : mwypan
- the challenge will check that it is running in a specific current working directory : /tmp/pqkoft

## 79
```py
1 import subprocess
2 p1 = subprocess.Popen(["/challenge/embryoio_level79"],cwd="/tmp/jxnvtl")
3 p1.wait()    
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will check that it is running in a specific current working directory : /tmp/jxnvtl
- the challenge will check to make sure that the parent's parent CWD to be different than the challenge's CWD

## 80

```c
  1 #include <fcntl.h>
  2 #include <stdio.h>  
  3 #include <unistd.h>     
  4                 
  5 void pwncollege(char** argv, char** envp){            
  6     pid_t pid = fork(); 
  7                 
  8     if(pid<0)   
  9         printf("Error while forking! \n");            
 10                 
 11     if(pid==0){ 
 12         char *args[151];
 13         for(int i=0;i<151;i++) args[i] = "mmndmplsfi";
 14         args[151] = NULL;                                                                           
 15         execv("/challenge/embryoio_level80", args);
 16                 
 17     }else waitpid(pid); 
 18 }               
 19                 
 20 void main(int argc, char** argv, char** envp){        
 21     pwncollege(argv, envp);                           
 22 }  
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 150:mmndmplsfi

## 82
```c
  1 #include <fcntl.h>          
  2 #include <stdio.h>          
  3 #include <unistd.h>         
  4                             
  5 void pwncollege(char** argv, char** envp){
  6     pid_t pid = fork();     
  7                             
  8     if(pid<0)               
  9         printf("Error while forking! \n");           
 10                             
 11     if(pid==0){             
 12         char *env[] = {"312=eqybcrweat",NULL};                                                      
 13         execve("/challenge/embryoio_level82",argv, env );
 14                             
 15     }else waitpid(pid);     
 16 }                           
 17                             
 18 void main(int argc, char** argv, char** envp){       
 19     pwncollege(argv, envp);   
 20 }                           
```
    env -i ./s

Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that the environment is empty (except LC_CTYPE, which is impossible to get rid of in some cases)
- the challenge will check that env[KEY] holds value VALUE (listed to the right as KEY:VALUE) : 312:eqybcrweat

## 83

```c
  1 #include <fcntl.h>
  2 #include <stdio.h>  
  3 #include <unistd.h>     
  4                
  5 void pwncollege(char** argv, char** envp){
  6     pid_t pid = fork();
  7                
  8     if(pid<0)  
  9         printf("Error while forking! \n");      
 10                
 11     if(pid==0){
 12         char *args[177];
 13         for(int i=0;i<177;i++) args[i] = "gffrnmbjqi";
 14         args[177] = NULL;                                                              
 15         char *env[] = {"122=bpcjagpuyx",NULL};
 16         execve("/challenge/embryoio_level83",args, env );
 17           
 18     }else waitpid(pid);
 19 }              
 20          
 21 void main(int argc, char** argv, char** envp){
 22     pwncollege(argv, envp);
 23 } 
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that the environment is empty (except LC_CTYPE, which is impossible to get rid of in some cases)
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 176:gffrnmbjqi
- the challenge will check that env[KEY] holds value VALUE (listed to the right as KEY:VALUE) : 122:bpcjagpuyx

## 84

```c
  1 #include <fcntl.h>                                            
  2 #include <stdio.h>                                            
  3 #include <unistd.h>                                           
  4                                                               
  5 void pwncollege(char** argv, char** envp){                    
  6     pid_t pid = fork();                                       
  7                                                               
  8     if(pid<0)                                                 
  9         printf("Error while forking! \n");                    
 10                                                               
 11     if(pid==0){                                               
 12         chdir("/tmp/racuzo");                                 
 13         int f = open("ftssxb",O_RDWR);                        
 14         dup2(f,STDIN_FILENO);                                 
 15         execlp("/challenge/embryoio_level84","embryoio_level84",NULL); 
 16                                                               
 17     }else waitpid(pid);                                       
 18 }                                                             
 19                                                               
 20 void main(int argc, char** argv, char** envp){                
 21     pwncollege(argv, envp);                                   
 22 } 
```
    mkdir /tmp/racuzo
    touch /tmp/racuzo/ftssxb
    cd ~
    gcc -o s s.c
    ./s

Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that input is redirected from a specific file path : ftssxb
- the challenge will check that it is running in a specific current working directory : /tmp/racuzo

## 85

```c
  1 #include <fcntl.h>  
  2 #include <stdio.h>  
  3 #include <unistd.h>                                                   
  4                     
  5 void pwncollege(char** argv, char** envp){                            
  6     pid_t pid = fork();                                               
  7                     
  8     if(pid<0)       
  9         printf("Error while forking! \n");                            
 10                     
 11     if(pid==0){     
 12         chdir("/tmp/kuxzlq");                                         
 13         execlp("/challenge/embryoio_level85","embryoio_level85",NULL);
 14         chdir("~"); 
 15         sleep(1000);  
 16                     
 17     }else waitpid(pid);
 18 }                   
 19                     
 20 void main(int argc, char** argv, char** envp){                        
 21     pwncollege(argv, envp);
 22 } 
```
    mkdir /tmp/kuxzlq
    cd ~
    gcc -o s s.c
    ./s

Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that it is running in a specific current working directory : /tmp/kuxzlq
- the challenge will check to make sure that the parent's parent CWD to be different than the challenge's CWD

## 86 - 87
bash script to run the challenge and use python for calculations

## 88
```sh
  1 #!/bin/bash
  2 /tmp/psxuhn        
```
ln -s /challenge/em... /tmp/ps...

## 89
```sh
  1 #!/bin/bash
  2 kutyuy   
```
ls -s /ch.../em...89 kut...
export PATH=$PATH:.
Task:
- the challenge checks for a specific parent process : shellscript
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 0:kutyuy

## 91

    mkfifo my_pipe

```sh
  1 #!/bin/bash
  2 /challenge/embryoio_level91 > my_pipe 
```
    # open with cat from another terminal
    cat my_pipe

Task:
- the challenge checks for a specific parent process : shellscript
- the challenge will make sure that stdout is a redirected from fifo

## 92 

```sh
#!/bin/bash
/challenge/embryoio_level92 < in_pipe > out_pipe
```
    mkfifo in_pipe
    mkfifo out_pipe
    [terminal 1] echo "psw" > in_pipe
    [terminal 2] ./script.sh 
    [terminal 3] cat out_pipe

Task:
- the challenge checks for a specific parent process : shellscript
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will check for a hardcoded password over stdin : jheroibv

```
shellscript -> /challenge/embryoio_level92 < in_p
echo "tfsxnkub" > in_p | ./s.sh > out_p | cat out_p
```

## 93
- the challenge checks for a specific parent process : shellscript
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will force the parent process to solve a number of arithmetic problems : 1
- the challenge will use the following arithmetic operations in its arithmetic problems : +*
- the complexity (in terms of nested expressions) of the arithmetic problems : 1

```sh
s.sh -> /challenge/embryoio_level93 < in_p
cat > in_p | ./s.sh > out_p | cat out_p
```

## 94
```sh
1 #!/bin/bash
2            
3 exec 303<> f303 # creating a file descriptor 303 from file f303 which has the password inside                 
4            
5 /challenge/embryoio_level94 <&303 # redirecting stdin from fd 303
6            
7 exec 303>&-   # closing fd 303
```
Task: 
- the challenge checks for a specific parent process : shellscript
- the challenge will take input on a specific file descriptor : 303
- the challenge will check for a hardcoded password over stdin : fjnvdylk

## 95
```sh
/challenge/embryoio_level95 <&2
```
TasK:
- the challenge checks for a specific parent process : shellscript
- the challenge will take input on a specific file descriptor : 2
- the challenge will check for a hardcoded password over stdin : praegoxs

## 99
```py
1 import subprocess  
2 subprocess.run(["/challenge/embryoio_level99"])  
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will force the parent process to solve a number of arithmetic problems : 1
- the challenge will use the following arithmetic operations in its arithmetic problems : +*
- the complexity (in terms of nested expressions) of the arithmetic problems : 1

## 100
da rifare con script

## 101

    ln -s /challenge/embryoio_level101 /tmp/htjwkx
```py
import subprocess 
subprocess.run(["/tmp/htjwkx"]) 
```      
- the challenge checks for a specific parent process : python
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 0:/tmp/htjwkx

## 102

    ln -s /challenge/embryoio_level102 ywdkvt
    export PATH=$PATH:.
```py
  1 import subprocess
  2 subprocess.run("ywdkvt"])   
```      
- the challenge checks for a specific parent process : python
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 0:ywdkvt

## 103
```py
  1 import subprocess                   
  2 import pwn                          
  3 import os                           
  4 pin = os.open("in_pipe",os.O_RDWR)  
  5  
  6 p1 = pwn.process(["cat","-"],stdout=pin)
  7 p1.sendline(b'pztwdmts')
  8  
  9 p2 = pwn.process(["/challenge/embryoio_level103"],stdin=pin)
 10 p2.interactive()
 11  
 12 pin.close()     
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will check for a hardcoded password over stdin : pztwdmts

## 104
```py
  1 import subprocess                       
  2 import pwn
  3 import os 
  4 pout = os.open("in_pipe",os.O_RDWR)     
  5     
  6 pin = os.open("in_pipe",os.O_WRONLY)    
  7     
  8 p2 = pwn.process(["/challenge/embryoio_level104"],stdout=pin)
  9 p1 = pwn.process(["cat","-"],stdin=pout)
 10 p1.interactive()               
 11  
 12 pin.close()
 13 pout.close()    
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will make sure that stdout is a redirected from fifo

## 105
```py
  1 import subprocess                 
  2 import pwn                        
  3 import os                         
  4 p1out = os.open("in_pipe",os.O_RDWR)
  5 p1in = os.open("in_pipe",os.O_WRONLY)
  6  
  7 p2out = os.open("out_pipe",os.O_RDWR)
  8 p2in = os.open("out_pipe",os.O_WRONLY)
  9  
 10 p1 = pwn.process(["cat","-"],stdout=p1in)
 11 p1.sendline(b'kqtxhpnf')
 12  
 13 p2 = pwn.process(["/challenge/embryoio_level105"],stdin=p1out ,stdout=p2in)
 14 p3 = pwn.process(["cat","-"],stdin=p2out)
 15 p3.interactive()
 16  
 17 p1in.close()
 18 p2in.close()
 19 p2out.close()
 20 p1out.close()     
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will check for a hardcoded password over stdin : kqtxhpnf

## 109
```py
1 import subprocess
2  
3 p = subprocess.Popen(["/challenge/embryoio_level109"])
4 p.wait()
```

## 110
same as 109 send signal from another terminal

    kill -SIGUSR2 <pid>

## 111
same as 110

## 112-113
did with python terminal

## 114
```c
  1 #include <fcntl.h>                
  2 #include <stdio.h>
  3 #include <unistd.h>
  4  
  5 void pwncollege(char** argv, char** envp){
  6     pid_t pid = fork();
  7  
  8     if(pid<0)
  9         printf("Error while forking! \n");
 10  
 11     if(pid==0){
 12         execlp("/tmp/wpoefa","/tmp/wpoefa",NULL);
 13  
 14     }else waitpid(pid);
 15 }
 16  
 17 void main(int argc, char** argv, char** envp){
 18     pwncollege(argv, envp);
 19 }
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 0:/tmp/wpoefa

## 115
same as 114 with

    export PATH=$PATH:.

Task:
- the challenge checks for a specific parent process : binary
- the challenge will check that argv[NUM] holds value VALUE (listed to the right as NUM:VALUE) : 0:xoxlle

## 118
used 3 terminals

terminal 1

    mkfifo in_pipe 
    mkfifo out_pipe
    echo "password" > in_pipe

terminal 2

    ./s.out < in_pipe > out_pipe

terminal 3

    cat out_pipe

```sh
echo "cpkzuebb" > in_p | ./c.out < in_p > out_p | cat out_p
```

Task:
- the challenge checks for a specific parent process : binary
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will check for a hardcoded password over stdin : qcrutuch
  
## 119
Create 2 FIFOs (named pipe) `mkfifo in_pipe` e `mkfifo out_pipe`

```c
#include <fcntl.h>                                             
#include <stdio.h>
#include <unistd.h>
 
void pwncollege(char** argv, char** envp){
    pid_t f_pid = fork();
 
    if(f_pid<0)
         printf("Error while forking! \n");
  
    if(f_pid==0){
        // file descriptors for in_pie and out_pipe
        int f_in = open("in_pipe",O_RDWR);
        int f_out = open("out_pipe",O_RDWR); 
  
        pid_t s_pid = fork();
  
        if(s_pid != 0){ // creating 2 processes challenge as parent and cat out_pipe as child
            dup2(f_in,0);
            dup2(f_out,1);
            execlp("/challenge/embryoio_level119","/challenge/embryoio_level119",NULL);
             // exec challenge with stdin = in_pipe and stdout = out_pipe
        }else if(s_pid == 0){
            dup2(f_out,0);
            execl("cat","cat","-",NULL);
            // exec cat to read from out_pipe
        }else waitpid(s_pid);  // waiting for s_pid
  
    }else waitpid(f_pid); // waiting for f_pid 
}
  
void main(int argc, char** argv, char** envp){
    pwncollege(argv, envp);
}
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will force the parent process to solve a number of arithmetic problems : 1
- the challenge will use the following arithmetic operations in its arithmetic problems : +*
- the complexity (in terms of nested expressions) of the arithmetic problems : 1

## 120

```c
  1 #include <fcntl.h>
  2 #include <stdio.h>  
  3 #include <unistd.h>     
  4   
  5 void pwncollege(char** argv, char** envp){
  6     pid_t f_pid = fork();
  7         
  8     if(f_pid<0)
  9         printf("Error while forking!\n");
 10  
 11     if(f_pid==0){
 12         int f_in = open("in_pipe",O_RDWR);
 13  
 14         dup2(f_in,16);
 15         execlp("/challenge/embryoio_level120","/challenge/embryoio_level120",NULL);
 16  
 17     }else waitpid(f_pid);
 18 }     
 19  
 20 void main(int argc, char** argv, char** envp){
 21     pwncollege(argv, envp);   
 22 } 
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge will take input on a specific file descriptor : 16
- the challenge will check for a hardcoded password over stdin : uefymrwe

## 121
```c
  1 #include <fcntl.h>
  2 #include <stdio.h>  
  3 #include <unistd.h>     
  4   
  5 void pwncollege(char** argv, char** envp){
  6     pid_t f_pid = fork();
  7         
  8     if(f_pid<0)
  9         printf("Error while forking!\n");
 10  
 11     if(f_pid==0){
 12         int f_in = open("in_pipe",O_RDWR);
 13         dup2(f_in,2);        
 14         execlp("/challenge/embryoio_level121","/challenge/embryoio_level121",NULL);
 15  
 16     }else waitpid(f_pid);
 17 }     
 18  
 19 void main(int argc, char** argv, char** envp){
 20     pwncollege(argv, envp);   
 21 } 
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge will take input on a specific file descriptor : 2
- the challenge will check for a hardcoded password over stdin : bctxddpj

## 123
same as 122

Alternative way
```c
#include <fcntl.h>
#include <stdio.h>  
#include <unistd.h>    
#include <signal.h>
#include <stdlib.h>
#include <sys/wait.h>

void pwncollege(char** argv, char** envp){
    pid_t pid = fork();    
    
    if(pid == 0){
        dup2(0,1);
        char *proc = "/challenge/embryoio_level122";
        execlp(proc,proc,NULL);
    }else{
        wait(NULL);         
    }
    
}     
    
void main(int argc, char** argv, char** envp){
    pwncollege(argv, envp);   
}
```
```
./s.out and enter the password
```
## 123
```
./s.out
from another terminal exec -> kill -SIG... pid
```

## 127
run script from sh file

```sh
1 #!/bin/bash                                                      
2 /challenge/embryoio_level127
```
Copy sigals array
```py
import subprocess
import signal  
       
sigs = ['SIGINT', 'SIGINT', 'SIGUSR1', 'SIGINT', 'SIGHUP', 'SIGUS    R2', 'SIGUSR2', 'SIGABRT', 'SIGABRT', 'SIGHUP', 'SIGHUP', 'SIGUSR    1', 'SIGABRT', 'SIGABRT', 'SIGUSR2', 'SIGUSR2', 'SIGUSR2', 'SIGUS    R1', 'SIGUSR1', 'SIGHUP', 'SIGINT', 'SIGUSR1', 'SIGINT', 'SIGUSR2    ', 'SIGHUP', 'SIGINT', 'SIGINT', 'SIGHUP', 'SIGHUP', 'SIGHUP', 'S    IGUSR2', 'SIGUSR1', 'SIGABRT', 'SIGABRT', 'SIGUSR1', 'SIGINT', 'S    IGUSR1', 'SIGHUP', 'SIGUSR2', 'SIGUSR1', 'SIGHUP', 'SIGUSR2', 'SI    GABRT', 'SIGUSR1', 'SIGABRT', 'SIGHUP', 'SIGUSR1', 'SIGUSR1', 'SI    GUSR1', 'SIGUSR2']
       
pid = "15435"                                                    
       
for sig in sigs:
    subprocess.run(["kill","-"+sig,pid])
```
Task:
- the challenge checks for a specific parent process : shellscript
- the challenge will require the parent to send number of signals : 50

## 128 
same as 127

## 129

    cat | /challenge/em...| cat

```py
  1 from pwn import *              
  2                                
  3 p = process(["b.sh"])          
  4 ch_str = "Please send the solution for: "
  5 line = p.recvuntil(b"[TEST] CHALLENGE!" )
  6 while True:                    
  7     line = p.recv().decode()   
  8     print("my script: ",line)  
  9     if ch_str in line:         
 10         line = line.split(':')[1].strip()
 11         print(line)            
 12         res = eval(line)       
 13         tosend = f"{str(res)}\n"
 14         p.send(tosend.encode())
 15     if "flag" in line:         
 16         print(line)            
 17         break                  
 18                                
 19 p.interactive() 
```
Task:
- the challenge checks for a specific parent process : shellscript
- the challenge checks for a specific process at the other end of stdin : cat
- the challenge checks for a specific process at the other end of stdout : cat
- the challenge will force the parent process to solve a number of arithmetic problems : 50
- the challenge will use the following arithmetic operations in its arithmetic problems : +*&^%|
- the complexity (in terms of nested expressions) of the arithmetic problems : 5

## 130

```py
from pwn import *                 
                                  
p = process(["/challenge/embryoio_level130"])       
ch_str = "Please send the solution for: "
line = p.recvuntil(b"[TEST] CHALLENGE!" )
while True:                       
   line = p.recv().decode()      
   print("my script: ",line)     
   if ch_str in line:            
        line = line.split(':')[1].strip()
        print(line)               
        res = eval(line)          
        tosend = f"{str(res)}\n"  
        p.send(tosend.encode())   
    if "flag" in line:            
        print(line)               
        break                     
                                  
p.interactive()                   
```
Task:
- the challenge checks for a specific parent process : python
- the challenge will force the parent process to solve a number of arithmetic problems : 50
- the challenge will use the following arithmetic operations in its arithmetic problems : +*&^%|
- the complexity (in terms of nested expressions) of the arithmetic problems : 5
  
## 131 
same as 130

## 132 - 133
same as 127


## 134
```py
import subprocess, os, fcntl

r1,w1 = os.pipe()
r2,w2 = os.pipe()

c1 = subprocess.Popen(["cat"],stdin=subprocess.PIPE,stdout=w1)
p = subprocess.Popen(["/challenge/embryoio_level134"],stdin=r1,stdout=w2)
c2 = subprocess.Popen(["cat"],stdin=r2,stdout=subprocess.PIPE)

for i in range(50):
   line = ''
   while True:
      line = c2.stdout.readline().decode()
      if "CHALLENGE" in line or line == "":
         break

   print(line)
   
   cmd = line.split(':')[1].strip()
   print(cmd)
   
   res = eval(cmd)
   print(res)

   c1.stdin.write(b"%d\n"%res)
   c1.stdin.flush()

while True:
   line = c2.stdout.readline().decode()
   if "pwn.college{" in line or line == "":
      print(line)
      break
```
Task:
- the challenge checks for a specific parent process : python
- the challenge checks for a specific process at the other end of stdin : cat
- the challenge checks for a specific process at the other end of stdout : cat
- the challenge will force the parent process to solve a number of arithmetic problems : 50
- the challenge will use the following arithmetic operations in its arithmetic problems : +*&^%|
- the complexity (in terms of nested expressions) of the arithmetic problems : 5

## 135 - 136
same as 130

## 137 - 138
same as 127

## 139
```c
#include <fcntl.h>
#include <stdio.h>  
#include <unistd.h>    
#include <signal.h>
#include <stdlib.h>

void pwncollege(char** argv, char** envp){
    pid_t pid = fork();    
    if(pid<0)
        printf("Fork error\n");

    if(!pid){
        char *proc = "/challenge/embryoio_level139";
        execve(proc,NULL,NULL);
    }else{
        wait(pid);         
    }
    
}     
    
void main(int argc, char** argv, char** envp){
    pwncollege(argv, envp);   
}
```
```sh
#!/bin/bash
cat - | ./s.out | cat -
```
```py
from pwn import *                 
p = process(["./b.sh"])       
ch_str = "Please send the solution for: "
line = p.recvuntil(b"[TEST] CHALLENGE!" )

while True:                       
     line = p.recv().decode()      
     print("my script: ",line)     
     if ch_str in line:            
        line = line.split(':')[1].strip()
        print(line)               
        res = eval(line)          
        tosend = f"{str(res)}\n"  
        p.send(tosend.encode())   
     if "flag" in line:
        print(line)               
        break                     
                                  
p.interactive() 
```
Task:
- the challenge checks for a specific parent process : binary
- the challenge checks for a specific process at the other end of stdin : cat
- the challenge checks for a specific process at the other end of stdout : cat
- the challenge will force the parent process to solve a number of arithmetic problems : 50
- the challenge will use the following arithmetic operations in its arithmetic problems : +*&^%|
- the complexity (in terms of nested expressions) of the arithmetic problems : 5
  
## 140
```sh
1 #!/bin/bash   
2 exec 4<>/dev/tcp/localhost/1560
3  
4 while read -u 4 line
5 do
6     echo "$line"
7     if [[ $line == *"CHALLENGE! Please send the solution for:"* ]]
8     then
9         cmd=${line:48}
10         sol=$(python -c "print(${cmd})")
11         echo $sol >&4
12     fi
13 done
 ```
Task:
- the challenge checks for a specific (network) client process : shellscript
- the challenge will listen for input on a TCP port : 1560
- the challenge will force the parent process to solve a number of arithmetic problems : 5
- the challenge will use the following arithmetic operations in its arithmetic problems : +*%
- the complexity (in terms of nested expressions) of the arithmetic problems : 3

## 141
```py
import subprocess                 
import socket                     
                                  
                                  
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:     
    s.connect(("localhost",1360)) 
    data = s.recv(2048).decode('utf-8')
                                  
    while len(data)>0:            
                                   
         lines = data.split('\n')  
                                   
         count = 0                 
         for line in lines:        
             count += 1            
             if "CHALLENGE" in line:
                 cmd = line.split(':')[1].strip()
                 print("Command:",cmd) 
                 cal = subprocess.Popen(["python","-c","print("+cmd+")"],stdout=subprocess.PIPE) 
                 cal.wait()        
                 result = cal.stdout.read().decode('utf-8')
                                   
                 tosend = f"{str(result)}"
                 print("Result:",tosend)
                 s.sendall(tosend.encode())
             if "pwn.college" in line:
                 print("FLAG:",line)                              
                                   
                                   
         data = s.recv(2048).decode('utf-8')
         if count < len(lines)-1:  
             data = lines[-1] + data
```
Task:
- the challenge checks for a specific (network) client process : python
- the challenge will listen for input on a TCP port : 1360
- the challenge will force the parent process to solve a number of arithmetic problems : 5
- the challenge will use the following arithmetic operations in its arithmetic problems : +*%
- the complexity (in terms of nested expressions) of the arithmetic problems : 3

## 142
```c
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/wait.h>


#define PORT 1866

int pwncollege(){
    int sfd = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in srvaddr;
    srvaddr.sin_family = AF_INET;
    srvaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    srvaddr.sin_port = htons(PORT);

    connect(sfd, (const struct sockaddr *)&srvaddr, sizeof(srvaddr));
    char buffer[1024];
    char* str = "[TEST] CHALLENGE";
    int num = 1;
    while(num > 0){
        num = read(sfd, buffer, sizeof(buffer));
        write(1, buffer, num);
        if(strncmp(buffer, str, 15) == 0){
            pid_t pid = fork();
            if(pid == 0){
                char problem[200] = "print(";
                strcpy(&problem[6], &buffer[48]);
                char end[3] = ")\0";
                strcpy(&problem[num - 42], &end[0]);
                dup2(sfd, STDOUT_FILENO);
                execl("/usr/bin/python", "/usr/bin/python", "-c", &problem, NULL);
            }
            else wait(NULL);
        }
    }
    close(sfd);
}

int main(){
        pwncollege();
}
```
Task:
- the challenge checks for a specific (network) client process : binary
- the challenge will listen for input on a TCP port : 1866
- the challenge will force the parent process to solve a number of arithmetic problems : 5
- the challenge will use the following arithmetic operations in its arithmetic problems : +*%
- the complexity (in terms of nested expressions) of the arithmetic problems : 3

```c
#include <arpa/inet.h> // inet_addr()
#include <netdb.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h> // bzero()
#include <sys/socket.h>
#include <fcntl.h>
#include <sys/select.h>
#include <unistd.h> // read(), write(), close()
#define MAX 1024
#define PORT 1866
#define SA struct sockaddr



void pwncollege(int connfd)
{
    char buff[MAX]; 
    int n; 
    // infinite loop for chat 
    for (;;) { 
        bzero(buff, MAX); 
        int count = 1;

        while( count > 0){
            count = read(connfd, buff, sizeof(buff)); /* there was data to read */
            printf("%s", buff);
            bzero(buff, MAX); 
            
        }
        bzero(buff, MAX); 
        // printf("reading\n");
        n = 0; 
        // copy server message in the buffer 
        while ((buff[n++] = getchar()) != '\n'); 

        // printf("read: %s\n",buff);
        
        // and send that buffer to client 
        write(connfd, buff, sizeof(buff)); 
   
        // if msg contains "Exit" then server exit and chat ended. 
        if (strncmp("exit", buff, 4) == 0) { 
            printf("Server Exit...\n"); 
            break; 
        } 
    } 
}
 
int main()
{
    int sockfd, connfd;
    struct sockaddr_in servaddr, cli;
 
    // socket create and verification
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("socket creation failed...\n");
        exit(0);
    }
    else
        printf("Socket successfully created..\n");

    bzero(&servaddr, sizeof(servaddr));
 
    // assign IP, PORT
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    servaddr.sin_port = htons(PORT);
 
    // connect the client socket to server socket
    if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr))
        != 0) {
        printf("connection with the server failed...\n");
        exit(0);
    }
    else
        printf("connected to the server..\n");
 
    // function for chat
    pwncollege(sockfd);
 
    // close the socket
    close(sockfd);
}
```