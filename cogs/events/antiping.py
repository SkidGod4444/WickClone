import os
import discord
from discord.ext import commands
import requests
import sys
from utils.Tools import getConfig, add_user_to_blacklist, getanti
import setuptools
from itertools import cycle
from collections import Counter
import threading
import datetime
import logging
from core import Darkz, Cog
import time
import asyncio
import aiohttp
import tasksio
from discord.ui import View, Button
import json
from discord.ext import tasks
import random

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antipinginv(Cog):
    def __init__(self, client: Darkz):
        self.client = client
        self.spam_control = commands.CooldownMapping.from_cooldown(10, 12.0, commands.BucketType.user)
        print("Cog Loaded: Antipinginv")

    @commands.Cog.listener()
    async def on_message(self, message):
      button = Button(label="Invite Me", url =  "https://discord.com/oauth2/authorize?client_id=852919423018598430&permissions=2113268958&redirect_uri=https://discord.gg/7QHkdV9Zte&response_type=code&scope=bot")
      button1 = Button(label="Support Server", url = "https://discord.gg/7QHkdV9Zte")
      button2 = Button(label="Vote Me", url = "https://top.gg/bot/852919423018598430/vote")
      try:
       
        with open("blacklist.json", "r") as f:
          data2 = json.load(f)
          darkz = '<@852919423018598430>'
          try:
            data = getConfig(message.guild.id)
            anti = getanti(message.guild.id)
            prefix = data["prefix"]
            wled = data["whitelisted"]
            punishment = data["punishment"]
          except Exception:
            pass
          guild = message.guild
          if message.mention_everyone:
            if str(message.author.id) in wled or anti == "off":
              pass
            else:
              if punishment == "ban":
                await message.guild.ban(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "kick":
                await message.guild.kick(message.author, reason="Mentioning Everyone | Not Whitelisted")
              elif punishment == "none":
                return


          elif message.content == darkz or message.content == "<@!852919423018598430>":
            if str(message.author.id) in data2["ids"]:
              embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)")
              await message.reply(embed=embed, mention_author=False)
            else:

              embed = discord.Embed(description=f"""Hey, I\'m Darkz Security 

                                    
Please use the following command instead: `{prefix}help`

                                    
If you continue to have problems, consider asking for help in support server [here](https://discord.gg/7QHkdV9Zte)""", color=discord.Colour(0x2f3136))
              view = View()
              view.add_item(button)
              view.add_item(button1)
              view.add_item(button2)
              await message.reply(embed=embed, mention_author=False, view=view)
          else:
            return
      except Exception as error:
        if isinstance(error, discord.Forbidden):
              return