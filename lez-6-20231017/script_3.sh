#!/bin/bash
echo "what is your name"
read USER_NAME # legge
echo "Hello $USER_NAME"
echo "i will create you a file called ${USER_NAME}_file"
touch "${USER_NAME}_file"