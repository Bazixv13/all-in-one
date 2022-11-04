import os
import firston
import config
os.system(f"title hakier prompt, current config: loading bars = {config.loading_bars}, typing animations = {config.typing_animation} (1 letter per {config.typing_animation_speed} second)".center(130))


def pip():
    print(
        "INFO:Check if u have pip added to path by typing pip in command prompt, Get more info in readme.txt")
    os.system("timeout 30")
    print("please wait....")
    os.system("pip install tqdm")
    os.system("pip install discord.py==1.7.3")
    os.system("cls")


if firston.on is True:
    print("INFO:Everything seems to be downaled skipping... if something is not downalded chcnge on to False in fiston.py ")
    os.system("timeout 2")
elif firston.on is False:
    pip()
    f = open("firston.py", "w")
    f.write("on = True")
    f.close()


from sys import stdout
import time
from tqdm import tqdm
import random
from colorama import Fore, Style
import ctypes

f = open("data2.py", "w")
f.write(f"username = None")
f.close()


def wanimation(text, s=None, t=random.uniform(.05, .1)):
    for i in text:
        stdout.write(i)
        stdout.flush()
        if config.typing_animation is False:
            t = 0
        if config.manual_typing_animation_speed is True and config.typing_animation is True:
            if config.typing_animation_speed > 0:
                t = config.typing_animation_speed
        time.sleep(t)
    if s:
        print("")


os.system("cls")
print(Style.BRIGHT)
os.system(f"title hakier prompt, current config: loading bars = {config.loading_bars}, typing animations = {config.typing_animation} (1 letter per {config.typing_animation_speed} second)".center(130))
print(Fore.LIGHTGREEN_EX)
print("")
wanimation("Welcome Dear hecker", True)
if config.loading_bars is True:
    for i in tqdm(range(0, 100), desc="Loading avaible options", ascii=" ----------", unit="1 %", ncols=84):
        time.sleep(random.uniform(.001, .01))
    time.sleep(random.randint(1, 3))
os.system("cls")
os.system(f"title hakier prompt")
if config.loading_bars is True:
    wanimation("1.destroy the world", True)
    wanimation(f"2.hack user on discord [BETA{config.d_finished}]", True)
    wanimation("3.do not click me", True)
    wanimation("4.calculator [BETA]", True)
    wanimation("chose option: ");
if config.loading_bars is False:
    wanimation("1.destroy the world [unavaible with current configuration, to run this edit config.py file]", True)
    wanimation(f"2.hack user on discord [BETA{config.d_finished}]", True)
    wanimation("3.do not click me", True)
    wanimation("4.calculator [BETA]", True)
    wanimation("chose option: ");
tudu = input()
if tudu == "1":
    wanimation("are you sure? (y/n) ");
    ays = input(":")
    if ays == "y":
        for i in tqdm(range(0, 100), desc="Destroying world", ascii=" ----------", unit="1 %", ncols=84):
            time.sleep(random.uniform(21, 37))
        time.sleep(5)
        os.system("cls")
        wanimation("┏┓┏┓┏┳━━━┳━━━┳┓╋╋┏━━━┓  ┏━━━┳━━━┳━━━┳━━━━┳━━━┳━━━┳━━━┳━━━┓", True)
        wanimation('┃┃┃┃┃┃┏━┓┃┏━┓┃┃╋╋┗┓┏┓┃  ┗┓┏┓┃┏━━┫┏━┓┃┏┓┏┓┃┏━┓┃┏━┓┃┏━━┻┓┏┓┃', True)
        wanimation('┃┃┃┃┃┃┃╋┃┃┗━┛┃┃╋╋╋┃┃┃┃  ╋┃┃┃┃┗━━┫┗━━╋┛┃┃┗┫┗━┛┃┃╋┃┃┗━━┓┃┃┃┃', True)
        wanimation('┃┗┛┗┛┃┃╋┃┃┏┓┏┫┃╋┏┓┃┃┃┃  ╋┃┃┃┃┏━━┻━━┓┃╋┃┃╋┃┏┓┏┫┃╋┃┃┏━━┛┃┃┃┃', True)
        wanimation('┗┓┏┓┏┫┗━┛┃┃┃┗┫┗━┛┣┛┗┛┃  ┏┛┗┛┃┗━━┫┗━┛┃ ┃┃ ┃┃┃┗┫┗━┛┃┗━━┳┛┗┛┃', True)
        wanimation('╋┗┛┗┛┗━━━┻┛┗━┻━━━┻━━━┛  ┗━━━┻━━━┻━━━┛ ┗┛ ┗┛┗━┻━━━┻━━━┻━━━┛', True)
        print("")
        os.system("pause")
        wanimation("colosing in 1 miute", True)
        os.system("timeout 60")
    elif ays != "y":
        wanimation("closing")
        wanimation("...", True, random.uniform(2, 4))
        os.system("exit")

