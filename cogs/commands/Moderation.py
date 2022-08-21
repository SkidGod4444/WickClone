import discord
from discord.ext import commands
from core import Cog, Darkz, Context
from discord.ui import Button, View
import datetime
from typing import Optional
from utils.Tools import *

class Moderation(Cog):
  """Sends a list of usable commands for this server."""
  def __init__(self, client: Darkz):
    self.client = client

  def convert(self, time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]

  @commands.command(name="prefix", aliases=["setprefix", "set-prefix", "prefixset", "prefix-set"], help="Allows you to change prefix of the bot for this server")
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _prefix(self, ctx, prefix):

        data = getConfig(ctx.guild.id)
        data["prefix"] = str(prefix)  
        updateConfig(ctx.guild.id, data)
        await ctx.reply(f"Successfully Changed Prefix For This Server\nNew Prefix Is: `{prefix}`\nUse `{prefix}help` For More!", mention_author=False)

  @commands.command(name="lock", help="Locks the channel")
  @blacklist_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _lock(self, ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Locked By {ctx.author}")
    await ctx.reply(f"Succefully Locked {channel.mention}", mention_author=False)

  
  @commands.command(name="unlock", help="Unlocks the channel")
  @blacklist_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _unlock(self, ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unlocked By {ctx.author}")
    await ctx.reply(f"Succefully Unlocked {channel.mention}", mention_author=False)

  @commands.command(name="hide", help="Hides the channel")
  @blacklist_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _hide(self, ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Hidden By {ctx.author}")
    await ctx.reply(f"Succefully Hidden {channel.mention}", mention_author=False)

  @commands.command(name="unhide", help="Locks the channel")
  @blacklist_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _unhide(self, ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await channel.set_permissions(ctx.guild.default_role,
                                  overwrite=overwrite,
                                  reason=f"Channel Unhidden By {ctx.author}")
    await ctx.reply(f"Succefully Unhidden {channel.mention}", mention_author=False)

  @commands.command(name='kick', help="Somebody is breaking rules simply kick him from the server as punishment")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(kick_members=True)
  async def _kick(self, ctx, member: discord.Member, *, reason: Optional[str]=None):
    if ctx.author == ctx.guild.owner:
      if ctx.guild.me.top_role > member.top_role:
        try:
            await member.kick(reason=f"{ctx.author}, Reason: {reason}")
            await member.send(
                f"**You got Kicked from {ctx.guild.name} , reason = {reason}**"
            )
            await ctx.reply(
                f'✅ | Successfully Kicked {member} | Use $help For my commands', mention_author=False
            )
        except:

            await member.kick(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.reply(
                f'✅ | Successfully Kicked {member} | Use $help For my commands', mention_author=False
            )
      else:
        await ctx.reply(f"❌ | My highest role is below or equal to {member.mention}")
    elif ctx.guild.me.top_role >= ctx.author.top_role:
        await ctx.reply(
            '❌ | You Must Be Higher Then Me To Use This Command', mention_author=False
        )
        return
    elif member == ctx.author:
        await ctx.reply(
            "❌ | You cannot kick yourself", mention_author=False)
    else:
      if ctx.guild.me.top_role > member.top_role:
        try:
            await member.kick(reason=f"{ctx.author}, Reason: {reason}")
            await member.send(
                f"**You got Kicked from {ctx.guild.name} , reason = {reason}**"
            )
            await ctx.reply(
                f'✅ | Successfully Kicked {member} | Use $help For my commands', mention_author=False
            )
        except:
            await member.kick(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.reply(
                f'✅ | Succesfully Kicked {member} | Use $help For my commands', mention_author=False
            )
      else:
        await ctx.reply(f"❌ | My highest role is below or equal to {member.mention}")

  @commands.command(name='ban', help="Somebody is breaking rules again and again | ban him from the server as punishment")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def _ban(self, ctx, member: discord.Member, *, reason: Optional[str]=None):
    if ctx.author == ctx.guild.owner:
      if ctx.guild.me.top_role > member.top_role:
        try:
            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await member.send(
                f"**You got Banned from {ctx.guild.name} , reason = {reason}**"
            )
            await ctx.reply(
                f'✅ | Successfully Banned {member} | Use $help For my commands', mention_author=False
            )
        except:

            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.reply(
                f'✅ | Successfully Banned {member} | Use $help For my commands', mention_author=False
            )
      else:
        await ctx.reply(f"❌ | My highest role is below or equal to {member.mention}")
    elif ctx.guild.me.top_role >= ctx.author.top_role:
        await ctx.reply(
            '❌ | You Must Be Higher Then Me To Use This Command', mention_author=False
        )
        return
    elif member == ctx.author:
        await ctx.reply(
            "❌ | You cannot ban yourself", mention_author=False)
    else:
      if ctx.guild.me.top_role > member.top_role:
        try:
            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await member.send(
                f"**You got Banned from {ctx.guild.name} , reason = {reason}**"
            )
            await ctx.reply(
                f'✅ | Successfully Banned {member} | Use $help For my commands', mention_author=False
            )
        except:
            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.reply(
                f'✅ | Succesfully Banned {member} | Use $help For my commands', mention_author=False
            )
      else:
        await ctx.reply(f"❌ | My highest role is below or equal to {member.mention}")

  @commands.command(name='softban', help="Literally trolling command or you can use to clear all messages by the user.", aliases=["soft-ban"])
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def _softban(self, ctx, member: discord.Member, *, reason: Optional[str]=None):
    if ctx.author == ctx.guild.owner:
        try:
            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.guild.unban(discord.Object(member.id), reason=f"{ctx.author}, Reason: {reason}")
            await member.send(
                f"**You got Soft-Banned from {ctx.guild.name} , reason = {reason}**"
            )
            await ctx.reply(
                f'✅ | Successfully SoftBanned {member} | Use $help For my commands', mention_author=False
            )
        except:

            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.guild.unban(discord.Object(member.id), reason=f"{ctx.author}, Reason: {reason}")
            await ctx.reply(
                f'✅ | Successfully SoftBanned {member} | Use $help For my commands', mention_author=False
            )
    elif ctx.guild.me.top_role >= ctx.author.top_role:
        await ctx.reply(
            '❌ | You Must Be Higher Then Me To Use This Command', mention_author=False
        )
        return
    elif member == ctx.author:
        await ctx.reply(
            "❌ | You cannot softban yourself", mention_author=False)
    else:
        try:
            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.guild.unban(discord.Object(member.id), reason=f"{ctx.author}, Reason: {reason}")
            await member.send(
                f"**You got Soft-Banned from {ctx.guild.name} , reason = {reason}**"
            )
            await ctx.reply(
                f'✅ | Successfully SoftBanned {member} | Use $help For my commands', mention_author=False
            )
        except:
            await member.ban(reason=f"{ctx.author}, Reason: {reason}")
            await ctx.guild.unban(discord.Object(member.id), reason=f"{ctx.author}, Reason: {reason}")
            await ctx.reply(
                f'✅ | Succesfully SoftBanned {member} | Use $help For my commands', mention_author=False
            )

  @commands.command(name="unban", help="If someone realises his mistake you should unban him.")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(ban_members=True)
  async def _unban(self, ctx, user: discord.User, reason: str=None):
    try:
      otay = await self.client.fetch_user(user.id)
    except:
      await ctx.reply("❌ | User is invalid!")
    try:
      await ctx.guild.unban(discord.Object(otay.id), reason=f"{ctx.author}, Reason: {reason}")
      await ctx.reply(f"✅ | Successfully Unbanned {otay}")
    except:
      await ctx.reply(f"❌ | {otay} is not banned in this server")

  @commands.command(name="timeout", help="Mutes a specific member", aliases=["mute", "stfu"])
  @blacklist_check()
  @commands.cooldown(1, 20, commands.BucketType.member)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def _mute(self, ctx, member: discord.Member, duration):
    ok = duration[:-1]
    tame = self.convert(duration)
    till = duration[-1]
    if tame == -1:
      await ctx.reply(f"You didnt didnt gave time with correct unit\nExamples:\n{ctx.prefix}mute 10m {ctx.author}\n{ctx.prefix}mute 5h {ctx.author}", mention_author=False)
    elif tame == -2:
      await ctx.reply(f"Time must be an integer!", mention_author=False)
    else:
      if till.lower() == "d":
        t = datetime.timedelta(seconds=tame)
        msg = "Successfully Muted {0.mention} For {1} Day(s)".format(member, ok)
      elif till.lower() == "m":
        t = datetime.timedelta(seconds=tame)
        msg = "Successfully Muted {0.mention} For {1} Minute(s)".format(member, ok)
      elif till.lower() == "s":
        t = datetime.timedelta(seconds=tame)
        msg = "Successfully Muted {0.mention} For {1} Second(s)".format(member, ok)
      elif till.lower() == "h":
        t = datetime.timedelta(seconds=tame)
        msg = "Successfully Muted {0.mention} For {1} Hour(s)".format(member, ok)

    try:
      if member.guild_permissions.administrator:
        await ctx.reply("I can\'t mute administrators")
      else:
        await member.timeout(discord.utils.utcnow() + t, reason="Command By: {0}".format(ctx.author))
        await ctx.send(msg)
    except:
      await ctx.send("An error occurred")

  @commands.command(name="untimeout", aliases=["unmute", "unshut"], help="Unmutes a member")
  @blacklist_check()
  @commands.cooldown(1, 20, commands.BucketType.member)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def _unmute(self, ctx, member: discord.Member):
    if member.is_timed_out():
      try:
        await member.edit(timed_out_until=None)
      except Exception as e:
        await ctx.send("Unable to Remove Timeout:\n```py\n{}```".format(e))
    else:
      await ctx.send("{} Is Not Muted".format(member.mention))

  @commands.command(help="Unbans Everyone In The Guild!", aliases=['massunban'])
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only() 
  @commands.has_permissions(ban_members=True)
  async def unbanall(self, ctx):
      button = Button(label="Yes", style=discord.ButtonStyle.green, emoji="<:success_ok:946729333274337350>")
      button1 = Button(label="No", style=discord.ButtonStyle.red, emoji="<:error_ok:946729104126922802>")
      async def button_callback(interaction: discord.Interaction):
        a = 0
        if interaction.user == ctx.author:
          if interaction.guild.me.guild_permissions.ban_members:
            await interaction.response.edit_message(content=f"Unbanning All Banned Member(s)", embed=None, view=None)
            async for idk in interaction.guild.bans(limit=None):
              await interaction.guild.unban(user=idk.user, reason="Unbanall Command Executed By: {}".format(ctx.author))
              a += 1

            
            await interaction.channel.send(content=f"Successfully Unbanned {a} Member(s)")
          else:
            await interaction.response.edit_message(content="I am missing ban members permission.\ntry giving me permissions and retry", embed=None, view=None)
        else:
          await interaction.response.send_message("This Is Not For You Dummy!", embed=None, view=None, ephemeral=True)
      async def button1_callback(interaction: discord.Interaction):
        if interaction.user == ctx.author:
          await interaction.response.edit_message(content="Ok I will not unban anyone in this guild", embed=None, view=None)
        else:
          await interaction.response.send_message("This Is Not For You Dummy!", embed=None, view=None, ephemeral=True)
   # if ctx.guild.me.guild_permissions.ban_members:
      embed = discord.Embed(title='Confirmation',
                          color=000000,
                          description=f'**Are you sure you want to unban everyone in this guild?**')
      view = View()
      button.callback = button_callback
      button1.callback = button1_callback
      view.add_item(button)
      view.add_item(button1)
      await ctx.reply(embed=embed, view=view, mention_author=False)
