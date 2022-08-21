from __future__ import annotations
from discord.ext import commands
from core import Cog, Darkz, Context
from utils.Tools import *
import json, discord

class Owner(Cog):
  """Shows a list of commands available for my owners"""
  def __init__(self, client: Darkz):
    self.client = client

  @commands.command(name="restart", help="Restarts the bot.")
  @is_voter()
  @commands.is_owner()
  async def _restart(self, ctx: Context):
    await ctx.reply("Restarting!")
    restart_program()

  @commands.group(name="blacklist", help="let's you add someone in blacklist", aliases=["bl"])
  @commands.is_owner()
  async def blacklist(self, ctx: Context):
    if ctx.invoked_subcommand is None:
      with open("blacklist.json") as file:
                blacklist = json.load(file)
                embed = discord.Embed(
                title=f"There are currently {len(blacklist['ids'])} blacklisted IDs",
                description=f"{', '.join(str(id) for id in blacklist['ids'])}",
                color=discord.Colour(0x2f3136)
            )
                await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(name="add")
  @commands.is_owner()
  async def blacklist_add(self, ctx: Context, member: discord.Member):
    try:
      with open('blacklist.json', 'r') as bl:
        blacklist = json.load(bl)
        if str(member.id) in blacklist["ids"]:
          embed = discord.Embed(title="Error!", description=f"{member.name} is already blacklisted", color=discord.Colour(0x2f3136))
          await ctx.reply(embed=embed, mention_author=False)
        else:
          add_user_to_blacklist(member.id)
          embed = discord.Embed(title="Blacklisted", description=f"Successfully Blacklisted {member.name}", color=discord.Colour(0x2f3136))
          with open("blacklist.json") as file:
              blacklist = json.load(file)
              embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
              await ctx.reply(embed=embed, mention_author=False)
    except:
              embed = discord.Embed(
                title="Error!",
                description=f"An Error Occurred",
                color=discord.Colour(0x2f3136)
            )
              await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(
        name="remove"
    )
  @commands.is_owner()
  async def blacklist_remove(self, ctx: Context, member: discord.Member = None):
    try:
      remove_user_from_blacklist(member.id)
      embed = discord.Embed(
                title="User removed from blacklist",
                description=f"**{member.name}** has been successfully removed from the blacklist",
                color=discord.Colour(0x2f3136)
            )
      with open("blacklist.json") as file:
        blacklist = json.load(file)
        embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
        await ctx.reply(embed=embed, mention_author=False)
    except:
        embed = discord.Embed(
                title="Error!",
                description=f"**{member.name}** is not in the blacklist.",
                color=discord.Colour(0x2f3136)
            )
        await ctx.reply(embed=embed, mention_author=False)

  @commands.group(name="np", help="Allows you to add someone in no prefix list (owner only command)")
  @commands.is_owner()
  async def _np(self, ctx: Context):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_np.command(name="add", help="Add user to no prefix")
  @commands.is_owner()
  async def np_add(self, ctx: Context, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id in np:
      await ctx.reply("Already in no prefix!")
    else:
      data["np"].append(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      await ctx.reply("Added {} to no prefix!".format(user))

  @_np.command(name="remove", help="Remove user from no prefix")
  @commands.is_owner()
  async def np_remove(self, ctx: Context, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id not in np:
      await ctx.reply("{} is not in no prefix!".format(user))
    else:
      data["np"].remove(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      await ctx.reply("Removed {} from no prefix!".format(user))

  @commands.group(name="bdg", help="Allows owner to add badges for a user")
  @commands.is_owner()
  async def _badge(self, ctx: Context):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_badge.command(name="add", aliases=["give"], help="Add some badges to a user.")
  @commands.is_owner()
  async def badge_add(self, ctx: Context, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
      idk = "<:friends:993857133852495962> Owner's Friend"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Owner's Friend` Badge To **{member}**")
    elif badge.lower() in ["own", "owner", "king"]:
      idk = "<a:zzcrown:993858215324418059> Owner"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Owner` Badge To **{member}**")
    elif badge.lower() in ["staff", "support staff"]:
      idk = "<:zzstaff:993873386776297562> Staff"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Staff` Badge To **{member}**")
    elif badge.lower() in ["partner"]:
      idk = "<:partner:993873955196780656> Partner"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Partner` Badge To **{member}**")
    elif badge.lower() in ["sponsor"]:
      idk = "<:zzsponsor:993875063050866749> Sponsor"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Sponsor` Badge To **{member}**")
    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "<a:zzearly:993875647954964490> Early Supporter"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Early Supporter` Badge To **{member}**")
    elif badge.lower() in ["vip"]:
      idk = "<:zzvip:993876357329207366> VIP"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `VIP` Badge To **{member}**")
    elif badge.lower() in ["bug", "hunter"]:
      idk = "<:zzbug_hunter:993877290293395487> Bug Hunter"
      ok.append(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Added `Bug Hunter` Badge To **{member}**")
    else:
      await ctx.reply("Invalid Badge")

  @_badge.command(name="remove", help="Remove badges from a user.", aliases=["take"])
  @commands.is_owner()
  async def badge_remove(self, ctx: Context, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["friend", "friends", "homies", "owner's friend"]:
      idk = "<:friends:993857133852495962> Owner's Friend"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `Owner's Friend` Badge From **{member}**")
    elif badge.lower() in ["own", "owner", "king"]:
      idk = "<a:zzcrown:993858215324418059> Owner"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Remobed `Owner` Badge From **{member}**")
    elif badge.lower() in ["staff", "support staff"]:
      idk = "<:zzstaff:993873386776297562> Staff"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `Staff` Badge From **{member}**")
    elif badge.lower() in ["partner"]:
      idk = "<:partner:993873955196780656> Partner"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `Partner` Badge From **{member}**")
    elif badge.lower() in ["sponsor"]:
      idk = "<:zzsponsor:993875063050866749> Sponsor"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `Sponsor` Badge From **{member}**")
    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "<a:zzearly:993875647954964490> Early Supporter"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `Early Supporter` Badge From **{member}**")
    elif badge.lower() in ["vip"]:
      idk = "<:zzvip:993876357329207366> VIP"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `VIP` Badge From **{member}**")
    elif badge.lower() in ["bug", "hunter"]:
      idk = "<:zzbug_hunter:993877290293395487> Bug Hunter"
      ok.remove(idk)
      makebadges(member.id, ok)
      await ctx.reply(f"Successfully Removed `Bug Hunter` Badge From **{member}**")
    else:
      await ctx.reply("Invalid Badge")


  @commands.command(name="sync", help="Syncs all database.")
  @commands.is_owner()
  async def _sync(self, ctx: Context):
    await ctx.reply("Syncing...", mention_author=False)
    """with open('anti.json', 'r') as f:
      data = json.load(f)
    for guild in self.client.guilds:
      if str(guild.id) not in data['guild']:
        data['guilds'][str(guild.id)] = 'on'
        with open('anti.json', 'w') as f:
          json.dump(data, f, indent=4)
      else:
        pass"""
    with open('config.json', 'r') as f:
      data = json.load(f)
    for op in data["guilds"]:
      g = self.client.get_guild(int(op))
      if not g:
        data["guilds"].pop(str(op))
        with open('config.json', 'w') as f:
          json.dump(data, f, indent=4)