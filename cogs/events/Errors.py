import discord, json
from discord.ext import commands
from core import Astroz, Cog, Context

class Errors(Cog):
  def __init__(self, client:Astroz):
    self.client = client
    print(f"Cog Loaded: {self.__class__.__name__}")

  @commands.Cog.listener()
  async def on_command_error(self, ctx: Context, error):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if isinstance(error, commands.CommandNotFound):
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)
    elif isinstance(error, commands.NoPrivateMessage):
      hacker = discord.Embed(color=0xdbdbdb,description=f"You Can\'t Use My Commands In Dm(s)", timestamp=ctx.message.created_at)
      hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
      hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
    elif isinstance(error, commands.TooManyArguments):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, commands.CommandOnCooldown):
      hacker = discord.Embed(color=0xdbdbdb, title="Cooldown!",description=f"<:person:1053178413478838312> **Moderator:** `{ctx.author.name}`\n<:tiktik:1056815610199285800> **Time:** `{error.retry_after:.2f}` second(s)\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> This Command is on cooldown retry after `{error.retry_after:.2f}` second(s)!", timestamp=ctx.message.created_at)
      #hacker.set_author(name=f"Cooldown!")
    #  hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
    elif isinstance(error, commands.MaxConcurrencyReached):
      hacker = discord.Embed(color=0xdbdbdb,title="Running Command!",description=f"<:person:1053178413478838312> **Moderator:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> This Command is already going on, let it finish and retry after", timestamp=ctx.message.created_at)
    #  hacker.set_author(name=f"Running Command!")
     # hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
      ctx.command.reset_cooldown(ctx)
    elif isinstance(error, commands.MissingPermissions):
      missing = [
                perm.replace("_", " ").replace("guild", "server").title()
                for perm in error.missing_permissions
            ]
      if len(missing) > 2:
                fmt = "{}, and {}".format(", ".join(missing[:-1]), missing[-1])
      else:
                fmt = " and ".join(missing)
      hacker = discord.Embed(color=0xdbdbdb,title="Permission Lacking!",description=f"<:person:1053178413478838312> **Moderator:** `{ctx.author.name}`\n<:ellor:1056829282858573925> **Permission(s):** `{fmt}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> You are lacking permissions to use this command!", timestamp=ctx.message.created_at)
   #   hacker.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
     # hacker.set_thumbnail(url =f"{ctx.author.avatar}")
      await ctx.reply(embed=hacker)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, commands.BadArgument):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, discord.HTTPException):
      pass
    elif isinstance(error, commands.CommandInvokeError):
      pass
    elif isinstance(error, commands.CheckFailure):
      if str(ctx.author.id) in data["ids"]:
        embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User!", description="\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> **Reason:** `Spamming My Commands`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> You Are Blacklisted From Using My Commands.\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> Join my [Support Server](https://discord.gg/3YmDAzbuRR) to appeal.", color=0xdbdbdb)
        await ctx.reply(embed=embed, mention_author=False)
