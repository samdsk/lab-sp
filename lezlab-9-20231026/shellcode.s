.intel_syntax noprefix
.global _start
.section .text
_start:
mov rax, 59
lea rdi, [rip + binsh]
mov rsi, 0
mov rdx, 0
syscall
binsh:
.string "/bin/sh"