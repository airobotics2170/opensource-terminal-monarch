import os
import time
print("AI Terminal version:Monarch stable")
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
    up = "os.update --newest"
    dev_update = "os.update --dev check"
    update = "false"
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
        print("sudo su, to change to root")
        print("exit, to exit the terminal")
        print("hostname, view hostname for ssh")
        print("cd downloads, to go to downloads directory")
        print("python3, to program in python")
        print("clear, to clear all output text")
        print("time, to view time")
        print("ls, to list all files in directory")
        print("os.update --newest, to update to newest terminal")
        print("cd documents, to go to documents")
    elif s == up:
        if update == "true":
            print("updating ...")
            time.sleep(20)
            print("now updated to latest terminal.")
        else:
            print("no updates are avaliable for ai-terminal")
    elif s == dev_update:
        code = input("username: ")
        if code == "root":
            password = input("password: ")
            if password == "1418":
                print("Coming out update:")
                print("Bug fixes.")
                print("Faster response time.")
                print("New commands.")
                print("More help on how to use.")
