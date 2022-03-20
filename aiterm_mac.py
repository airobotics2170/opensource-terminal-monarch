import os
import time
print("[OK] Running terminal")
time.sleep(1)
print("[OK] systemctl start service ai-term.service")
time.sleep(1)
print("[OK] Loading user preferences")
time.sleep(1)
print("[OK] Version Monarch:ON")
time.sleep(1)
print("AI Terminal version:Monarch stable")
time.sleep(1)
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
    up = "term.update --newest"
    dev_update = "term.update --dev check"
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
    mkdir3 = "mkdir code"
    mkdir4 = "mkdir other"
    patrion = "patrion"
    help1 = "sudo su -help"
    help2 = "exit -help"
    help3 = "hostname -help"
    help4 = "cd downloads -help"
    help5 = "cd desktop -help"
    help6 = "python3 -help"
    help7 = "clear -help"
    help8 = "time -help"
    help9 = "ls -help"
    help10 = "term.update -help"
    help11 = "backup -help"
    help12 = "cd documents"
    help13 = "nano -help"
    help14 = "$USER -help"
    help15 = "mkdir -help"
    verify = "verify"
    help16 = "verify -help"
    f = open("verification.txt", "a")
    s = input("AI-term@localhost>")
    if s == o:
        print("Now root")
    elif s == d:
            break
    elif s == f:
        os.system("hostname")
    elif s == ff:
        #os.chdir("/Users/username/Downloads")
        print("Path: downloads")
    elif s == ffff:
        #os.chdir("/Users/username/Desktop")
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
        print("term.update --newest, to update to newest terminal")
        print("cd documents, to go to documents")
        print("nano, to edit and create files")
        print("cd desktop, to go to desktop directory")
        print("mkdir new, to make new directory called new")
        print("mkdir home, to make new directory called home")
        print("mkdir files, to make new directory called files")
        print("eject, to eject drive")
        print("patrion")
        print("$USER, to view user")
        print("verify, to verify you are a human")
        print("--help, run one of these commands with --help at the end to get even more help on that command")
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
    elif s == patrion:
    	email = input("please enter your email: ")
    	signup_password = input("password: ")
    	print("thank you so so much for your support the pro tip you get is bsod-run this command runs a bsod simulation for fun!")
    elif s == help1:
    	print("the sudo su command lets you have super user prinvelaeges instead of doin sudo before command")
    elif s == help2:
    	print("the exit command lets you easily exit the terminal")
    elif s == help3:
    	print("the hostname lets you view the address your computer can be accessed at")
    elif s == help4:
    	print("the cd downloads command lets you access the downloads directory")
    elif s == help5:
    	print("the cd desktop command lets you access the desktop directory")
    elif s == help6:
    	print("the python3 command lets you program in python")
    elif s == help7:
    	print("the clear command lets you clear all output text")
    elif s == help8:
    	print("the time command lets you view the time")
    elif s == help9:
    	print("the ls command lets you view all files in a directory")
    elif s == help10:
    	print("the term.update commands let you update to the newest terminal")
    elif s == help11:
    	print("the backup commands let you view and download all backed up files")
    elif s == help12:
    	print("the cd documents command lets you access the documents directory")
    elif s == help13:
    	print("the nano command lets you use the nano text editor")
    elif s == help14:
    	print("the $USER command lets you view the current user")
    elif s == help15:
    	print("the mkdir commands let you make a new directory")
    elif s == mkdir3:
    	os.system("mkdir code")
    elif s == mkdir4:
    	os.system("mkdir other")
    elif s == verify:
    	print("car,cat,gas")
    	captcha = input("which is living: ")
    	if captcha == "cat":
    		print("you are now verified as human")
    		f.write("user = human")
    		f.write("\n")
    		f.close
    	elif captcha == "car":
    		f.write("user = robot")
    		f.write("\n")
    		f.close
    		break
    	elif captcha == "gas":
    		f.write("user = robot")
    		f.write("\n")
    		f.close
    		break
    	else:
    		print("no option",captcha)
    		f.write("user = unknown")
    elif s == help16:
    	print("the verify command lets you verify you are a human for things on the terminal")
    else:
    	print("Command",s,"was not found ): try running help command or -help for after any command for help on commands")
