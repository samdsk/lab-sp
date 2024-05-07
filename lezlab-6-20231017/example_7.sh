#!/bin/bash
while [ ! -s input.txt ]
do
    echo waiting...
    sleep 5
done
echo input.txt is ready