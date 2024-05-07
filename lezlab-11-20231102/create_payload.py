with open('payload','wb') as f: # 'wb' write bytes
    f.write(b'\x90'*80)
    f.write(b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII')
    
print("Payload created!")