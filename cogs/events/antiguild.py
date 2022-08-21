import os
import discord
from discord.ext import commands
import requests
import sys
import setuptools
from itertools import cycle
import threading
import datetime
import logging
from core import Cog, Darkz
import time
import asyncio
import aiohttp
import tasksio
from discord.ext import tasks
import random
import httpx
from utils.Tools import *
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}

class antiguild(Cog):
    def __init__(self, client: Darkz):
        self.client = client      
        self.headers = {"Authorization": f"Bot ODUyOTE5NDIzMDE4NTk4NDMw.GoxHP1.xHwxbepouv5-7IJbvyL5Espvi6j_JOMvwMm1mY"}
        print("Cog Loaded: Antiguild")
    @commands.Cog.listener()
    async def on_guild_update(self, before, after) -> None:
        try:
            data = getConfig(before.id)
            anti = getanti(before.id)
            punishment = data["punishment"]
            wled = data["whitelisted"]
            reason = "Updating Guild | Not Whitelisted"
            guild = after
            async for entry in after.audit_logs(
                limit=1):
              user = entry.user.id
            api = random.randint(8,9)
            if entry.user.id == 852919423018598430:
              return
            elif entry.user == after.owner:
              return
            elif str(entry.user.id) in wled or anti == "off":
              return
            else:
             if entry.action == discord.AuditLogAction.guild_update:
              async with aiohttp.ClientSession(headers=self.headers) as session:
               if punishment == "ban":
                  async with session.put(f"https://discord.com/api/v{api}/guilds/%s/bans/%s" % (guild.id, user), json={"reason": reason}) as r:
                      if before.icon and not before.icon == after.icon:
                        banneidn = requests.get(before.icon.url)
                        huehuehue = banneidn.content
                        await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, icon=huehuehue, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                      if after.icon and not before.icon:
                        await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, icon=None, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                      if not before.icon and not after.icon:
                        await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                      if before.icon == after.icon:
                        await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                      logging.info("Successfully banned %s" % (user))
               elif punishment == "kick":
                         async with session.delete(f"https://discord.com/api/v{api}/guilds/%s/members/%s" % (guild.id, user), json={"reason": reason}) as r2:
                               if before.icon and not before.icon == after.icon:
                                bannei = requests.get(before.icon.url)
                                huehueh = bannei.content
                                await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, icon=huehueh, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                         if after.icon and not before.icon:
                           await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, icon=None, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                         if not before.icon and not after.icon:
                           await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                         if before.icon and before.icon == after.icon:
                           await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                           logging.info("Successfully kicked %s" % (user))
               elif punishment == "none":
                           mem = guild.get_member(entry.user.id)
                           await mem.edit(roles=[role for role in mem.roles if not role.permissions.administrator], reason=reason)
                           if before.icon and not before.icon == after.icon:
                              bann = requests.get(before.icon.url)
                              huehu = bann.content
                              await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, icon=huehu, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                           if after.icon and not before.icon:
                            await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, icon=None, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                           if not before.icon and not after.icon:
                             await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
                           if before.icon and before.icon == after.icon:
                            await after.edit(name=f"{before.name}", description=f"{before.description}", verification_level=before.verification_level, rules_channel=before.rules_channel, afk_channel=before.afk_channel, afk_timeout=before.afk_timeout, default_notifications=before.default_notifications, explicit_content_filter=before.explicit_content_filter, system_channel=before.system_channel, system_channel_flags=before.system_channel_flags, public_updates_channel=before.public_updates_channel, reason=reason, premium_progress_bar_enabled=before.premium_progress_bar_enabled)
               else:
                       return
        except Exception as error:
            if isinstance(error, discord.Forbidden):
              return