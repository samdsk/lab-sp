#!/bin/sh
for f in $*
do
    if [ -f $f -a ! -x $f ]
    then
        case $f in
        core)
            echo "$f: a core dumb file"
            ;;
        *.c)
            echo "$f: a C program"
            ;;
        *.cpp|*.cc|*.cxx)
            echo "$f: a C++ program"
            ;;
        *.txt)
            echo "$f: a text file"
            ;;
        *.pl)
            echo "$f: a PERL script"
            ;;
        *.html|*.htm)
            echo "$f: a web document"
            ;;
        *)
            echo "$f: appears to be "`file -b $f`
            ;;
        esac
    fi
done