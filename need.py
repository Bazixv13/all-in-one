import asyncio
import discord
from discord import activity
from discord.ext import commands
import os
import config
import data
from tqdm import tqdm
import time
from colorama import Fore, Back, Style
import random


print(" ")


bot = commands.Bot(command_prefix=commands.when_mentioned_or('^'), help_command=None)
activity = activity

print(Fore.RED)
os.system("echo INFO:if program broke it means you entered wrong id")
os.system("timeout 5")
os.system("cls")

def wanimation(text, s=None,t=random.uniform(.01, .05)):
    for char in text:
        time.sleep(t)
        print(char, end='')
    if s:
        print("")


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="Searching for some things...",
                                  status=discord.Status.idle))
    user = None
    f = open("data.py", "r")
    user_id = data.id
    f.close()

    print(Fore.LIGHTGREEN_EX)
    wanimation("fetching user nickname and hashtag",None,0)
    wanimation("...",True,1)
    user = await bot.fetch_user(int(user_id))
    f = open("data2.py", "wb")
    f.write(f"username = '{user}'".encode("utf-8"))
    f.close()
    await bot.close()


bot.run(config.bot_token)
