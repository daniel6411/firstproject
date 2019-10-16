#!/bin/bash
#add fix to exercise5-server1 here
steps:
1. Create Authentication SSH-Kegen Keys
   ssh-keygen -t rsa
2. Create .ssh Directory
   mkdir -p .ssh
3. Upload Generated Public Keys
   cat .ssh/id_rsa.pub | ssh server2 'cat >> .ssh/authorized_keys'
4. login to server2 
