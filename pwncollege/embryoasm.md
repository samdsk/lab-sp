# Pwm Embryoams
~~~sh
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
 12  
 13 echo -e "compiling assembly from ${RED}${file}${NC}"
 14 gcc -nostdlib -static -o $out $file
 15 echo -e "copying text section binary to ${RED}${sol}"
 16 objcopy --dump-section .text=$sol $out
 17 echo -e "${GREEN}DONE!"
~~~

## lvl 1
~~~s
  1 .intel_syntax noprefix
  2 .global _start    
  3 .section .text    
  4 _start:           
  5     mov rdi,0x1337 # your reg
~~~
assign address to register as immediate value

    gcc -nostdlib -static -o outfile file.s
    objcopy --dump-section .text=sol.txt binaryfile.asm

## lvl 3
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:    
  5    mov rbx,rdx # moving b to rbx cz mul uses rdx and rax regs
  6    mov rdx,rdi # moving m to rdx
  7    mov rax,rsi # moving x to rax
  8    mul rdx # mul m*x    
  9    add rax,rbx # mx + b
~~~

## lvl 4
~~~s
  1 .intel_syntax noprefix
  2 .global _start 
  3 .section .text 
  4 _start:    
  5    # division        
  6     mov rax,rdi # moving dividen to rax
  7     div rsi  # quotient is at rax and in rdx remainder
~~~

## lvl 5
~~~s
  1 .intel_syntax noprefix     
  2 .global _start
  3 .section .text
  4 _start: # division and take the remainder
  5     mov rax,rdi
  6     div rsi
  7     mov rax,rdx # moving remainder
~~~
## lvl 6
~~~s
  1 .intel_syntax noprefix   
  2 .global _start
  3 .section .text
  4 _start: # exec op modulo using only mov command
  5     mov rax,0
  6     mov rbx,0
  7     mov al,dil
  8     mov bx,si
~~~
## lvl 7
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:   
  5 # shifting 4 byte to right         
  6 mov rax,0 # needs to clear the register (set all bits to 0)
  7 shr rdi,32 # shifting 32 bits to right
  8 mov al,dil # copying only last 8bits to rax
~~~
Task: Set `rax` to the 5th least significant byte of `rdi`

## lvl 8
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:   
  6 and rax,0  
  7 or  rax,rdi
  8 and rax,rsi
~~~
Task: without using mov or xchg, perform and between rdi and rsi and put the result in rax

## lvl 9
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:  
  5          
  6 xor rax,rax
  7 or  rax,1         
  8 and rdi,1
  9 xor rax,rdi
~~~
Task: Using only the following instructions: and, or, xor

Implement the following logic:

    if x is even then
      y = 1
    else
      y = 0
    where:
    x = rdi
    y = rax

## lvl 10
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:       
  5               
  6 mov rax,[0x404000]
  7 add qword ptr [0x404000],0x1337    
~~~
Task: 
1. Place the value stored at 0x404000 into rax
2. Increment the value stored at the address 0x404000 by 0x1337. Make sure the value in rax is the original value stored at 0x404000 and make sure
that [0x404000] now has the incremented value

## lvl 11
~~~s
  1 .intel_syntax noprefix
  2 .global _start    
  3 .section .text    
  4 _start:           
  5                   
  6 mov al,[0x404000] 
  7 mov bx,[0x404000] 
  8 mov ecx, [0x404000]
  9 mov rdx,[0x404000]   
~~~
Task: 
1) Set rax to the byte at 0x404000
2) Set rbx to the word at 0x404000
3) Set rcx to the double word at 0x404000
4) Set rdx to the quad word at 0x404000
  
## lvl 12
~~~s
  1 .intel_syntax noprefix 
  2 .global _start         
  3 .section .text         
  4 _start:                
  5 mov rax, 0xdeadbeef00001337
  6 mov qword ptr [rdi],rax
  7 mov rax,0xc0ffee0000   
  8 mov qword ptr [rsi],rax 
~~~
Task: 
1. set [rdi] = 0xdeadbeef00001337
2. set [rsi] = 0xc0ffee0000
Hint: it may require some tricks to assign a big constant to a dereferenced register. Try setting
a register to the constant then assigning that register to the derefed register.

## lvl 13
~~~s
  1 .intel_syntax noprefix
  2 .global _start 
  3 .section .text 
  4 _start:      
  5              
  6 add rax,[rdi]
  7 add rax,[rdi+8]
  8 mov [rsi],rax  
~~~
Task: 
1. load two consecutive quad words from the address stored in rdi
2. calculate the sum of the previous steps quad words.
3. store the sum at the address in rsi
   
## lvl 14
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start: 
  5 pop rax 
  6 sub rax,rdi
  7 push rax      
