.intel_syntax noprefix
.global _start
.section .text
_start:

mov rdx,5600
mov rsi,4000
add rsi,rdx
lea rdi,buffer
call TO_ASCII

lea rdi,buffer
mov rsi,rax
call Print

call EXIT


EXIT:
mov rax,60
mov rdi,0
syscall

Print: # (rdi = buffer, rsi = size)
mov r8,rdi
mov r9,rsi

mov rax,1
mov rdi,1
mov rsi,r8
mov rdx,r9
syscall

ret

# func to_ascii

TO_ASCII: # (rdi = buffer, rsi = number)
# prologue
push rbp
mov rbp, rsp
sub rsp, 50

xor rax,rax
mov rax,rsi
xor rcx,rcx

xor rbx,rbx
mov rbx,10

DIVID: # saving reminder in rbp
cmp rax,0
je REVERSE_INIT

xor rdx,rdx
div rbx
add dl,0x30
mov byte ptr [rbp+rcx], dl
inc rcx
jmp DIVID

REVERSE_INIT:
xor rbx,rbx
dec rcx
REVERSE: # storing in buffer ascii char in reverse order
cmp rcx,0
jl EXIT_TO_ASCII

mov dl, byte ptr [rbp+rcx]
mov byte ptr [rdi+rbx], dl
inc rbx
dec rcx
jmp REVERSE

EXIT_TO_ASCII:
inc rbx
mov byte ptr [rdi+rbx],0 # NULL char 0x0 = 0
mov byte ptr [rdi+rbx+1],10 # LINE FEED '\n' char 0xa = 10 questo toglie "%" da shell
mov rax,rbx

# epilogue
mov rsp,rbp
pop rbp
ret

.section .data
buffer: .space 100
