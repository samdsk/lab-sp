#!/bin/bash
# print file last access and modification date
# stat command
stat_cmd=$(which stat)
# file to be verified
LIST=`ls $1`
echo $LIST

for file in $LIST
do
    if ([ -f "$1/$file"] || [ -d "$1/$file" ]); then
        mod_time=$($stat_cmd --format="%y" $1/$file)
        acc_time=$($stat_cmd --format="%x" $1/$file)
        echo "$1/$file last access is $acc_time, modification time is $mod_time"
    else
        echo "File $1/$file does not exist"
    fi
done