if tudu == "2":
    ctypes.windll.user32.MessageBoxW(0, "This function may not work properly.", "WARNING" , 0)
    ctypes.windll.user32.MessageBoxW(0, "If user nickname have unusual characters program will broke", "WARNING 2", 0)
    wanimation("enter user id ");
    userid = input(":")
    if len(userid) == 18:
        f = open("data.py", "w")
        f.write(f"id = {userid}")
        f.close()
        os.system('C:/Users/%USERNAME%/Documents/"all in one"/need.py')
        os.system('C:/Users/%USERNAME%/Documents/"all in one"/restofall.py')
    else:
        print(Fore.RED)
        print(Style.BRIGHT)
        wanimation("Wrong id! closing program in 5 seconds", True)
        os.system("timeout 5")
if tudu == "3":
    for i in range(random.randint(1, 5)):
        print("NONE")
        time.sleep(random.uniform(0.2137, 1.69))
    os.system("start https://hi.bazixv13.repl.co/hello.html")
    os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")

if tudu == "4":
    wanimation("CALCULATOR", True)
    wanimation("Do you wanna?", True);
    wanimation("1.add", True)
    wanimation("2.minus", True)
    wanimation("3.multiply", True)
    wanimation("4.devide", True)
    wanimation("chosen option: ");
    znak = input()
    if znak == "1":
        separator = "+"
        wanimation("enter your mathematical operation: ")

if tudu == "dev1":
    ays = input("are you sure? (y/n)")
    if ays == "y":
        for i in tqdm(range(0, 100), desc="Destroying world", ascii=" ----------", unit="1 %", ncols=72):
            time.sleep(1)
            time.sleep(5)
            os.system("cls")
            wanimation("┏┓┏┓┏┳━━━┳━━━┳┓╋╋┏━━━┓  ┏━━━┳━━━┳━━━┳━━━━┳━━━┳━━━┳━━━┳━━━┓", True)
            wanimation('┃┃┃┃┃┃┏━┓┃┏━┓┃┃╋╋┗┓┏┓┃  ┗┓┏┓┃┏━━┫┏━┓┃┏┓┏┓┃┏━┓┃┏━┓┃┏━━┻┓┏┓┃', True)
            wanimation('┃┃┃┃┃┃┃╋┃┃┗━┛┃┃╋╋╋┃┃┃┃  ╋┃┃┃┃┗━━┫┗━━╋┛┃┃┗┫┗━┛┃┃╋┃┃┗━━┓┃┃┃┃', True)
            wanimation('┃┗┛┗┛┃┃╋┃┃┏┓┏┫┃╋┏┓┃┃┃┃  ╋┃┃┃┃┏━━┻━━┓┃╋┃┃╋┃┏┓┏┫┃╋┃┃┏━━┛┃┃┃┃', True)
            wanimation('┗┓┏┓┏┫┗━┛┃┃┃┗┫┗━┛┣┛┗┛┃  ┏┛┗┛┃┗━━┫┗━┛┃ ┃┃ ┃┃┃┗┫┗━┛┃┗━━┳┛┗┛┃', True)
            wanimation('╋┗┛┗┛┗━━━┻┛┗━┻━━━┻━━━┛  ┗━━━┻━━━┻━━━┛ ┗┛ ┗┛┗━┻━━━┻━━━┻━━━┛', True)
            print("")
            os.system("pause")
            wanimation("Restart in 1minute to finish destoying the world", True)
            wanimation("colosing in 1 miute", True)
            os.system("timeout 60")
            exit()
