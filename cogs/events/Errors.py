import discord, json
from discord.ext import commands
from utils.Tools import check_voter
from core import Darkz, Cog, Context

class Errors(Cog):
  def __init__(self, client: Darkz):
    self.client = client
    print(f"Cog Loaded: {self.__class__.__name__}")

  @commands.Cog.listener()
  async def on_command_error(self, ctx: Context, error):
    #vote = await check_voter(ctx.author.id)
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if isinstance(error, commands.CommandNotFound):
      return
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)
    elif isinstance(error, commands.NoPrivateMessage):
      await ctx.reply("You Can\'t Use My Commands In Dm(s)")
    elif isinstance(error, commands.TooManyArguments):
      await ctx.send_help(ctx.command)
      ctx.command.reset_cooldown(ctx)

    elif isinstance(error, commands.CommandOnCooldown):
      await ctx.reply(f"This Command Is On Cooldown For {error.retry_after:.2f} second(s)")
    elif isinstance(error, commands.MaxConcurrencyReached):
      await ctx.reply("This Command is already going on, let it finish and retry after")
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
      await ctx.reply(f"You lack `{fmt}` permission(s) to run `{ctx.command.name}` command!")
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
        embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
        await ctx.reply(embed=embed, mention_author=False)
      if ctx.command.name.lower() in ['jsk', 'jishaku', 'bdg', 'restart', 'sync', 'bl', 'blacklist', 'np']:
          await ctx.reply("This command can only be used by my Developers!", mention_author=False)
      else:
          embed = discord.Embed(color=discord.Colour(0x2f3136), description="this command is confined only to my voters.\nPlease vote me [here](https://top.gg/bot/852919423018598430/vote) to unlock command.")
          await ctx.reply(embed=embed, mention_author=False)

    #elif isinstance(error, commands.NotOwner):
      #await ctx.reply("This command can only be executed by my developers!")