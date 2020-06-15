import time, os, sys

# code
os.system("clear")
time.sleep(2)

#colors
R="\033[1;31m"

# code
print (R+"""
     _  _ ___  _  _ _  _ ___ _  _ _  _
     |  | |__] |  | |\ |  |  |  |  \/
     |__| |__] |__| | \|  |  |__| _/\_
"""+R)
time.sleep(1)
print("\033[1;36m ×=======================================× ")
print("\033[1;36m ×         \033[1;31mCode By - Kartike Singh       \033[1;36m× ")
print("\033[1;36m ×       \033[1;34mInstagram - khackersx           \033[1;36m× ")
print("\033[1;36m ×         \033[0;32mYoutube - KHACKERSX           \033[1;36m× ")
print("\033[1;36m ×=======================================× ")
time.sleep(2)
print("  ")
print(" \033[0;32m1. Install Ubuntu ")
print(" \033[0;31m2. Exit ")
print(" ")
op = input ("\033[1;33mChoose any one option : ")
if op == "1" :
   print("\033[0;32mInstalling Ubuntu...")
   os.system("cd")
   os.system("apt install wget openssl-tool proot -y && hash -r && wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh && bash ubuntu.sh")

else :
  print("\033[0;31mAborting... See you soon...")