~~~
Task: Replace the top value of the stack with (substract stack value - rdi).
   
## lvl 15
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:
  5       
  6 push rdi
  7 push rsi
  8 pop rdi
  9 pop rsi                      
~~~
Task: Using only following instructions: push, pop. Swap values in rdi and rsi.

## lvl 16
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start:
  5    
  6 mov rax,[rsp]
  7 mov rdx,[rsp+8]
  8 add rax,rdx
  9 mov rdx,[rsp+16]
 10 add rax,rdx
 11 mov rdx,[rsp+24]
 12 add rax,rdx
 13 shr rax,2
 14 mov [rsp-8], rax
~~~
Task: Without using pop please calculate the average of 4 consecutive quad words stored on the stack. Store the average on the top of the stack.

## lvl 17
~~~s
1 .intel_syntax noprefix                                                                              
  2 .global _start
  3 .section .text
  4 _start:
  5  
  6 jmp JUMP
  #...
  7 nop # for byte*times
  #...
 88 JUMP:
 89     mov rdi,[rsp]
 90     mov rcx,0x403000
 91     jmp rcx                          
~~~
Task: Create a two jump trampoline:
1. Make the first instruction in your code a jmp
2. Make that jmp a relative jump to 0x51 bytes from its current position
3. At 0x51 write the following code:
4. Place the top value on the stack into register rdi
5. jmp to the absolute address 0x403000

## lvl 18
~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start: 
  5         
  6 mov ebx,[rdi]
  7         
  8 cmp ebx,0x7f454c46
  9 jne else_if
 10         
 11 mov ecx,[rdi+4]
 12 add eax,ecx
 13         
 14 mov ecx,[rdi+8]
 15 add eax,ecx
 16         
 17 mov ecx,[rdi+12]
 18 add eax,ecx
 19         
 20 jmp done
 21         
 22 else_if:
 23 cmp ebx,0x00005A4D
 24 jne else
 25         
 26 mov eax,[rdi+4]
 27 mov ecx,[rdi+8]
 28         
 29 sub eax,ecx
 30         
 31 mov ecx,[rdi+12]
 32 sub eax,ecx
 33         
 34 jmp done
 35         
 36 else:   
 37         
 38 mov  eax,[rdi+4]
 39 mov  ecx,[rdi+8]
 40 imul eax,ecx
 41     
 42 mov  ecx,[rdi+12]
 43 imul eax,ecx
 44     
 45 done:
~~~
Task: Create a if-else_if-else:

	if [x] is 0x7f454c46:
	y = [x+4] + [x+8] + [x+12]
	else if [x] is 0x00005A4D:
	y = [x+4] - [x+8] - [x+12]
	else:
	y = [x+4] * [x+8] * [x+12]

where: x = rdi, y = rax. Assume each dereferenced value is a signed dword. This means the values can start as a negative value at each memory position. A valid solution will use the following at least once: jmp (any variant), cmp

## lvl 19

~~~s
  1 .intel_syntax noprefix
  2 .global _start     
  3 .section .text     
  4 _start:            
  5                    
  6 cmp rdi,4          
  7 jl JUMPS           
  8 mov rdi,4          
  9 JUMPS:             
 10 jmp [rsi + rdi * 8] 
~~~

Task: implement the following logic: a switch statement

	if rdi is 0:
		jmp 0x403010
	else if rdi is 1:
		jmp 0x403105
	else if rdi is 2:
		jmp 0x40319e
	else if rdi is 3:
		jmp 0x40329f
	else:
		jmp 0x403371

Please do the above with the following constraints:
- assume rdi will NOT be negative
- use no more than 1 cmp instruction
- use no more than 3 jumps (of any variant)
- we will provide you with the number to 'switch' on in rdi.
- we will provide you with a jump table base address in rsi.

Here is an example table:
*    [0x404111] = 0x403010 (addrs will change)
*    [0x404119] = 0x403105
*    [0x404121] = 0x40319e
*    [0x404129] = 0x40329f
*    [0x404131] = 0x403371

## lvl 20

~~~s
  1 .intel_syntax noprefix 
  2 .global _start         
  3 .section .text         
  4 _start: 
  5 xor rax, rax           
  6 xor rcx, rcx           
  7         
  8 FOR:    
  9 cmp rcx,rsi
 10 jge EXIT
 11         
 12 mov rbx,[rdi + rcx * 8]
 13 add rax,rbx
 14 inc rcx 
 15 jmp FOR 
 16         
 17 EXIT:   
 18 idiv rsi  
~~~

Task: compute the average of n consecutive quad words, where:
* rdi = memory address of the 1st quad word
* rsi = n (amount to loop for)
* rax = average computed

## lvl 21

