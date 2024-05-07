# AbraWorm
_Corso di Sicurezza e Privatezza @ Unimi_

## Passaggi per l'utilizzo
_Testato su ubuntu_

* Installazione di docker e docker-compose https://docs.docker.com/engine/install/ubuntu/

* Con il comando `docker-compose up --force-recreate` vengono scaricate le immagini di openssh-server
(immagini minimali da circa 12MB). Vengono creati 2 container di nome _openssh-server-attacker_ e
_openssh-server-user_. Entrambi i container espongono la porta 2222 che viene rimappata sulla porta
dell'host 22 per openssh-server-user e 12345 per openssh-server-attacker. Ora la macchina dello
studente avrá due porte esposte 22 e 12345, si puó vedere con `netstat -tulpn | grep LISTEN`

```
teozoia@teozoia-blade:~/Desktop/abraworm/abraworm/worm$ netstat -tulpn | grep LISTEN
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -     
tcp        0      0 0.0.0.0:12345           0.0.0.0:*               LISTEN      -
...     
```          

* Come dichiarato all'interno del file _docker-compose.yaml_ al rispettivo container verrá montata la cartella
_user/config_ e _attacker/config_; da notare che in _user/config_ é presente il file _text.txt_ il quale contiene
la parola abracadabra.

* Per testare il funzionamento dei due container é possibile collegarsi al container user con
`ssh user@127.0.0.1` (password: password) e attacker con `ssh seed@127.0.0.1 -p 12345` (password: dees).

* É possibile eseguire il worm sulla propria macchina `python3 AbraWorm.py`. Se si vuole velocizzare il processo
é possibile togliere il `while` e fare in modo che le funzioni `get_password_list()` e `get_user_list()`
ritornino una lista fissata non lunga. Per usare il worm in modo verboso é necessario che `DEBUG=1`.

```
teozoia@teozoia-blade:~/Desktop/abraworm/abraworm/worm$ python3 AbraWorm.py 
user@127.0.0.1 -> adjfhfad
Exception catched: Authentication failed.
user@127.0.0.1 -> dhf931f
Exception catched: Authentication failed.
matteo@127.0.0.1 -> idhf
Exception catched: Authentication failed.
user@127.0.0.1 -> password
Connected user@127.0.0.1 -> password
[user@127.0.0.1] executing: ls
        stdout:['AbraWorm.py\n', 'logs\n', 'ssh_host_keys\n', 'sshd.pid\n', 'test.txt\n']
Target user@127.0.0.1 already infected
[user@127.0.0.1] executing: grep -ls abracadabra *
        stdout:['AbraWorm.py\n', 'test.txt\n']
Files of interest at the target: ['AbraWorm.py', 'test.txt']
Will now try to exfiltrate the files
Connected to exhiltration host
```

## Docker install
https://docs.docker.com/engine/install/ubuntu/

* `sudo apt-get remove docker docker-engine docker.io containerd runc`
* `sudo apt-get update`
* `sudo apt-get install ca-certificates curl gnupg lsb-release`
* `sudo mkdir -p /etc/apt/keyrings`
* `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`
* `echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null`
* `sudo apt-get update`
* `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin`
