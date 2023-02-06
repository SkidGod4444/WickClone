############MODULES#############
import discord
import requests
import aiohttp
import datetime
import random
from discord.ext import commands
from random import randint
from time import sleep
from utils.Tools import *
from core import Cog, Astroz, Context




def RandomColor(): 
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="To voice deafen a specific user.",usage="vcdeafen [member]") 
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcdeafen(self, ctx, user: discord.Member, * , reason=None):
        hacker = discord.Embed(color=0x00FFE4,description=f":GreenTick: | {user.display_name} has been deafened, for: {reason}", timestamp=ctx.message.created_at)
        hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=hacker)
        await user.edit(deafen = True)

    @commands.command(help="To voice mute a specific user.",usage="vcmute [member]")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcmute(self, ctx, member: discord.Member, * , reason=None):
        hacker = discord.Embed(color=0x00FFE4,description=f":GreenTick: | {member.display_name} has been muted, for: {reason}", timestamp=ctx.message.created_at)
        hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=hacker)
        await member.edit(mute = True)
    @commands.command(help="To voice unmute a specific user.",usage="vcunmute [member]")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcunmute(self, ctx, member: discord.Member):
        hacker = discord.Embed(color=0x00FFE4,description=f":GreenTick: | {member.display_name} has been unmuted.", timestamp=ctx.message.created_at)
        hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=hacker)
        await member.edit(mute = False)

    @commands.command(help="To voice undeafen a specific user.",usage="vcundeafen [member]")
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    async def vcundeafen(self, ctx, member: discord.Member):
        hacker = discord.Embed(color=0x00FFE4,description=f":black_astroz: | {member.display_name} has been undeafened.", timestamp=ctx.message.created_at)
        hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
        await ctx.send(embed=hacker)
        await member.edit(deafen = False)