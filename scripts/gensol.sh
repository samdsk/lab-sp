#!/bin/bash                                                                             
# script for generating solution
# defining I/O files
file="a.s"
sol="sol.txt"
out="a.out"
    
# colored terminal
RED="\033[0;31m"
NC="\033[0m" 
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
    
echo -e "compiling assembly from ${RED}${file}${NC}"
gcc -z execstack -fno-stack-protector -nostdlib -static -o $out $file
echo -e "copying text section binary to ${RED}${sol}"
objcopy --dump-section .text=$sol $out
 
echo -e "${GREEN}#### DONE! ####"