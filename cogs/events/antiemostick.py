import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
from core import Cog, Darkz
import datetime
import logging
import time
import asyncio
import aiohttp
import tasksio
from discord.ext import tasks
import random
from utils.Tools import *

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antiemostick(Cog):
    def __init__(self, client: Darkz):
        self.client = client      
        self.headers = {"Authorization": f"Bot ODUyOTE5NDIzMDE4NTk4NDMw.GoxHP1.xHwxbepouv5-7IJbvyL5Espvi6j_JOMvwMm1mY"}
        print("Cog Loaded: Antiemostick")
    @commands.Cog.listener()
    async def on_guild_emojis_update(self, guild, before, after) -> None:
      try:
        data = getConfig(guild.id)
        anti = getanti(guild.id)
        punishment = data["punishment"]
        wled = data["whitelisted"]
        reason = "Creating Emojis | Not Whitelisted"
        async for entry in guild.audit_logs(
                limit=1):
            user = entry.user.id
            emoji = await guild.fetch_emoji(entry.target.id)
        api = random.randint(8,9)
        if user == 852919423018598430:
          pass
        elif entry.user == guild.owner:
          pass
        elif str(entry.user.id) in wled or anti == "off":
            pass
        else:
         if entry.action == discord.AuditLogAction.emoji_create:
          async with aiohttp.ClientSession(headers=self.headers) as session:
            if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                    if r.status in (200, 201, 204):
                      await emoji.delete()
                      logging.info("Successfully banned %s" % (user))
            elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                             if r2.status in (200, 201, 204):
                               await emoji.delete()
                               logging.info("Successfully kicked %s" % (user))
            elif punishment == "none":
              mem = guild.get_member(entry.user.id)
              await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
              await emoji.delete()
            else:
                       return
      except Exception as error:
            if isinstance(error, discord.Forbidden):
              return