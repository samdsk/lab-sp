#!/bin/bash

echo "*** DISABLING MaxAuthTries ***"
sed -i 's/MaxAuthTries .*/MaxAuthTries 2147483647/g' /etc/ssh/sshd_config