~~~s
  1 .intel_syntax noprefix
  2 .global _start
  3 .section .text
  4 _start: 
  5     
  6 xor rax,rax
  7 cmp rdi,0
  8 je END
  9     
 10 xor rcx,rcx
 11     
 12 WHILE:
 13     mov dl,[rdi + rcx]
 14     cmp dl,0
 15     je END
 16     inc rax
 17     inc rcx
 18     jmp WHILE
 19            
 20 END:  
~~~

Task: (While loop) Count the consecutive non-zero bytes in a contiguous region of memory, where:
* rdi = memory address of the 1st byte
* rax = number of consecutive non-zero bytes
* Additionally, if rdi = 0, then set rax = 0.

## lvl 22

~~~s
  1 .intel_syntax noprefix 
  2 .global _start      
  3 .section .text      
  4 _start:             
  5                     
  6 xor rax,rax         
  7 xor rdx,rdx         
  8                     
  9 IF_1:               
 10     cmp rdi,0       
 11     je END          
 12                     
 13 xor rcx,rcx         
 14                     
 15 WHILE:              
 16     mov bl, byte ptr [rdi + rcx]
 17     cmp bl,0        
 18     je END          
 19                     
 20     IF_2:       
 21       cmp bl,0x5a
 22       jg IF_2_END  
 23                     
 24       mov rax,0x403000 # store the addr of foo function
 25       push rdi # save the addr of while loop
 26       mov rdi,rbx # load in rdi current content of rbx as arg1 of foo function
 27       call rax # call foo function, returned value will be in RAX
 28       pop rdi 
 29       mov byte ptr [rdi + rcx], al # assigning returned value to original memory location
 30       inc rdx 
 31                     
 32     IF_2_END:  
 33       inc rcx    
 34       jmp WHILE  
 35                     
 36 END:                
 37   mov rax,rdx         
 38   ret   
~~~

Task:
~~~
  str_lower(src_addr):
      rax = 0
      if src_addr != 0:
          while [src_addr] != 0x00:
              if [src_addr] <= 0x5a:
                  [src_addr] = foo([src_addr])
                  rax += 1
              src_addr += 1
~~~
`foo` is provided at 0x403000. `foo` takes a single argument as a value

An important note is that `src_addr` is an address in memory (where the string is located) and `[src_addr]` refers to the byte that exists at `src_addr`.

Therefore, the function `foo` excepts a byte as its first argument, and returns a byte.

We will now run multiple tests on your code, here is an example run:
- (data) [0x404000] = {10 random bytes},
- rdi = 0x404000

## lvl 23

~~~s
  1 .intel_syntax noprefix 
  2 .global _start      
  3 .section .text      
  4 _start:             
  5                     
  6 mov rbp,rsp
  7 sub rsp,0x500 
  8  
  9 xor rbx,rbx # b = 0
 10 xor rcx,rcx # i = 0 counter
 11  
 12 FOR_1:
 13     cmp rcx,rsi # rsi is the second arg of function since func(s_adrr,size)
 14     jge FOR_1_END
 15     movb  dl, byte ptr [rdi + rcx]
 16     mov eax, dword ptr -0x400[rbp + rdx * 4]
 17     inc eax
 18     mov dword ptr -0x400[rbp + rdx * 4], eax
 19     inc rcx
 20     jmp FOR_1
 21  
 22 FOR_1_END:
 23  
 24 xor rcx,rcx # b = 0
 25 xor rbx,rbx
 26 xor rdx,rdx # max_frew = 0
 27 xor rax,rax # max_freq_byte = 0
 28  
 29 FOR_2:
 30     cmp rcx, 0xff
 31     jg FOR_2_END
 32     IF:
 33       mov ebx, dword ptr -0x400[rbp + rcx * 4]
 34       cmp edx,ebx
 35       jge IF_END
 36       mov edx,ebx
 37       mov rax,rcx
 38     IF_END:
 39       inc rcx
 40       jmp FOR_2
 41  
 42 FOR_2_END:
 43     mov rsp,rbp
 44     ret  
~~~

Task:
~~~
ost_common_byte(src_addr, size):
    b = 0
    i = 0
    for i <= size-1:
        curr_byte = [src_addr + i]
        [stack_base - curr_byte] += 1
    b = 0

    max_freq = 0
    max_freq_byte = 0
    for b <= 0xff:
        if [stack_base - b] > max_freq:
            max_freq = [stack_base - b]
            max_freq_byte = b

    return max_freq_byte
~~~
Assumptions:
- There will never be more than 0xffff of any byte
- The size will never be longer than 0xffff
- The list will have at least one element
Constraints:
- You must put the "counting list" on the stack
- You must restore the stack like in a normal function
- You cannot modify the data at src_addr

