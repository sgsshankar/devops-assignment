#!/usr/bin/python

"""
app.py - Program to execute command on Multiple Linux Servers

Dependency - cryptography, paramiko

Input:  list of hostnames
        command

Output: Stdout of the Command from each Servers

""" 

import sys, os, string, threading
import traceback
import paramiko # Great implementation of SSH in Python

uname = "root" # Connecting as root (Easy to test with Docker)
key = paramiko.RSAKey.from_private_key_file("./private.pem") # Same Private key for all the system

lock = threading.Lock()

"""
Executes command on the remote system and prints the output on the screen

Params : host, command
Output : Output of the command execution with details 

"""

def executeCommand(host, command):

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=uname, pkey = key)
        stdin, stdout, stderr = ssh.exec_command(command)
        stdin.flush()

        with lock:
            print("Host:"+host)
            print("\n"+stdout.readlines())
            print("\n"+stderr.readlines())
    
    except:
        print(traceback.format_exc())

    return;

def main():
    threads = []
    host =str(sys.argv[1])
    if(!host):
        print("usage: python app.py <List of hosts in comma separated>")
        sys.exit()
    command = input('Enter the command to execute: ')
    hosts = [i.strip() for i in host.split(',')]
    for h in hosts:
        t = threading.Thread(target=executeCommand, args=(h,command))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == "__main__":
    sys.exit(main())