from discord.ext import commands
from utils.Tools import *
import discord
from core import Cog, Astroz, Context

class Raidmode(Cog):
  """Setup Anti-raid in your server!"""
  def __init__(self, client: Astroz):
    self.client = client

  @commands.command(name="automod", aliases=["Automoderation"], help="Shows help about Automoderation feature of bot.")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antiraid(self, ctx):
    data = getConfig(ctx.guild.id)
    spam = data["antiSpam"]
    link = data["antiLink"]
    punish = data["punishment"]
    embed = discord.Embed(title="Antiraid Settings!",
                          description="Raidmode Commands",color=0xdbdbdb)  
    embed.add_field(name="<:1spacer:1056545806943006760><:rightshort:1053176997481828452> antispam on/off",
                    value=f"Enables/Disables antispam feature\nCurrently Its `{spam}`",
                    inline=False)  
    embed.add_field(name="<:1spacer:1056545806943006760><:rightshort:1053176997481828452> antilink on/off",
                    value=f"Enables/Disables antilink feature\nCurrently Its `{link}`",
                    inline=False)
    embed.add_field(name="<:1spacer:1056545806943006760><:rightshort:1053176997481828452> punishment kick/ban/none",
                    value=f"Sets Punishment For Anti-Nuke + Raidmode Feature\nCurrently Its `{punish}`",
                    inline=False)
    #embed.set_footer(text="Anti-Raid Features")
    await ctx.reply(embed=embed, mention_author=False)

  @commands.command(name="antispam", aliases=['anti-spam'], help="Enables or Disables anti spam feature")
  @blacklist_check()

 # @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antispam(self, ctx: Context, type: str):
    
        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner
        admin = data["admin"]
        mod = data["mod"]

        if ctx.author == owner or str(ctx.author.id) in admin or str(ctx.author.id) in mod:
            if onOroff == "on":
                if data["antiSpam"] is True:
                    hacker = discord.Embed(title="Antiraid System!",
                          description=f"Anti-Spam is already enabled in **`{ctx.guild.name}`**",color=0xdbdbdb)  
                    await ctx.reply(embed=hacker, mention_author=False)
                else:
                    data["antiSpam"] = True
                    updateConfig(ctx.guild.id, data)
                    hacker1 = discord.Embed(title="Antiraid Settings!",
                          description=f"Successfully enabled anti-spam in **`{ctx.guild.name}`**",color=0xdbdbdb)  
                    await ctx.reply(embed=hacker1, mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiSpam"] = False
                updateConfig(ctx.guild.id, data)
                hacker2 = discord.Embed(title="Antiraid System!",
                          description=f"Successfully disabled anti-spam in **`{ctx.guild.name}`**",color=0xdbdbdb)  
                await ctx.reply(embed=hacker2, mention_author=False)
            else:
                hacker3 = discord.Embed(title="Automoderation!",
                          description=f"Invalid Value.\nIt Should Be On/Off",color=0xdbdbdb)  
                await ctx.reply(embed=hacker3, mention_author=False)

        else:
            hacker5 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `Antinuke mod/admin`!")
            await ctx.reply(embed=hacker5, mention_author=False)

  @commands.command(aliases=['anti-link'], name="antilink", help="Enables or Disables antilink feature")
  @blacklist_check()

 # @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antilink(self, ctx: Context, type: str):

        onOroff = type.lower()

        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner
        admin = data["admin"]
        mod = data["mod"]

        if ctx.author == owner or str(ctx.author.id) in admin or str(ctx.author.id) in mod:#if ctx.author == owner:
            if onOroff == "on":
                if data["antiLink"] is True:
                    hacker = discord.Embed(title="Antiraid Settings!",
                          description=f"Anti-link is already enabled in **`{ctx.guild.name}`**",color=0xdbdbdb)  
                    await ctx.reply(embed=hacker, mention_author=False)
                else:
                    data["antiLink"] = True
                    updateConfig(ctx.guild.id, data)
                    hacker1 = discord.Embed(title="Antiraid Settings!",
                          description=f"Successfully enabled anti-link!",color=0xdbdbdb)  
                    await ctx.reply(embed=hacker1, mention_author=False)

            elif onOroff == "off":
                data = getConfig(ctx.guild.id)
                data["antiLink"] = False
                updateConfig(ctx.guild.id, data)
                hacker2 = discord.Embed(title="Antiraid Settings!",
                          description=f"Successfully disabled anti-link!",color=0xdbdbdb)  
                await ctx.reply(embed=hacker2, mention_author=False)
            else:
                hacker3 = discord.Embed(title="Antiraid Settings!",
                          description=f" Invalid Value.\nIt Should Be On/Off",color=0xdbdbdb)  
                await ctx.reply(embed=hacker3, mention_author=False)

        else:
            hacker5 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `Antinuke mod/admin`!")
            await ctx.reply(embed=hacker5, mention_author=False)