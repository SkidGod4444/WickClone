import discord
from discord.ext import commands
import os
#os.system("pip install git+https://github.com/NotHerHacker/Discord-Games")
from core import Cog, Astroz, Context
import discord_games as games
from utils.Tools import *
from discord_games import button_games as btn
import json

def add_channel_to_ignore(user_id: int) -> None:
    with open("ignore.json", "r") as file:
        file_data = json.load(file)
        if str(user_id) in file_data["ids"]:
            return

        file_data["ids"].append(str(user_id))
    with open("ignore.json", "w") as file:
        json.dump(file_data, file, indent=4)


class Utils(Cog):
  """Utils"""
  def __init__(self, client:Astroz):
    self.client = client


    
    @commands.group(name="ignore", invoke_without_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @blacklist_check()
    async def _ignore(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_ignore.group(name="channel",
                   aliases=["chnl"],
                   invoke_without_command=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @blacklist_check()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def _channel(self, ctx):
        if ctx.subcommand_passed is None:
            await ctx.send_help(ctx.command)
            ctx.command.reset_cooldown(ctx)

    @_channel.command(name="add")
    @commands.has_permissions(administrator=True)
    async def channel_add(self, ctx: Context, channel: discord.TextChannel):
        if ctx.author == ctx.guild.owner or ctx.author.top_role.position > ctx.guild.me.top_role.position:
            with open('ignore.json', 'r') as ignore:
                ignores = json.load(ignore)
                if str(channel.id) in ignores["ids"]:
                    embed = discord.Embed(
                        title="Error!",
                        description=
                        f"{channel.mention} is already in ignore channel list .",
                        color=0x2f3136)
                    await ctx.reply(embed=embed, mention_author=False)
                else:
                    add_channel_to_ignore(channel.id)
                    embed = discord.Embed(
                        description=
                        f"Now onwards {channel.mention} will be ignored by the bot.",
                        color=0x2f3136)
                    await ctx.reply(embed=embed, mention_author=False)
        else:
            hacker5 = discord.Embed(
                description=
                """```diff\n - You must have Administrator permission.\n - Your top role should be above my top role. \n```""",
                color=0x2f3136)
            hacker5.set_author(name=f"{ctx.author.name}",
                               icon_url=f"{ctx.author.avatar}")
            await ctx.reply(embed=hacker5)
