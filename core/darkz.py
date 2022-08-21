from __future__ import annotations
from discord.ext import commands
import discord
import aiohttp
import json
import jishaku, time
import asyncio
import typing
from utils.config import OWNER_IDS, EXTENSIONS, No_Prefix
from utils import getConfig, updateConfig, DotEnv
from .Context import Context


class Darkz(commands.AutoShardedBot):
    def __init__(self, *arg, **kwargs):
      self.topgg_headers = {"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijg1MjkxOTQyMzAxODU5ODQzMCIsImJvdCI6dHJ1ZSwiaWF0IjoxNjU3OTczMzg1fQ.dAJ-sw8rZi2yVVCq8jeoXUlj1AB1drooDexd6RF4Q2Y"}
      intents = discord.Intents.all()
      intents.presences = False
      super().__init__(command_prefix=self.get_prefix,
                         case_insensitive=True,
                         intents=intents,
                         status=discord.Status.dnd,
                         strip_after_prefix=True,
                         owner_ids=OWNER_IDS,
                         allowed_mentions=discord.AllowedMentions(
                             everyone=False, replied_user=False), 
shard_count=2)
  
    async def on_ready(self):
        print("Connected as {}".format(self.user))

    async def on_connect(self):
      await self.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.competing, name=f'{len(self.guilds)} Guilds!'))
      #await self.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=f'Azadi Ka Amrit Mahotsav 🇮🇳'))
      async with aiohttp.ClientSession(headers=self.topgg_headers)as session:
        async with session.post("https://top.gg/api/bots/852919423018598430/stats", json={"server_count": len(self.guilds), "shard_count": len(self.shards)}) as r:
          print("Posted Data On Top GG", r.status)

    async def send_raw(self, channel_id: int, content: str,
                       **kwargs) -> typing.Optional[discord.Message]:
        await self.http.send_message(channel_id, content, **kwargs)

    async def invoke_help_command(self, ctx: Context) -> None:
        """Invoke the help command or default help command if help extensions is not loaded."""
        return await ctx.send_help(ctx.command)

    async def fetch_message_by_channel(
        self, channel: discord.TextChannel, messageID: int
    ) -> typing.Optional[discord.Message]:
        async for msg in channel.history(
            limit=1,
            before=discord.Object(messageID + 1),
            after=discord.Object(messageID - 1),
        ):
            return msg

    async def get_prefix(self, message: discord.Message):
      with open('info.json', 'r') as f:
        p = json.load(f)
      if message.author.id in p["np"]:
      #if message.author.id in [743431588599038003, 905396101274828821, 968013339953352715, 730000865133592646]:
        return ['$', '']
      else:
        if message.guild:
          data = getConfig(message.guild.id)
          prefix = data["prefix"]
          return prefix
        else:
          return "$"

    async def on_message_edit(self, before, after):
      ctx: Context = await self.get_context(after, cls=Context)
      if before.content != after.content:
        if after.guild is None or after.author.bot:
          return
        if ctx.command is None:
          return
        if type(ctx.channel) == "public_thread":
          return
        await self.invoke(ctx)
      else:
        return