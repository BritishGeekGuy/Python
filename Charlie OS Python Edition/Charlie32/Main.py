#Imports Some Third-Party Commands
import os
import sys
import random
import ctypes

#Clearing Command Line
os.system('cls')

#Sys
while True:
        #Sets Command Line`s Name
        ctypes.windll.kernel32.SetConsoleTitleA("CharlieOS")

        #user command line
        usr_cmd = input("user@charlieos~: ")

        #Commands
        if usr_cmd == "Shutdown":
               sys.exit()
        if usr_cmd == "Help":
        	   print("Welcome To Help! If You Want To Find Help On A Specific Command: Type Help And Then The Commands Name Or If You Want All Of The Commands: Type Help All")
        if usr_cmd == "About":
               print("Copyright (C) Charlie Who")
               print("All Right Reserved")
               print("You Are Free To Edit And Re-distribute Do Not Re-distribute Under Charlie OS")
        if usr_cmd == "Help Shutdown":
        	print("Shutdown Turns The Script Off")
        if usr_cmd == "Help All":
        	print("Shutdown Turns The Script Off")
        	print("About Shows Copyright Infomation")
        if usr_cmd == "Help About":
        	print("About Shows Copyright Infomation")
            