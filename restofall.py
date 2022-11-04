import os
import time
from tqdm import tqdm
import random
from colorama import Fore, Style

import config
import data2
import sys
from sys import stdout

print(Style.BRIGHT)
os.system("title hakier prompt".center(130))
print(Fore.LIGHTGREEN_EX)
dusername = 0


def wanimation(text, s=None, t=random.uniform(.05, .1)):
    for i in text:
        stdout.write(i)
        stdout.flush()
        time.sleep(t)
    if s:
        print("")


print("")
print(Fore.LIGHTGREEN_EX)


def getusername():
    if data2.username is None:
        os.system("cls")
        print(Fore.RED)
        wanimation("Wrong id! closing program in 5 seconds", True)
        os.system("timeout 5")
        time.sleep(10)
        exit()
    else:
        for i in tqdm(range(0, 23), desc="Fetching user's ip adress", ascii=" ----------", unit="1 %", ncols=84,
                      total=100):
            time.sleep(random.uniform(.01, .1))
        os.system('cls')
        for i in range(4):
            print("")
        for i in tqdm(range(23, 62), desc="Fetching user's password", ascii=" ----------", unit="1 %", ncols=82,
                      total=100, initial=23):
            time.sleep(random.uniform(.01, .1))
        os.system('cls')
        for i in range(4):
            print("")
        for i in tqdm(range(62, 81), desc="Fetching user's credit card info", ascii=" ----------", unit="1 %", ncols=91,
                      total=100, initial=62):
            time.sleep(random.uniform(.01, .1))
        os.system('cls')
        for i in range(4):
            print("")
        for i in tqdm(range(81, 100), desc="Fetching user's email", ascii=" ----------", unit="1 %", ncols=83,
                      total=100, initial=81):
            time.sleep(random.uniform(.01, .1))
        email = "@yahoo.com", "@gmail.com", "@onet.pl", "@o2.pl"
        rando = random.randint(0, len(email) - 1)
        separator = '#'
        mail1 = data2.username.split(separator, 1)[0]
        if random.randint(0, 1) == 1:
            rok = random.randint(0, 2022)
        else:
            rok = random.randint(1900, 2022)

        wanimation(
            f'username: {data2.username.encode("utf-8").decode("unicode-escape")} \n e-mail: {mail1.encode("utf-8").decode("unicode_escape")}{rok}{email[rando]}',
            True)
        wanimation(f"password:{random.choice(config.words_pass)}{random.randint(1950,2020)}{random.choice(config.words_pass)}")
        input()


getusername()
