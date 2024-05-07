#!/bin/bash
# print file size
# size command
stat_cmd=$(which stat)
# file to be verified
file=$1

if [ -f "$file" ]; then

    size=$($stat_cmd --format="%s" $file) # byte
    units="B"

    if [ "$size" -gt "1024" ]; then
        size=$(expr $size / 1024) # kilobytes
        units="KB"
    fi
    if [ "$size" -gt "1024" ]; then
        size=$(expr $size / 1024) # megabytes
        units="MB"
    fi
    if [ "$size" -gt "1024" ]; then
        size=$(expr $size / 1024) # gigabytes
        units="GB"
    fi
    if [ "$size" -gt "1024" ]; then
        size=$(expr $size / 1024) # terabytes
        units="TB"
    fi

    echo "$file size is $size $units"
else
    echo "File does not exist"
fi