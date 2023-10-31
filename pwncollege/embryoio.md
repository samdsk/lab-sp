# Pwn college Embryoio  

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
 

## lvl 19

~~~py
import subprocess; \
file = open("/tmp/jkibzf","r"); \
subprocess.run(["/challenge/embryoio_level19"],stdin=file);
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
 

## lvl 29

~~~c
#include <stdio.h>

void pwncollege(){ 
    int pid = fork();
    if(pid<0)
        printf("Error! \n");
    

    if(pid==0)
        execve("/challenge/embryoio_level29");        

    else waitpid(pid);
}

int main(){
    pwncollege();
    return 0;
}
~~~

## lvl 30
same as 29

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
        
void pwncollege(char** argv, char** envp){
    int pid = fork();
        
    if(pid<0)
        printf("Error! \n");
         
    if(pid==0){
        char *prog = "/challenge/embryoio_level32";
        char *args[] = {prog};
        char *env[] = {"xwzwxd=rsaqanygyj"};
                                                                                                    
        execve("/challenge/embryoio_level32", NULL,envp);
        
    }else waitpid(pid);
}       
        
int main(int argc, char** argv, char** envp){
    pwncollege(argv, envp); 
    return 0;
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
    just put them inside a sh file

## lvl 48
~~~py
import subprocess; \ 
p1 = subprocess.Popen(["/challenge/embryoio_level48"], stdout=subprocess.PIPE); \
subprocess.run(["cat"],stdin=p1.stdout);

# use subprecess.PIPE to pipe stdin and stdout between subprocs
~~~
 

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
