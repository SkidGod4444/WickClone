from __future__ import annotations
from discord.ext import commands
from core import Cog, Astroz, Context
import discord
from utils.Tools import *
from discord.ui import Button, View
import datetime
from typing import Optional


class Security(Cog):
  """Shows a list of commands regarding antinuke"""
  def __init__(self, client:Astroz):
    self.client = client

  @commands.group(name="Antinuke", aliases=["anti", "Security"], help="Enables/Disables antinuke in your server!", invoke_without_command=True, usage="Antinuke Enable/Disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antinuke(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antinuke.command(name="enable", help="Server owner should enable antinuke for the server!",usage="Antinuke Enable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_enable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    mod = d2["mod"]
    admin = d2["admin"]
    #if str(ctx.author.user.id) in mod: #or ctx.author == ctx.guild.owner_id:
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id: 
    
   # str(ctx.author.user.id) in mod:
      if data == "on":
        embed = discord.Embed(title="Already Enabled!", description=f"**[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n**[2]. Status:**\n<:1spacer:1056545806943006760><:tixk:1053178188613820468> **Alredy Enabled**\n**[3]. Punishment:**\n<:1spacer:1056545806943006760><:punish:1056860249212059688> `{punish}`\n**[4]. Whitelisted Users:**\n<:1spacer:1056545806943006760><:WhitelistWebhook:1058042975529214015> `{len(wled)} whitelisted`", color=0xdbdbdb)
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateanti(ctx.guild.id, data)
        embed2 = discord.Embed(title="Security Enabled!", description=f" **[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:tiktik:1056815610199285800> **Interval:** `6hours`\n**[2]. Status:**\n<:1spacer:1056545806943006760><:tixk:1053178188613820468> **Enabled**\n**[3]. Punishment:**\n<:1spacer:1056545806943006760><:punish:1056860249212059688> `{punish}`\n**[4]. Whitelisted Users:**\n<:1spacer:1056545806943006760><:WhitelistWebhook:1058042975529214015> `{len(wled)} whitelisted`", color=0xdbdbdb)
   #  embed2.add_field(name="Manual Punishment:", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> To change the punishment type, do `s!antinuke punishment set <Ban\Kick\None>`.")
    #  embed2.set_footer(text=f"~ Hell for Nukers")
      await ctx.reply(embed=embed2, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5, mention_author=False)

  @_antinuke.command(name="disable", help="You can disable antinuke for your server using this command", aliases=["off"],usage="Antinuke disable")
  @blacklist_check()

  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_disable(self, ctx: Context):
        
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    #wled = d2["whitelisted"]
    #punish = d2["punishment"]
    #mod = d2["mod"]
    admin = d2["admin"]
    #if str(ctx.author.user.id) in mod: #or ctx.author == ctx.guild.owner_id:
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
        
    
    #data = getanti(ctx.guild.id)
   # if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id:
      if data == "off":
        emb = discord.Embed(title="Already Disabled!", description=f"**[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n**[2]. Status:**\n<:1spacer:1056545806943006760><:xross:1053176060759515218> **Disabled**",color=0xdbdbdb)
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateanti(ctx.guild.id, data)
        final = discord.Embed(title="Security Disabled!", description=f"**[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n**[2]. Status:**\n<:1spacer:1056545806943006760><:xross:1053176060759515218> **Disabled**",color=0xdbdbdb)
        await ctx.reply(embed=final, mention_author=False)

  @_antinuke.command(name="show", help="Shows currently antinuke config settings of your server", aliases=["config"],usage="Antinuke show")
  @blacklist_check()

  #@commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_show(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    admin = d2["admin"]
    punish = d2["punishment"]


    #if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:

    if data == "off":
      emb = discord.Embed(title="Unable to fetch!", description=f"**[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n**[2]. Status:**\n<:1spacer:1056545806943006760><:xross:1053176060759515218> **Disabled**\n**[3]. Suggestion:**\n<:1spacer:1056545806943006760><:urrow:1053243283549204520> **Type `s!antinuke enable` to use this command**",color=0xdbdbdb)
      await ctx.reply(embed=emb, mention_author=False)
    elif data == "on":
      embed2 = discord.Embed(title="Security Settings", description=f" **[1]. Scanning:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** `{ctx.guild.owner}`\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:tiktik:1056815610199285800> **Interval:** `6hours`\n**[2]. Security Status:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Bot:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Ban:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Kick:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Prune:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Channel:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Role:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Webhook:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Emoji:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Guild Update:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Community Spam:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Integration Create:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Anti Everyone/Here/Role Ping:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **[<a:premium:1056725098641494167>] Anti Vanity Snipe:** | <:tixk:1053178188613820468> **Enabled**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **[<a:premium:1056725098641494167>] Auto Recovery:** | <:tixk:1053178188613820468> **Enabled**\n**[3]. Whitelisted Users:**\n<:1spacer:1056545806943006760><:WhitelistWebhook:1058042975529214015> `{len(wled)}` whitelisted\n**[4]. Security Punishment:**\n<:1spacer:1056545806943006760><:punish:1056860249212059688> `{punish}`", color=0xdbdbdb)
     # embed2.add_field(name="Other Settings", value=f"To change the punishment type `{ctx.prefix}Antinuke punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`.")
      embed2.set_footer(text=f"Current Punishment Type Is {punish}")
      await ctx.reply(embed=embed2, mention_author=False)
  @_antinuke.command(name="recover", help="Deletes all channels with name of rules and moderator-only",usage="Antinuke recover")
  @blacklist_check()

  #@commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _recover(self, ctx: Context):
        
    
    #if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()
            except:
                pass
    await ctx.reply("Successfully Deleted All Channels With Name Of `rules, moderator-only`", mention_author=False)

  @_antinuke.group(name="punishment", help="Changes Punishment of antinuke and antiraid for this server.", invoke_without_command=True,usage="Antinuke punishment set/show")
  @blacklist_check()
#  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _punishment(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_punishment.command(name="set", help="Changes Punishment of antinuke and automod for this server.", aliases=["change"],usage="Antinuke punishment set <none>")
  @blacklist_check()

  #@commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_set(self, ctx, punishment: str):
        data = getConfig(ctx.guild.id)
        admin = data["admin"]
        owner = ctx.guild.owner
        if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:#if ctx.author == owner:

            kickOrBan = punishment.lower()

            if kickOrBan == "kick":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "kick"
                hacker = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",color=0x00FFE4)
                await ctx.reply(embed=hacker, mention_author=False)

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "ban":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "ban"
                hacker1 = discord.Embed(title="Security Settings!", description=f"<:GreenTick:1029990379623292938> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",color=0xdbdbdb)
                await ctx.reply(embed=hacker1, mention_author=False)

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "none":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "none"
                hacker3 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Changed Punishment To: **{kickOrBan}** For {ctx.guild.name}",color=0x00FFE4)
                await ctx.reply(embed=hacker3, mention_author=False)

                updateConfig(ctx.guild.id, data)
            else:
               hacker5 = discord.Embed(title="Astroz Security", description=f"Invalid Punishment Type\nValid Punishment Type(s) Are: Kick, Ban, None",color=0x00FFE4)
               await ctx.reply(embed=hacker5, mention_author=False)

        else:
            hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
            await ctx.reply(embed=hacker5, mention_author=False)

  @_punishment.command(name="show", help="Shows custom punishment type for this server",usage="Antinuke punishment show")
  @blacklist_check()
#  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_show(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    punish = data["punishment"]
    hacker5 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description="Custom punishment of anti-nuke and automod is: **{}**".format(punish.title()))
    await ctx.reply(embed=hacker5,mention_author=False)
  @_antinuke.command(name="setvanity", aliases=['vanityset', 'vanity'], help="Sets vanity code in database and reverts when server vanity is changed",usage="Antinuke setvanity <vanity_code>")
  @blacklist_check()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _setvanity(self, ctx: Context, vanity_code: str):
  
        if not ctx.guild.premium_tier == 3:
            hacker5 = discord.Embed(title="Security Settings!", description=f"Your Servers Vanity Is Locked Try After Reaching Lvl3",color=0xdbdbdb)
            await ctx.reply(embed=hacker5)
        else:
          if ctx.author.id == ctx.guild.owner_id:
            if "https://discord.gg/" in vanity_code:
              idk = vanity_code.replace("https://discord.gg/", "")
            elif "discord.gg/" in vanity_code:
              idk = vanity_code.replace("discord.gg/", "")
            elif "discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("discord.com/invite", "")
            elif "https://discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("https://discord.com/invite/", "")
            else:
              idk = vanity_code
            update_vanity(ctx.guild.id, idk)
            hacker = discord.Embed(title="Security Settings!", description=f"<:GreenTick:1029990379623292938> | Successfully Set Vanity For {ctx.guild.name} To {idk}",color=0xdbdbdb)         
            await ctx.reply(embed=hacker, mention_author=False)
          elif ctx.author.id == 967791712942583818:
            if "https://discord.gg/" in vanity_code:
              idk = vanity_code.replace("https://discord.gg/", "")
            elif "discord.gg/" in vanity_code:
              idk = vanity_code.replace("discord.gg/", "")
            elif "discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("discord.com/invite", "")
            elif "https://discord.com/invite/" in vanity_code:
              idk = vanity_code.replace("https://discord.com/invite/", "")
            else:
              idk = vanity_code
            update_vanity(ctx.guild.id, idk)
            hacker1 = discord.Embed(title="Security Settings!", description=f"Successfully Set Vanity For {ctx.guild.name} To {idk}",color=0xdbdbdb)         
            await ctx.reply(embed=hacker1, mention_author=False)
          else:
            hacker4 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
            await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.command(name="channelclean", aliases=['cc'], help="deletes channel with similar name provided.",usage="Antinuke channelclean <none>")
  @blacklist_check()

  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
 # @commands.has_permissions(manage_channels=True)
  async def _channelclean(self, ctx: Context, channeltodelete: str):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    owner = ctx.guild.owner
       # if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
    if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in admin:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      hacker1 = discord.Embed(title="Security Settings!", description=f"Successfully Deleted All Channels With The Name Of {channeltodelete}",color=0xdbdbdb)         
      await ctx.reply(embed=hacker1, mention_author=False)
    elif ctx.author.id == 967791712942583818:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      hacker2 = discord.Embed(title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Deleted All Channels With The Name Of {channeltodelete}",color=0x00FFE4)         
      await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker4 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.command(name="roleclean", aliases=['cr'], help="deletes role with similar name provided",usage="Antinuke roleclean <none>")
  @blacklist_check()

  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
 # @commands.has_permissions(manage_roles=True)
  async def _roleclean(self, ctx: Context, roletodelete: str):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    owner = ctx.guild.owner




    if ctx.author.id == ctx.guild.owner_id or str(ctx.author.id) in admin:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      hacker = discord.Embed(title="Security Settings!", description=f"Successfully Deleted All Roles With The Given Name {roletodelete}",color=0xdbdbdb)         
      await ctx.reply(embed=hacker, mention_author=False)
    elif ctx.author.id == 967791712942583818:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      hacker3 = discord.Embed(title="Security Settings!", description=f"Successfully Deleted All Roles With The Given Name {roletodelete}",color=0xdbdbdb)
                             
      await ctx.reply(embed=hacker3, mention_author=False)
    else:
      hacker4 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker4, mention_author=False)

  @_antinuke.group(name="whitelist", aliases=["wl"], help="Whitelist your TRUSTED users for anti-nuke", invoke_without_command=True,usage="Antinuke whitelist add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _whitelist(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)
      
  @_whitelist.command(name="add", help="Add a user to whitelisted users",usage="Antinuke whitelist add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def whitelist_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if len(wled) == 15:
        hacker = discord.Embed(title="Security Settings!", description=f"Sorry this server have already maximum number of whitelisted users!)",color=0xdbdbdb)
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in wled:
          hacker1 = discord.Embed(title="Already Whitelisted!", description=f" That user is already in my whitelist.",color=0xdbdbdbd)          
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          wled.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Successfully Whitelisted {user.mention}")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)
#########


      
  @_whitelist.command(name="remove", help="Remove a user from whitelisted users",usage="Antinuke whitelist remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def whitelist_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if str(user.id) in wled:
        wled.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Successfully Unwhitelisted {user.mention}!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description="This user is not in my whitelist system!.")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5, mention_author=False)

  @_whitelist.command(name="show", help="Shows list of whitelisted users in the server.",usage="Antinuke whitelist show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_show(self, ctx):
      #data = getConfig(ctx.guild.id)
      data = getConfig(ctx.guild.id)
      admin = data["admin"]
      wled = data["whitelisted"]
     # if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:
     # wled = data["whitelisted"]
      if len(wled) == 0:
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f" There aren\'t any whitelised users for this server")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(title=f"Security Whitelised!", description="\n", color=0xdbdbdb)
      for idk in wled:
        embed.description += f"<@{idk}> | ID: {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)


  @_whitelist.command(name="reset", help="removes every user from whitelist database", aliases=["clear"],usage="Antinuke whitelist reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def wl_reset(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id:
      #data = getConfig(ctx.guild.id)
     # admin = data["admin"]
    # if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:  
      data["whitelisted"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed(color=0x00FFE4,title="Astroz Security", description=f"<:GreenTick:1029990379623292938> | Successfully Cleared Whitelist Database For **{ctx.guild.name}**")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)

  @_antinuke.group(name="mod", help="Whitelist your TRUSTED users for anti-nuke-mod", invoke_without_command=True,usage="Antinuke Moderator add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _mod(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_mod.command(name="add", help="Add a user to antinuke-mod",usage="Antinuke mod add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def mod_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if len(mod) == 4:
        hacker = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> This server has reached the max no.of `antinuke mods` remove one to add another.",color=0xdbdbdb)
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in mod:
          hacker1 = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> That user is already an `antinuke mod` in this server! ",color=0xdbdbdb)          
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          mod.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> Successfully added as `antinuke mod` now you can make changes!")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)
#########
      
  @_mod.command(name="remove", help="Remove a user from antinuke mod users",usage="Antinuke mod remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def mod_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if str(ctx.author.id) in admin or ctx.author == owner:#if ctx.author == owner:
      if str(user.id) in mod:
        mod.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> Successfully removed from `antinuke mod` now that user can't make changes!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> That user is not a `antinuke mod` in this server! ")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5, mention_author=False)

  @_mod.command(name="show", help="Shows list of antinuke-mod users in the server.",usage="Antinuke mod show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def mod_show(self, ctx):
      data = getConfig(ctx.guild.id)
      mod = data["mod"]
      if len(mod) == 0:
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistRole:1058042681772740629> **Mods:** `No one is there as antinuke mod! in this server.`")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistRole:1058042681772740629> **Mods:**\n", color=0xdbdbdb)
      for idk in mod:
        embed.description += f"<:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><@{idk}> `:` {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)
      
  @_mod.command(name="reset", help="removes every user from antinuke-mod database", aliases=["clear"],usage="Antinuke mod reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
 # @commands.has_permissions(administrator=True)
  async def mod_reset(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    if str(ctx.author.id) in admin or ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id:
      
      data["mod"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Successfully Cleared `Antinuke mods` Database!")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make you `antinuke admin`!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)

  @_antinuke.group(name="admin", help="Add your Trusted users for antinuke-admin", invoke_without_command=True,usage="Antinuke admin add/remove")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def _admin(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_admin.command(name="add", help="Add a user to antinuke-admin",usage="Antinuke admin add <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
#  @commands.has_permissions(administrator=True)
  async def admin_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
   # mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if ctx.author == owner:#if ctx.author == owner:
      if len(admin) == 2:
        hacker = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> This server has reached the max no.of `antinuke admins` remove one to add another.",color=0xdbdbdb)
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        if str(user.id) in admin:
          hacker1 = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> That user is already an `antinuke admin` in this server! ",color=0xdbdbdb)
          await ctx.reply(embed=hacker1, mention_author=False)
        else:
          admin.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          hacker4 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> Successfully added as `antinuke admin` now you can make changes!")
          await ctx.reply(embed=hacker4, mention_author=False)

    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)
#########

  @_admin.command(name="remove",help="Remove a user from antinuke admin users",usage="Antinuke admin remove <user>")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def admin_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    #mod = data["mod"]
    admin = data["admin"]
    owner = ctx.guild.owner
    if ctx.author == owner:#if ctx.author == owner:
      if str(user.id) in admin:
        admin.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> Successfully removed from `antinuke admin` now that user can't make changes!")      
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        hacker2 = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistUser:1056918373381971998> **Victim:** {user.mention}\n<:rightshort:1053176997481828452> That user is not a `antinuke admin` in this server! ")  
        await ctx.reply(embed=hacker2, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5, mention_author=False)

  @_admin.command(name="show", help="Shows list of antinuke-admin users in the server.",usage="Antinuke admin show")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def admin_show(self, ctx):
      data = getConfig(ctx.guild.id)
      admin = data["admin"]
      if len(admin) == 0:
        hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistRole:1058042681772740629> **Admins:** `No one is there as antinuke admin! in this server.`")
        await ctx.reply(embed=hacker, mention_author=False)
      else:
        embed = discord.Embed(title="Security Settings!", description=f"<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:1spacer:1056545806943006760><:WhitelistRole:1058042681772740629> **Admins:**\n", color=0xdbdbdb)
      for idk in admin:
        embed.description += f"<:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><:1spacer:1056545806943006760><@{idk}> `:` {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)
      
  @_admin.command(name="reset", help="removes every user from antinuke-admin database", aliases=["clear"],usage="Antinuke admin reset")
  @blacklist_check()

  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  #@commands.has_permissions(administrator=True)
  async def admin_reset(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    admin = data["admin"]
    if ctx.author == ctx.guild.owner:#if ctx.author.id == ctx.guild.owner_id:
      
      data["admin"] = []
      updateConfig(ctx.guild.id, data)
      hacker = discord.Embed(color=0xdbdbdb,title="Security Settings!", description=f"Successfully Cleared `Antinuke admins` Database!")         
      await ctx.reply(embed=hacker, mention_author=False)
    else:
      hacker5 = discord.Embed(title="Security Settings!", description=f"** Security Alert!:**\n<:1spacer:1056545806943006760><:profile:1056855971839873054> **Server:** `{ctx.guild.name}`\n<:1spacer:1056545806943006760><:rowner:1053178553161760778> **Owner:** <@{ctx.guild.owner.id}>\n<:1spacer:1056545806943006760><:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:rightshort:1053176997481828452> Sorry you can't use this command ask guild owner to make changes!",color=0xdbdbdb)
      await ctx.reply(embed=hacker5)
      


