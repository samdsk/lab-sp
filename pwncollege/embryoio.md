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

void  
    int pid = fork();
    if(pid<0)
        printf("Error! \n");
    

    if(pid==0)
        execve("/challenge/embryoio_level29");        

    else waitpid(pid);
}

int main(){
     
    return 0;
}
~~~

## lvl 30
same as 29

## lvl 31
~~~c
#include <stdio.h>           
                             
void  
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
     
    return 0;                
}
~~~ 

## lvl 32

    export var=str

~~~c
#include <stdio.h>
        
void  
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
     
    return 0;
}       
~~~ 

 

## lvl 33

    echo "psw" > /tmp/file

~~~c
#include <stdio.h>      
      
void  
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
      
void  
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
      
void  
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
 