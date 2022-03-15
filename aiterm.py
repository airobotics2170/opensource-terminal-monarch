import os
import time
print("AI Terminal version:2.2.1 stable")
while True:
    o = "sudo su"
    d = "exit"
    f = "hostname"
    ff = "cd downloads"
    ffff = "cd documents"
    q = "python3"
    w = "clear"
    t = "time"
    ls = "ls"
    help = "help"
    s = input("AI-term@localhost>")
    if s == o:
        print("Now root")
    elif s == d:
            break
    elif s == f:
        print("localhost")
    elif s == ff:
        os.chdir("C:\\Users\\alexh\\Downloads")
        print("Path: downloads")
    elif s == ffff:
        os.chdir("C:\\Users\\alexh\OneDrive\\Documents")
        print("Path: documents")
    elif s == q:
        os.system("python3")
    elif s == w:
        os.system("cls")
    elif s == t:
        curr = time.localtime(time.time())
        print("The time is:",curr)
    elif s == ls:
        os.system("dir")
    elif s == help:
        print("Commands for terminal: ")
        print("sudo su to change to root")
        print("exit to exit the terminal")
        print("hostname view hostname for ssh")
        print("cd downloads to go to downloads directory")
        print("python3 to program in python")
        print("clear to clear all output text")
        print("time to view time")
        print("ls to list all files in directory")