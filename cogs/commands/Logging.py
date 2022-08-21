import discord
from discord.ext import commands
from core import Darkz, Cog, Context
from utils.Tools import *
from typing import List

class Logging(Cog):
  """logging module to log anything which happens in server to send in a channel"""
  def __init__(self, client: Darkz):
    self.client = client
    self.no_mention = discord.AllowedMentions.none()
    
  async def get_log_webhook(self, ch):
        channel = self.client.get_channel(int(ch))
        if not channel:
            return None
        webhooks = await channel.webhooks()
        w = discord.utils.get(webhooks, name="Darkz Logs", user=self.client.user)
        if w is None:
            w = await channel.create_webhook(name="Darkz Logs")
        return w

  async def send_from_webhook(self, webhook: discord.Webhook, embed: discord.Embed, files: List[discord.File] = [], embeds: List[discord.Embed] = []):
        if webhook is None:
            return
        if embed is None:
            await webhook.send(
                allowed_mentions=self.no_mentions,
                avatar_url=self.client.user.display_avatar.url,
                files=files,
                embeds=embeds
            )
        else:
            await webhook.send(
                embed=embed,
                allowed_mentions=self.no_mentions,
                avatar_url=self.client.user.display_avatar.url,
                files=files
            )

  async def check_enabled(self, guild_id):
        g = getlogger(guild_id)
        if g['channel'] == "":
            return False
        else:
            return g

  @commands.group(name="logall", help="Enables/Disables All Logs At Once In A Particular Channel!", invoke_without_command=True)
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _logall(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_logall.command(name="enable", help="Enables Logging In A Given Channel", aliases=["on"])
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def logall_enable(self, ctx: Context, channel: discord.TextChannel):
    if ctx.author.id == ctx.guild.owner_id:
      data = getlogger(ctx.guild.id)
      chan = data["channel"]
      if chan == "":
        data["channel"] = str(channel.id)
        makelogger(ctx.guild.id, data)
        await ctx.reply("Successfully enabled logging in {} channel".format(channel.mention))
      elif int(chan) == int(channel.id):
        await ctx.reply("Logs are already enabled in that channel!")
      else:
        data["channel"] = str(channel.id)
        makelogger(ctx.guild.id, data)
        await ctx.reply("Successfully enabled logging in {} channel".format(channel.mention))
    else:
      await ctx.reply("Only owner can enable/disable logs in server!")


  @_logall.command(name="disable", help="Disables all the logs in the server", aliases=["off"])
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def logall_disable(self, ctx: Context):
    if ctx.author.id == ctx.guild.owner_id:
      data = getlogger(ctx.guild.id)
      data2 = getConfig(ctx.guild.id)
      prefix = data2["prefix"]
      if data["channel"] == "":
        await ctx.reply(f"Logging isnt enabled in this server!\nenable it by using `{prefix}logall enable <channel>`")
      else:
        data["channel"] = ""
        makelogger(ctx.guild.id, data)
        await ctx.reply("Successfully Disabled Logging In This Server!")

  @Cog.listener()
  async def on_member_ban(self, guild, member):
    data = getlogger(guild.id)
    chan = data["channel"]
    if chan != "":
      ch = self.client.get_channel(int(chan))
    else:
      return
    async for logs in guild.audit_logs(limit=1):
      if logs.action == discord.AuditLogAction.ban:
        embed = discord.Embed(description="A member have been banned from this server.", color=discord.Color.red())
        embed.add_field(name="Responsible mod", value=f"{logs.user} {logs.user.mention}", inline=False)
        embed.add_field(name="User", value=member, inline=False)
        embed.add_field(name="Reason", value=logs.reason if logs.reason else "No Reason")
        embed.set_author(name=member, icon_url=member.default_avatar)
        embed.set_footer(text="Ban", icon_url=logs.user.default_avatar)
        embed.timestamp = logs.created_at
        if ch:
          await ch.send(embed=embed)
        else:
          return


  @Cog.listener()
  async def on_member_unban(self, guild, member):
    data = getlogger(guild.id)
    chan = data["channel"]
    if chan != "":
      ch = self.client.get_channel(int(chan))
    else:
      return
    async for logs in guild.audit_logs(limit=1):
        if logs.action == discord.AuditLogAction.unban:
          embed = discord.Embed(description="A member have been unbanned from this server.", color=discord.Color.red())
          embed.add_field(name="Responsible mod", value=f"{logs.user} {logs.user.mention}", inline=False)
          embed.add_field(name="User", value=member, inline=False)
          embed.add_field(name="Reason", value=logs.reason if logs.reason else "No Reason")
          embed.set_author(name=member, icon_url=member.default_avatar)
          embed.set_footer(text="Unban", icon_url=logs.user.default_avatar)
          embed.timestamp = logs.created_at
          if ch:
            await ch.send(embed=embed)

  @Cog.listener()
  async def on_guild_channel_create(self, channel):
    guild = channel.guild
    data = getlogger(guild.id)
    chan = data["channel"]
    if chan != "":
      ch = self.client.get_channel(int(chan))
    else:
      return
    async for logs in guild.audit_logs(limit=1):
      if logs.action == discord.AuditLogAction.channel_create:
        embed = discord.Embed(color=discord.Color.green())
        if isinstance(channel, discord.TextChannel):
          description = "New text channel ({0}) created by {1.user.mention}".format(channel.mention, logs)
        elif isinstance(channel, discord.VoiceChannel):
          description = "New voice channel ({0}) created by {1.user.mention}".format(channel.mention, logs)
        elif isinstance(channel, discord.StageChannel):
          description = "New stage channel ({0}) created by {1.user.mention}".format(channel.mention, logs)
        embed.description = description
        embed.add_field(name="Name", value=f"{channel.name} (ID: {channel.id})", inline=False)
        embed.add_field(name="Position", value=channel.position, inline=False)
        embed.add_field(name="Category", value=f"{channel.category.name} (ID: {channel.category.id})" if channel.category else "No Category")
        embed.set_author(name=logs.user, icon_url=logs.user.avatar.url if logs.user.avatar.url else None)
        embed.set_footer(text="Channel Create", icon_url=logs.user.default_avatar)
        embed.timestamp = channel.created_at
        if ch:
          await ch.send(embed=embed)

  @Cog.listener()
  async def on_guild_channel_delete(self, channel):
    guild = channel.guild
    data = getlogger(guild.id)
    chan = data["channel"]
    if chan != "":
      ch = self.client.get_channel(int(chan))
    else:
      return
    async for logs in guild.audit_logs(limit=1):
      if logs.action == discord.AuditLogAction.channel_delete:
        embed = discord.Embed(color=discord.Color.red())
        if isinstance(channel, discord.TextChannel):
          description = "A text channel ({0}) deleted by {1.user.mention}".format(channel.mention, logs)
        elif isinstance(channel, discord.VoiceChannel):
          description = "A voice channel ({0}) deleted by {1.user.mention}".format(channel.mention, logs)
        elif isinstance(channel, discord.StageChannel):
          description = "A stage channel ({0}) deleted by {1.user.mention}".format(channel.mention, logs)
        embed.description = description
        embed.add_field(name="Name", value=f"{channel.name} (ID: {channel.id})", inline=False)
        embed.add_field(name="Position", value=channel.position, inline=False)
        embed.add_field(name="Category", value=f"{channel.category.name} (ID: {channel.category.id})" if channel.category else "No Category", inline=False)
        embed.set_author(name=logs.user)
        embed.set_footer(text="Channel Delete", icon_url=logs.user.default_avatar)
        embed.timestamp = channel.created_at
        if ch:
          await ch.send(embed=embed)

  @Cog.listener()
  async def on_member_join(self, member):
    guild = member.guild
    data = getlogger(guild.id)
    chan = data["channel"]
    if chan != "":
      ch = self.client.get_channel(int(chan))
    else:
      return
    if member.bot:
      async for logs in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
        embed = discord.Embed(title="A Bot Has Joined The Server!", description=f"Name: {member} | ID: {member.id}\n :bust_in_silhouette: Bot was created at: <t:{int(member.created_at.timestamp())}:R>")
        embed.add_field(name="Added By:", value=f"Name: {logs.user} | ID: {logs.user.id}")
        embed.set_thumbnail(url=member.default_avatar)
        embed.set_author(name=member, icon_url=member.default_avatar)
        embed.set_footer(text="Bot Added", icon_url=self.client.user.avatar.url)
    else:
      embed = discord.Embed(title="A Member Has Joined The Server!", description=f"Name: {member} | ID: {member.id}\n :bust_in_silhouette: Account was created at <t:{int(member.created_at.timestamp())}:R>", color=discord.Colour.green())
      embed.set_thumbnail(url=member.default_avatar)
      embed.set_author(name=member, icon_url=member.default_avatar)
      embed.set_footer(text="Member Joined", icon_url=self.client.user.avatar.url)
    embed.timestamp = member.created_at
    if ch:
      await ch.send(embed=embed)
      