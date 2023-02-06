import discord
from discord.ext import commands
from afks import afks
from discord.utils import get
import psutil
from psutil import Process, virtual_memory
from typing import Union, Optional
import time
import datetime
import random
import requests
import aiohttp
import re
from discord.ext.commands.errors import BadArgument
from discord.colour import Color
import hashlib
from utils.Tools import *
import contextlib
from traceback import format_exception
import discord
from discord.ext import commands
import io
import textwrap
import datetime
import sys
from discord.ui import Button, View
import psutil
import time
import datetime
import platform


password = ['1838812`', '382131847', '231838924', '218318371', '3145413', '43791', '471747183813474', '123747019', '312312318']
def remove(afk):
    if "[AFK]" in afk.split():
        return " ".join(afk.split()[1:])
    else:
        return afk

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.aiohttp = aiohttp.ClientSession()
        self._URL_REGEX = r'(?P<url><[^: >]+:\/[^ >]+>|(?:https?|steam):\/\/[^\s<]+[^<.,:;\"\'\]\s])'
        self.tasks = []
        self.dump_tasks = []
        self.sniped = {}
        self.afk = {}
        
        
    @commands.command(help="Changes your state to afk.",usage="Afk [reason]")
    @blacklist_check()
    async def afk(self, ctx, *, reason="I am afk."):
        member = ctx.author
        if member.id in afks.keys():
            afks.pop(member.id)
        else:
            try:
                await member.edit(nick = f"[AFK] • {member.display_name}")
            except:
                pass
        afks[member.id] = reason
        embed = discord.Embed(title="Afk Settings!",description = f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Executor:** `{member.name}`\n<:1spacer:1056545806943006760><:AFK:1057543367325667348> **Afk:** *Enabled* | <:tixk:1053178188613820468>\n<:1spacer:1056545806943006760><:logsx:1053178328846188565> **Reason:** {reason}",
        color = 0xdbdbdb
      )
        embed.set_footer(text=f" {ctx.author} is now set to Afk!")
      # embed.set_footer(name=f"!")
        await ctx.reply(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in afks.keys():
            afks.pop(message.author.id)
            try:
                await message.author.edit(nick = remove(message.author.display_name))
            except:
                pass
            embed = discord.Embed(title="Afk Settings!",description = f'<:1spacer:1056545806943006760><:profile:1056855971839873054> **Executor:** `{message.author.name}`\n<:1spacer:1056545806943006760><:AFK:1057543367325667348> **Afk:** *Disabled* | <:xross:1053176060759515218>',
        color = 0xdbdbdb
      )
        embed.set_footer(text=f" {message.author.name} your Afk! is removed")
            
        await message.channel.send(embed=embed)

        for id, reason in afks.items():
            member = get(message.guild.members, id = id)
            if (message.reference and member == (await message.channel.fetch_message(message.reference.message_id)).author) or member.id in message.raw_mentions:
                embed = discord.Embed(title='Afk Settings!',description =f'<:1spacer:1056545806943006760><:profile:1056855971839873054> **Executor:** {member.name}\n<:1spacer:1056545806943006760><:logsx:1053178328846188565> **Reason:** {reason}',
        color = 0xdbdbdb)
                                     
        embed.set_footer(text=f"{member.name} is Afk!")   
        await message.reply(embed=embed)

 
######################


    @commands.command(usage="Avatar [member]",
        name='avatar',
        aliases=['av', 'pfp'],
        help="""Wanna steal someone's avatar here you go
Aliases"""
    )
    @blacklist_check()
    async def avatar(self, ctx, user: discord.Member = None):
        try:
          if user == None:
             user = ctx.author
          else:  
             user = await self.bot.fetch_user(user.id)
        except AttributeError:
            user = ctx.author
        webp = user.avatar.replace(format='webp')
        jpg = user.avatar.replace(format='jpg')
        png = user.avatar.replace(format='png')
        avemb = discord.Embed(
            color=0xdbdbdb,
            title=f"Avatar Info!",description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
            if not user.avatar.is_animated()
            else f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({user.avatar.replace(format='gif')})"
        )
        avemb.set_image(url=user.avatar.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
    # button = discord.ui.Button(label='Avatar', style=discord.ButtonStyle.url, url=f'{member.avatar}')
     # hacker = discord.ui.Button(label='Server Avatar', style=discord.ButtonStyle.url, url=f'{member.display_avatar}')
      #view = discord.ui.View()
     # view.add_item(button)
     # view.add_item(hacker)
        await ctx.send(embed=avemb)#,view=view)
       # await ctx.send(embed=avemb)


    @commands.command(
                      help="Shows the banner",
                      usage="banner")
    @blacklist_check()
    async def banner(self, ctx):
        if len(ctx.guild.banner_url) == 0:
            return await ctx.send(embed=discord.Embed(
                title="banner", description="There is no guild banner"),
                                  color=self.color)
        await ctx.send(embed=discord.Embed(title="**`%s`**'s server banner" %
                                           (ctx.guild.name),
                                           color=self.color).set_image(
                                               url=ctx.guild.banner_url))

    @commands.command(help="Shows the server icon",usage="Servericon")
    @blacklist_check()
    async def servericon(self, ctx):
        server = ctx.guild
        webp = server.icon.replace(format='webp')
        jpg = server.icon.replace(format='jpg')
        png = server.icon.replace(format='png')
        avemb = discord.Embed(
            color=0xdbdbdb,
            title=f"{server}'s Icon",description=f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp})"
            if not server.icon.is_animated()
            else f"[`PNG`]({png}) | [`JPG`]({jpg}) | [`WEBP`]({webp}) | [`GIF`]({server.icon.replace(format='gif')})"
        )
        avemb.set_image(url=server.icon.url)
        avemb.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=avemb)



    @commands.command(
                      help="Get total guild members status info",
                      usage="memberstats",
                      aliases=["mstatus","gms","mst","statusall"])
    @blacklist_check()
    async def memberstats(self, ctx):
        online = 0
        offline = 0
        dnd = 0
        idle = 0
        bots = 0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.dnd:
                dnd += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.bot:
                bots += 1
        embed = discord.Embed(
            title=f"Guild Memebers Status!",
            description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n\n<:rightshort:1053176997481828452> **Counts:**\n<:1spacer:1056545806943006760><:Roles:1057491608603467838> **Memeber(s):** `%s`\n<:1spacer:1056545806943006760><a:bots:1057611653572726824> **Bot(s):** `{bots}`\n\n<:rightshort:1053176997481828452> **Status:**\n<:1spacer:1056545806943006760><:Online:1057609953248030750> **Online Users:** `{online}`\n<:1spacer:1056545806943006760><:idle:1057610060290867321> **Idle Users:** `{idle}`\n<:1spacer:1056545806943006760><:dnd:1057610035875827753> **Dnd Users:** `{dnd}`\n<:1spacer:1056545806943006760><:offline:1057609999729315890> **Invisible Users:** `{offline}`" % (len(ctx.guild.members)),color=0xdbdbdb)
           # (ctx.guild.name),
            
        embed.set_footer(text="Powered by Sputnik!")
        
        await ctx.send(embed=embed)


    @commands.command(
                      help="Get total guild members status info",
                      usage="memberstats",
                      aliases=["mc","memberscount"])
    @blacklist_check()
    async def membercount(self, ctx):
        online = 0
        offline = 0
        dnd = 0
        idle = 0
        bots = 0
        for member in ctx.guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.dnd:
                dnd += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.bot:
                bots += 1
        embed = discord.Embed(
            title=f"Memebers Count!",
            description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n\n<:rightshort:1053176997481828452> **Counts:**\n<:1spacer:1056545806943006760><:Roles:1057491608603467838> **Memeber(s):** `%s`\n<:1spacer:1056545806943006760><a:bots:1057611653572726824> **Bot(s):** `{bots}`" % (len(ctx.guild.members)),color=0xdbdbdb)
           # (ctx.guild.name),
            
        embed.set_footer(text="Powered by Sputnik!")
        
        await ctx.send(embed=embed)
      
    @commands.command(usage="Poll [message]",aliases= ["voting","votesystem"],help= "Creates a voting system in your server!")
    @blacklist_check()
    async def poll(self, ctx,*,message):
      emp = discord.Embed(title=f"**Vote System!**", description=f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:ctx:1056735079445053481> **Vote for:** `{message}`\n\n<:sarrow:1053149614003462174> React with <:tixk:1053178188613820468> if you agree with this statement!\n<:sarrow:1053149614003462174> React with <:xross:1053176060759515218> if you not agree with this statement!\n<:sarrow:1053149614003462174> React with <:nol:1056830376858886224> if you are not sure about!", color =  0xdbdbdb)
     #embed.set_footer(text="Powered by Sputnik!")
      msg = await ctx.send(embed=emp) 
      await msg.add_reaction("<:tixk:1053178188613820468>")
      await msg.add_reaction("<:xross:1053176060759515218>")
      await msg.add_reaction("<:nol:1056830376858886224>")
      
      

    @commands.command( help="Shortens specified url with 3 different url shorteners",usage="Shorten <url>",aliases= ["short"])
    @blacklist_check()
    @commands.is_owner()
    async def shorten(self, ctx: commands.Context, *, url: str):
        async with ctx.typing():
            embed = discord.Embed(
                title="URL Shortener!")
            async with self.aiohttp.get("https://api.shrtco.de/v2/shorten?url={}".format(url)) as shrtco:
                async with self.aiohttp.get("https://clck.ru/--?url={}".format(url)) as clck:
                    async with self.aiohttp.get("http://tinyurl.com/api-create.php?url={}".format(url)) as tiny:
                        parse = await shrtco.json()
                        embed.add_field(name="Shortened URL (9qr.de)", value=parse["result"]["full_short_link2"], inline=False)
                        embed.add_field(name="Shortened URL (clck.ru)", value=await clck.text(), inline=False)
                        embed.add_field(name="Shortened URL (tinyurl.com)", value=await tiny.text(), inline=False)
        await ctx.reply(embed=embed, mention_author=True)
        
        

    @commands.command(name="rickroll",help="Detects if provided url is a rick-roll",usage="Rickroll <url>")
    @blacklist_check()
    async def _rr(self, ctx: commands.Context, *, url: str):
        if not re.match(self._URL_REGEX, url):
            raise BadArgument("Invalid URL")

        phrases = ["rickroll", "rick roll", "rick astley", "never gonna give you up"]
        source = str(await (await self.aiohttp.get(url, allow_redirects=True)).content.read()).lower()
        rickRoll = bool(
            (re.findall('|'.join(phrases), source, re.MULTILINE | re.IGNORECASE)))
        await ctx.reply(embed=discord.Embed(
            title="Rick Roll!", description="{} in webpage".format(
                "was found" if rickRoll is True else "was not found"),
            color=Color.red() if rickRoll is True else Color.green(),
        ), mention_author=True)

    @commands.Cog.listener()
    async def on_message_delete(self, message): 
        if message.guild == None: 
            return
        if message.author.bot: 
            return
        if not message.content: 
            return 
        self.sniped[message.channel.id] = message
         #@commands.command(aliases=['sb'])
    @commands.guild_only()
    @commands.has_permissions(view_audit_log=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @blacklist_check()
    @commands.group(name="snipe", help="Snipes the most recently deleted message", usage="snipe", aliases=["snipemsgs"])
    async def snipe(self, ctx):
        message = self.sniped.get(ctx.channel.id)
        if message == None:
            return await ctx.send(embed=discord.Embed(title="Sniped!", description=f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:ctx:1056735079445053481> **Message:** `No msgs found to snipe!`", color=0xdbdbdb))#timestamp=message.created_at))
        embed = discord.Embed(title="Sniped!", description=f"<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:logsx:1053178328846188565> **Sent by:** `{message.author}`\n<:1spacer:1056545806943006760><:ctx:1056735079445053481> **Message:** `{message.content}`", color=0xdbdbdb) #timestamp=message.created_at)
        await ctx.reply(embed=embed)

 



    @commands.group(name="Quarantine", help="Quarantine a user", usage="Quarantine <user>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def qarantine(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Quarantined | Sputnik")
        if not role:
            await ctx.guild.create_role(name="Quarantined | Sputnik")

        Quarantine = discord.utils.get(ctx.guild.text_channels, name="Quarantined")
        if not jail:
            try:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
                }            
                Quarantine = await ctx.guild.create_text_channel("Quarantined", overwrites=overwrites)
                await ctx.send(embed=discord.Embed(title="Quarantine Settings!", description="Your server has no jail channel, I created one for you %s" % (Quarantined.mention), color=0xdbdbdb))
            except discord.Forbidden:
                return await ctx.send(embed=discord.Embed(title="Quarantine Settings!", help="Please give me permissions, I am unable to create the `Quarantined` channel", color=0xdbdbdb))

        for channel in ctx.guild.channels:
            if channel.name == "Quarantined":
                perms = channel.overwrites_for(member)
                perms.send_messages = True
                perms.read_messages = True
                await channel.set_permissions(member, overwrite=perms)
            else:
                perms = channel.overwrites_for(member)
                perms.send_messages = False
                perms.read_messages = False
                perms.view_channel = False
                await channel.set_permissions(member, overwrite=perms)

        role = discord.utils.get(ctx.guild.roles, name="Quarantined | Sputnik")
        await member.add_roles(role)

        await jail.send(content=member.mention, embed=discord.Embed(title="jail", description="Please live out your jail sentence until the court lets you free.", color=0x00FFE4))
        await ctx.send(embed=discord.Embed(title="jail", description="Successfully jailed **`%s`**" % (member.name), color=0x00FFE4))
        await member.send(embed=discord.Embed(title="jail", description="You have been jailed in **`%s`** by **`%s`**" % (ctx.guild.name, ctx.author.name), color=0x00FFE4))

    @commands.group(name="Unquarantine", help="Unjails a user", usage="unquarantine <user>",  aliases=["uq"])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def unquarantine(self, ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Quarantined | Sputnik")
        for channel in ctx.guild.channels:
            if channel.name == "Quarantine":
                perms = channel.overwrites_for(member)
                perms.send_messages = None
                perms.read_messages = None
                await channel.set_permissions(member, overwrite=perms)
            else:
                perms = channel.overwrites_for(member)
                perms.send_messages = None
                perms.read_messages = None
                perms.view_channel = None
                await channel.set_permissions(member, overwrite=perms)

        await member.remove_roles(role)
        await ctx.send(embed=discord.Embed(title="unjail", description="Successfully unjailed **`%s`**" % (member.name), color=self.color))
        await member.send(embed=discord.Embed(title="unjail", description="you have been unjailed in **`%s`** by **`%s`**" % (ctx.guild.name, ctx.author.name), color=0xdbdbdb))

    @commands.group(name="cleanup", help="deletes the bots messages", aliases=["purgebots"], usage="cleanup <amount>")
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def cleanup(self, ctx, amount: int):
        msg = await ctx.send("cleaning...")
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                if message.id == msg.id:
                    pass
                else:
                    await message.delete()
            except:
                pass
        await msg.edit(content="cleaned up successfully 👌")




