#!/bin/bash

STR="a"

prog_output=$(echo "$STR" | ./prog)
echo -e "${prog_output}\n"

while [[ "$prog_output"!=["You Win!"] ]] 
do
	echo -e "${prog_output} string length ${#STR}\n"
	STR="${STR}a"
	prog_output=$(echo "$STR" | ./prog)
done

echo -e "${prog_output} string length ${#STR}\n"

