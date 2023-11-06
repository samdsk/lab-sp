.intel_syntax noprefix
.global _start
.section .text
_start:
    
    mov rax,1
    mov rdi,1
    mov rsi, 0x216e7720756f592f
    shr rsi,0x8
    mov rdx, 10
    syscall
    
