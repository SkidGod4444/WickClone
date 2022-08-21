from __future__ import annotations
from discord.ext import commands
from core import Cog, Darkz, Context
import discord
from utils.Tools import *

class Antinuke(Cog):
  """Shows a list of commands regarding antinuke"""
  def __init__(self, client: Darkz):
    self.client = client

  @commands.group(name="antinuke", aliases=["anti", "security", "protection"], help="Enables/Disables antinuke in your server!", invoke_without_command=True)
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _antinuke(self, ctx: Context):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_antinuke.command(name="enable", help="Server owner should enable antinuke for the server!", aliases=["on"])
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_enable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    if ctx.author.id == ctx.guild.owner_id:
      if data == "on":
        embed = discord.Embed(title="Darkz Security", description=f"**{ctx.guild.name} security settings **<:role:977918310421237800>\nOhh uh! looks like your server has already enabled security\n\nCurrent Status: <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n\n> To disable use `antinuke disable`", color=discord.Colour(0x2f3136))
          
        await ctx.reply(embed=embed, mention_author=False)
      else:
        data = "on"
        updateanti(ctx.guild.id, data)
        embed2 = discord.Embed(title="Darkz Security", description=f"**{ctx.guild.name} security settings** <:role:977918310421237800>\nAlso move my role to top of roles for me to work properly.<:darkz:1001384193487544350>\n\nPunishments:\n\n**Anti Bot:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Ban:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Kick:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Prune:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Channel Create/Delete/Update:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Role Create/Delete/Update:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Webhook Create:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Emoji Create/Delete/Update:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Guild Update:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Community Spam:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Integration Create:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Everyone/Here Mention:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Anti Vanity Steal:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>\n**Whitelisted Users:** {len(wled)}\n\n**Auto Recovery:** <:disable_no:1001804850847301643><:enable_yes:1001804893671137280>", color=discord.Colour(0x2f3136))
        embed2.add_field(name="Other settings", value=f"To change the punishment type `{ctx.prefix}punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`.")
        embed2.set_footer(text=f"Current punishment type is {punish}")
        await ctx.reply(embed=embed2, mention_author=False)
    else:
      await ctx.reply("You must be the guild owner to use the command!", mention_author=False)

  @_antinuke.command(name="disable", help="You can disable antinuke for your server using this command", aliases=["off"])
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_disable(self, ctx: Context):
    data = getanti(ctx.guild.id)
    if ctx.author.id == ctx.guild.owner_id:
      if data == "off":
        emb = discord.Embed(title="Darkz Security", description=f"**{ctx.guild.name} security settings **<:role:977918310421237800>\nOhh NO! looks like your server has already disabled security\n\nCurrent Status: <:error_ok:946729104126922802>\n\n> To enable use `antinuke enable`")
        await ctx.reply(embed=emb, mention_author=False)
      else:
        data = "off"
        updateanti(ctx.guild.id, data)
        final = discord.Embed(title="Darkz Security", description=f"**{ctx.guild.name} security settings** <:role:977918310421237800>\nSuccessfully disabled security settings.\n\nCurrent Status: <:error_ok:946729104126922802>\n\n> To enable again use `antinuke enable`")
        await ctx.reply(embed=final, mention_author=False)

  @_antinuke.command(name="show", help="Shows currently antinuke config settings of your server", aliases=["config"])
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def antinuke_show(self, ctx: Context):
    data = getanti(ctx.guild.id)
    d2 = getConfig(ctx.guild.id)
    wled = d2["whitelisted"]
    punish = d2["punishment"]
    if data == "off":
      emb = discord.Embed(title="Darkz Security", description=f"**{ctx.guild.name} security settings **<:role:977918310421237800>\nOhh NO! looks like your server has already disabled security\n\nCurrent Status: <:error_ok:946729104126922802>\n\n> To enable use `antinuke enable`")
      await ctx.reply(embed=emb, mention_author=False)
    elif data == "on":
      embed2 = discord.Embed(title="Darkz Security", description=f"**{ctx.guild.name} security settings** <:role:977918310421237800>\nAlso move my role to top of roles for me to work properly.<:darkz:1001384193487544350>\n\nPunishments:\n\n**Anti Bot:** <:success_ok:946729333274337350>\n**Anti Ban:** <:success_ok:946729333274337350>\n**Anti Kick:** <:success_ok:946729333274337350>\n**Anti Prune:** <:success_ok:946729333274337350>\n**Anti Channel Create/Delete/Update:** <:success_ok:946729333274337350>\n**Anti Role Create/Delete/Update:** <:success_ok:946729333274337350>\n**Anti Webhook Create:** <:success_ok:946729333274337350>\n**Anti Emoji Create/Delete/Update:** <:success_ok:946729333274337350>\n**Anti Guild Update:** <:success_ok:946729333274337350>\n**Anti Community Spam:** <:success_ok:946729333274337350>\n**Anti Integration Create:** <:success_ok:946729333274337350>\n**Anti Everyone/Here/Role Mention:** <:success_ok:946729333274337350>\n**Anti Vanity Steal:** <:success_ok:946729333274337350>\n**Whitelisted Users:** {len(wled)}\n\n**Auto Recovery:** <:success_ok:946729333274337350>", color=discord.Colour(0x2f3136))
      embed2.add_field(name="Other settings", value=f"To change the punishment type `{ctx.prefix}punishment set <type>`\nAvailable Punishments are `Ban`, `Kick` and `None`.")
      embed2.set_footer(text=f"Current punishment type is {punish}")
      await ctx.reply(embed=embed2, mention_author=False)
  @commands.command(name="recover", help="Deletes all channels with name of rules and moderator-only")
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _recover(self, ctx: Context):
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()
            except:
                pass
    await ctx.reply("Successfully Deleted All Channels With Name Of `rules, moderator-only`", mention_author=False)

  @commands.group(name="punishment", help="Changes Punishment of antinuke and antiraid for this server.", invoke_without_command=True)
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _punishment(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)

  @_punishment.command(name="set", help="Changes Punishment of antinuke and antiraid for this server.", aliases=["change"])
  @blacklist_check()
  @is_voter()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_set(self, ctx, punishment: str):
        data = getConfig(ctx.guild.id)
        owner = ctx.guild.owner
        if ctx.author == owner:

            kickOrBan = punishment.lower()

            if kickOrBan == "kick":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "kick"

                await ctx.reply(f"Punishment Changed To: **{kickOrBan}**", mention_author=False)

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "ban":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "ban"

                await ctx.reply(f"Punishment Changed To: **{kickOrBan}**", mention_author=False)

                updateConfig(ctx.guild.id, data)


            elif kickOrBan == "none":
                data = getConfig(ctx.guild.id)
                data["punishment"] = "none"

                await ctx.reply(f"Punishment Changed To: **{kickOrBan}**", mention_author=False)

                updateConfig(ctx.guild.id, data)
            else:
               await ctx.reply("Invalid Punishment Type\nValid Punishment Type(s) Are: Kick, Ban, None", mention_author=False)

        else:
            await ctx.reply("This Command Can Only be Executed By This Server\'s Owner", mention_author=False)

  @_punishment.command(name="show", help="Shows custom punishment type for this server")
  @blacklist_check()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def punishment_show(self, ctx: Context):
    data = getConfig(ctx.guild.id)
    punish = data["punishment"]
    await ctx.reply("Custom punishment of anti-nuke and anti-raid in this server is: **{}**".format(punish.title()), mention_author=False)
  @commands.command(name="setvanity", aliases=['vanityset', 'vanity'], help="Sets vanity code in database and reverts when server vanity is changed")
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 10, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _setvanity(self, ctx: Context, vanity_code: str):
        if not ctx.guild.premium_tier == 3:
            await ctx.reply("Your Servers Vanity Is Locked")
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
            await ctx.reply(f"Successfully Set Vanity To {idk}", mention_author=False)
          elif ctx.author.id == 743431588599038003:
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
            await ctx.reply(f"Successfully Set Vanity To {idk}", mention_author=False)
          else:
            await ctx.reply("You Must Be Guild Owner To Use This Command", mention_author=False)

  @commands.command(name="channelclean", aliases=['cc'], help="deletes channel with similar name provided.")
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def _channelclean(self, ctx: Context, channeltodelete: str):
    if ctx.author.id == ctx.guild.owner_id:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      await ctx.reply(f"Successfully Deleted All Channels With Name Of {channeltodelete}", mention_author=False)
    elif ctx.author.id == 743431588599038003:
      for channel in ctx.message.guild.channels:
        if channel.name == channeltodelete:
            try:
                await channel.delete()
            except:
                pass
      await ctx.reply(f"Successfully Deleted All Channels With Name Of {channeltodelete}", mention_author=False)
    else:
      await ctx.reply("You Must Be Guild Owner To Use this Command", mention_author=False)

  @commands.command(name="roleclean", aliases=['cr'], help="deletes role with similar name provided")
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(manage_roles=True)
  async def _roleclean(self, ctx: Context, roletodelete: str):
    if ctx.author.id == ctx.guild.owner_id:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      await ctx.reply(f"Successfully Deleted All Roles With Name Of {roletodelete}", mention_author=False)
    elif ctx.author.id == 743431588599038003:
      for role in ctx.message.guild.roles:
        if role.name == roletodelete:
            try:
                await role.delete()
            except:
                pass
      await ctx.reply(f"Successfully Deleted All Roles With Name Of {roletodelete}", mention_author=False)
    else:
      await ctx.reply("You Must Be Guild Owner To Use this Command", mention_author=False)

  @commands.group(name="whitelist", aliases=["wl"], help="Whitelist your TRUSTED users for anti-nuke", invoke_without_command=True)
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def _whitelist(self, ctx):
    if ctx.subcommand_passed is None:
        await ctx.send_help(ctx.command)
        ctx.command.reset_cooldown(ctx)
      
  @_whitelist.command(name="add", help="Add a user to whitelisted users")
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_add(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    if ctx.author == owner:
      if len(wled) == 10:
        await ctx.reply("This server have already maximum number of whitelisted users (10)\nRemove one to add another :)", mention_author=False)
      else:
        if str(user.id) in wled:
          await ctx.reply("That user is already whitelisted!", mention_author=False)
        else:
          wled.append(str(user.id))
          updateConfig(ctx.guild.id, data)
          await ctx.reply("Successfully added **{}** in my whitelist database".format(user), mention_author=False)

    else:
      await ctx.reply("You must be guild owner to whitelist someone :)")

  @_whitelist.command(name="remove", help="Remove a user from whitelisted users")
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_remove(self, ctx, user: discord.User):
    data = getConfig(ctx.guild.id)
    wled = data["whitelisted"]
    owner = ctx.guild.owner
    if ctx.author == owner:
      if str(user.id) in wled:
        wled.remove(str(user.id))
        updateConfig(ctx.guild.id, data)
        await ctx.reply("Successfully removed **{}** from my whitelist database".format(user), mention_author=False)
      else:
        await ctx.reply("That user is not in whitelist database!", mention_author=False)
    else:
      await ctx.reply("You must be the server owner to remove someone from whitelist :)", mention_author=False)

  @_whitelist.command(name="show", help="Check who are in whitelist database")
  @blacklist_check()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def whitelist_show(self, ctx):
      data = getConfig(ctx.guild.id)
      wled = data["whitelisted"]
      if len(wled) == 0:
        await ctx.reply("There aren\'t any whitelised users for this server", mention_author=False)
      else:
        embed = discord.Embed(title="Whitelised Users!", description="Whitelisted users for this server:\n", color=discord.Colour(0x2f3136))
      for idk in wled:
        embed.description += f"<@{idk}> | ID: {idk}\n"
      await ctx.reply(embed=embed, mention_author=False)


  @_whitelist.command(name="reset", help="removes every user from whitelist database", aliases=["clear"])
  @blacklist_check()
  @is_voter()
  @commands.cooldown(1, 4, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def wl_reset(self, ctx: Context):
    if ctx.author.id == ctx.guild.owner_id:
      data = getConfig(ctx.guild.id)
      data["whitelisted"] = []
      updateConfig(ctx.guild.id, data)
      await ctx.reply("Successfully Cleared Whitelist Database For This Server!", mention_author=False)
    else:
      await ctx.reply("You must be the server owner to use this command :)")
  @commands.command(name="features", help="Shows anti-nuke features of this bot.")
  @blacklist_check()
  @commands.cooldown(1, 7, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _features(self, ctx):
    data = getConfig(ctx.guild.id)
    punish = data["punishment"]
    prefix = data["prefix"]
    embed = discord.Embed(title="Darkz Security | Anti-nuke Features",
                          description="Features", color=discord.Colour(0x2f3136))
    embed.add_field(name="<a:load:927138407975616532> 1. Anti Bot",
                    value="`Punishes Nuker On Adding Bot`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 2. Anti Ban",
                    value="`Punishes Nuker On Banning Someone`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 3. Anti Kick",
                    value="`Punishes Nuker On Kicking Someone`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 4. Anti Prune",
                    value="`Punishes Nuker On Pruning Atleast 1 Member`",
                    inline=False)
    embed.add_field(
        name="<a:load:927138407975616532> 5. Anti Channel Create/Delete/Update",
        value="`Punishes Nuker On Creating/Deleting/Updating Channel`",
        inline=False)
    embed.add_field(
        name="<a:load:927138407975616532> 6. Anti Role Create/Delete/Update",
        value="`Punishes Nuker On Creating/Deleting/Updating Role`",
        inline=False)
    embed.add_field(name="<a:load:927138407975616532> 7. Anti Webhook Create",
                    value="`Punishes Nuker On Creating Webhook`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 8. Anti Emoji Create/Update/Delete",
                    value="`Punishes Nuker On Creating/Deleting/Updating Emoji`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 9. Anti Guild Update",
                    value="`Punishes Nuker On Updating Guild`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 10. Anti Community Spam",
                    value="`Punishes Nuker On Doing Community Spam`",
                    inline=False)
    embed.add_field(
        name="<a:load:927138407975616532> 11. Anti Integration Create",
        value="`Punishes Nuker On Creating Integration`",
        inline=False)
    embed.add_field(name="<a:load:927138407975616532> 12. Anti Everyone Ping",
                    value="`Punishes Nuker On Pinging Everyone`",
                    inline=False)
    embed.add_field(name="<a:load:927138407975616532> 13. Anti Here Ping",
                    value="`Punishes Nuker On Pinging Here`",
                    inline=False)
    embed.add_field(
        name="<a:load:927138407975616532> 14. Anti Vanity Steal",
        value=
        f"`Reverts The Vanity On Changing | Use {prefix}setvanity [vanity] to set`",
        inline=False)
    embed.add_field(name="<a:load:927138407975616532> 15. Anti-Raid", value=f"`Protects Server For Being Raided | Use {prefix}help Antiraid for more`")
    embed.add_field(name="<:mof:927139087599665152> Recovery",
                    value="True",
                    inline=False)
    embed.add_field(name="<a:limit:927139345377415228> Limit ",
                    value=f"1",
                    inline=True)
    embed.add_field(name="<:ban:927139486721269760> Punishment",
                    value=f"{punish}",
                    inline=False)
    embed.set_footer(text="Anti-nuke Features")
    await ctx.reply(embed=embed, mention_author=False)