import discord
from discord.ext import commands
import datetime
import re
import json
from core import Darkz, Cog

from utils.Tools import getConfig


class AntiSpam(Cog):
    def __init__(self, client: Darkz):
        self.client = client
        self.spam_cd_mapping = commands.CooldownMapping.from_cooldown(4, 7, commands.BucketType.member)
        self.spam_punish_cooldown_cd_mapping = commands.CooldownMapping.from_cooldown(1, 10, commands.BucketType.member)
        print("Cog Loaded: AntiSpam")
    @commands.Cog.listener()    
    async def on_message(self, message):
      if not message.guild:
        return
      mem = message.author
      invite_regex = re.compile(r"(?:https?://)?discord(?:app)?\.(?:com/invite|gg)/[a-zA-Z0-9]+/?")
      link_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
      invite_matches = invite_regex.findall(message.content)
      link_matches = link_regex.findall(message.content)
      data = getConfig(message.guild.id)
      antiSpam = data["antiSpam"]
      antiLink = data["antiLink"]
      wled = data["whitelisted"]
      try:
                if antiSpam is True:
                  if mem.guild_permissions.administrator or str(message.author.id) in wled:
                    return
                  bucket = self.spam_cd_mapping.get_bucket(message)
                  retry = bucket.update_rate_limit()

                  if retry:
                    #punish_cd_bucket = self.spam_punish_cooldown_cd_mapping.get_bucket(message)
                 #   if not punish_cd_bucket.update_rate_limit():
                      if data["punishment"] == "kick":
                        await message.author.kick(reason=f"Darkz Security | Anti Spam")
                        await message.channel.send(f"<:success_ok:946729333274337350> Kicked {message.author} For Spamming")

                      if data["punishment"] == "ban":
                        await message.author.ban(reason=f"Darkz Security | Anti Spam")
                        await message.channel.send(f"<:success_ok:946729333274337350> Banned {message.author} For Spamming")

                      if data["punishment"] == "none":
                        now = discord.utils.utcnow()
                        await message.author.timeout(now + datetime.timedelta(minutes=15), reason="Darkz Security | Anti Spam")
                        await message.channel.send(f"<:success_ok:946729333274337350> Muted {message.author} For Spamming")

                if antiLink is True:
                    if mem.guild_permissions.administrator or str(message.author.id) in wled:
                        return
                    if invite_matches:
                        await message.delete()

                        if data["punishment"] == "kick":
                            await message.author.kick(reason=f"Darkz Security | Anti Discord Invites")
                            await message.channel.send(f"<:success_ok:946729333274337350> Kicked {message.author} For Sending Discord Server Invites")

                        if data["punishment"] == "ban":
                            await message.author.ban(reason=f"Darkz Security | Anti Discord Invites", delete_message_days=0)
                            await message.channel.send(f"<:success_ok:946729333274337350> Banned {message.author} For Sending Discord Server Invites")

                        if data["punishment"] == "none":
                             now = discord.utils.utcnow()
                             await message.author.timeout(now + datetime.timedelta(minutes=15), reason="Darkz Security | Anti Discord Invites")
                             await message.channel.send(f"<:success_ok:946729333274337350> Muted {message.author} For Sending Discord Server Invites")
                    if link_matches:
                        if data["punishment"] == "kick":
                          await message.author.kick(reason="Darkz Security | Anti Link")  
                          await message.channel.send(f"<:success_ok:946729333274337350> Kicked {message.author} For Sending Links")



                        if data["punishment"] == "ban":
                          await message.author.ban(reason="Darkz Security | Anti Link")    
                          await message.channel.send(f"<:success_ok:946729333274337350> Banned {message.author} For Sending Links")

                        if data["punishment"] == "none":
                          now = discord.utils.utcnow()
                          await message.author.timeout(now + datetime.timedelta(minutes=15), reason="Darkz Security | Anti Link")
                          await message.channel.send(f"<:success_ok:946729333274337350> Muted {message.author} For Sending Links")
                    else:
                      return
      except Exception as error:
                print(error)