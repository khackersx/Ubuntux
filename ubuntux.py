import time, os, sys

# code
os.system("clear")
time.sleep(2)

#colors
R="\033[1;31m"
G="\033[0;32m"

# code
print("\033[1;36mPlease Wait... Installing Requirements.")
time.sleep(3)
os.system("apt install python git -y")
time.sleep(2)
print(" ")
print("\033[0;0m Setup Finished... Launching the tool...")
time.sleep(2)
os.system("clear")

print (R+"""
     _  _ ___  _  _ _  _ ___ _  _ _  _
     |  | |__] |  | |\ |  |  |  |  \/
     |__| |__] |__| | \|  |  |__| _/\_
        """+G+"""   Author: @geekykartik """)
time.sleep(2)
print("  ")
print(" \033[0;32m1. Install Ubuntu ")
print(" \033[0;31m2. Exit ")
print(" ")
op = input ("\033[1;33mChoose any one option : ")
if op == "1" :
   print("\033[0;32mInstalling Ubuntu...\033[0;0m")
   os.system("cd")
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")

else :
  print("\033[0;31mAborting... \033[0mSee you soon...")
