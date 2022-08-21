from discord.ext import commands
from utils.Tools import *
import discord
from core import Cog, Darkz, Context

class Antiraid(Cog):
  """Enable/Disable Anti-raid in your server to be protected from unknown raids!"""
  def __init__(self, client: Darkz):
    self.client = client

  @commands.command(name="antiraid", aliases=["anti-raid"], help="Shows help about antiraid feature of bot.")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiraid(self, ctx):
    data = getConfig(ctx.guild.id)
    spam = data["antiSpam"]
    link = data["antiLink"]
    punish = data["punishment"]
    embed = discord.Embed(title="Darkz Security | Anti-Raid",
                          description="Anti-Raid Commands", color=discord.Colour(0x2f3136))  
    embed.add_field(name="<:stolen_emoji:973119620842139658> antispam on/off",
                    value=f"Enables/Disables antispam feature\nCurrently Its {spam}",
                    inline=False)  
    embed.add_field(name="<:stolen_emoji:973119620842139658> antilink on/off",
                    value=f"Enables/Disables antilink feature\nCurrently Its {link}",
                    inline=False)
    embed.add_field(name="<:stolen_emoji:973119620842139658> punishment kick/ban/none",
                    value=f"Sets Punishment For Anti-Nuke + Anti-Raid Feature\nCurrently Its {punish}",
                    inline=False)
    embed.set_footer(text="Anti-Raid Features")
    await ctx.reply(embed=embed, mention_author=False)

  @commands.command(name="antispam", aliases=['anti-spam'], help="Enables or Disables anti spam feature")
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antispam(self, ctx: Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner

        if ctx.author == owner:
            if onOroff == "on":
                if data["antiSpam"] is True:
                    await ctx.reply("Anti-Spam already enabled!", mention_author=False)
                else:
                    data["antiSpam"] = True
                    updateConfig(ctx.guild.id, data)
                    await ctx.reply("Anti-Spam enabled!", mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiSpam"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.reply("Anti-Spam disabled!", mention_author=False)
            else:
                await ctx.reply("Invalid Type.\nIt Should Be On/Off", mention_author=False)

        else:
            await ctx.reply("This Command Can Only Be Executed By This Servers Owner", mention_author=False)

  @commands.command(aliases=['anti-link'], name="antilink", help="Enables or Disables antilink feature")
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antilink(self, ctx: Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner

        if ctx.author == owner:
            if onOroff == "on":
                if data["antiLink"] is True:
                    await ctx.reply("Anti-Link already enabled!", mention_author=False)
                else:
                    data["antiLink"] = True
                    updateConfig(ctx.guild.id, data)
                    await ctx.reply("Anti-Link enabled!", mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiLink"] = False
                updateConfig(ctx.guild.id, data)
                await ctx.reply("Anti-Link disabled!", mention_author=False)
            else:
                await ctx.reply("Invalid Type.\nIt Should Be On/Off", mention_author=False)

        else:
            await ctx.reply("This Command Can Only Be Executed By This Server Owner", mention_author=False)
