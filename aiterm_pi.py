import os
import time
print("AI Terminal version:Monarch stable")
while True:
    o = "sudo su"
    d = "exit"
    f = "hostname"
    ff = "cd downloads"
    ffff = "cd desktop"
    q = "python3"
    w = "clear"
    t = "time"
    ls = "ls"
    help = "help"
    up = "os.update --newest"
    dev_update = "os.update --dev check"
    update = "false"
    backup = "backup -list"
    backupd = "backup -download"
    documents = "cd documents"
    nano = "nano"
    user = "$USER"
    eject = "eject"
    bsod = "bsod-run"
    mkdir = "mkdir new"
    mkdir1 = "mkdir home"
    mkdir2 = "mkdir files"
    s = input("AI-term@localhost>")
    if s == o:
        print("Now root")
    elif s == d:
            break
    elif s == f:
        os.system("hostname")
    elif s == ff:
        os.chdir("/Users/username/Downloads")
        print("Path: downloads")
    elif s == ffff:
        os.chdir("/Users/username/Desktop")
        print("Path: desktop")
    elif s == q:
        os.system("python3")
    elif s == w:
        os.system("clear")
    elif s == t:
        curr = time.localtime(time.time())
        print("The time is:",curr)
    elif s == ls:
        os.system("ls")
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
        print("nano, to edit and create files")
        print("cd desktop, to go to desktop directory")
        print("mkdir new, to make new directory called new")
        print("mkdir home, to make new directory called home")
        print("mkdir files, to make new directory called files")
        print("eject, to eject drive")
        print("bsod-run, to run test bsod")
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
    elif s == backup:
    	print("aiterm.conf")
    	print("aiterm.json")
    	print("terminal.conf")
    	print("ssh.pub")
    	print("ssh.key")
    	print("settings.term")
    	print("config.py")
    	print("AI-term.exe")
    elif s == backupd:
    	print("Downloading all files ...")
    	time.sleep(10)
    	print("Downloaded all files.")
    elif s == documents:
    	os.chdir("cd Documents")
    elif s == nano:
    	os.system("nano")
    elif s == user:
    	print("AI-term")
    elif s == eject:
    	time.sleep(5)
    	boot = input("tap a to boot from drive")
    	if boot == "a":
    		print("booted.")
    	else:
    		time.sleep(1)
    		print("Failed to load required files.")
    		time.sleep(0.5)
    		print("):")
    		print("Your computer ran into a boot error.")
    		print("Failed to collect files to run.")
    		break
    elif s == bsod:
    	time.sleep(2)
    	print("):")
    	print("Your computer ran into an error.")
    	print("ERR_PURPOSFUL_BSOD")
    elif s == mkdir:
    	os.system("mkdir new")
    elif s == mkdir1:
    	os.system("mkdir home")
    elif s == mkdir2:
    	os.system("mkdir files")
