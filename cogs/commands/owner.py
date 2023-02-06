from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from typing import Optional
class Owner(commands.Cog):
  def __init__(self, client):
    self.client = client

#https://cdn.discordapp.com/avatars/974984890959425566/7fedaa654af7ec62b211033852e048d0.webp?size=2048
  @commands.command(name="restart", help="Restarts the bot.")
  @commands.is_owner()
  async def _restart(self, ctx: Context):
    await ctx.reply("<:ellor:1056829282858573925> Restarting!")
    restart_program()


  @commands.command(name="sync", help="Syncs all database.")
  @commands.is_owner()
  async def _sync(self, ctx: Context):
    await ctx.reply("Syncing...", mention_author=False)
    with open('anti.json', 'r') as f:
      data = json.load(f)
    for guild in self.client.guilds:
      if str(guild.id) not in data['guild']:
        data['guilds'][str(guild.id)] = 'on'
        with open('anti.json', 'w') as f:
          json.dump(data, f, indent=4)
      else:
        pass
    with open('config.json', 'r') as f:
      data = json.load(f)
    for op in data["guilds"]:
      g = self.client.get_guild(int(op))
      if not g:
        data["guilds"].pop(str(op))
        with open('config.json', 'w') as f:
          json.dump(data, f, indent=4)
  @commands.group(name="blacklist", help="let's you add someone in blacklist", aliases=["bl"])
  @commands.is_owner()
  async def blacklist(self, ctx):
    if ctx.invoked_subcommand is None:
      with open("blacklist.json") as file:
                blacklist = json.load(file)
                embed = discord.Embed(
                title=f"There are currently {len(blacklist['ids'])} blacklisted IDs",
                description=f"{', '.join(str(id) for id in blacklist['ids'])}",
                color=0x00FFE4
            )
                #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
                await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(name="add")
  @commands.is_owner()
  async def blacklist_add(self, ctx, member: discord.Member):
    try:
      with open('blacklist.json', 'r') as bl:
        blacklist = json.load(bl)
        if str(member.id) in blacklist["ids"]:
          embed = discord.Embed(title="Error!", description=f"{member.name} is already blacklisted", color=0x00FFE4)
          await ctx.reply(embed=embed, mention_author=False)
        else:
          add_user_to_blacklist(member.id)
          embed = discord.Embed(title="Blacklisted", description=f"<:GreenTick:1029990379623292938> | Successfully Blacklisted {member.name}", color=0x00FFE4)
          with open("blacklist.json") as file:
              blacklist = json.load(file)
              embed.set_footer(
                text=f"There are now {len(blacklist['ids'])} users in the blacklist"
            )
              await ctx.reply(embed=embed, mention_author=False)
    except:
              embed = discord.Embed(
                title="Error!",
                description=f"**An Error Occurred**",
                color=0x00FFE4
            )
              #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
              await ctx.reply(embed=embed, mention_author=False)

  @blacklist.command(
        name="remove"
    )
  @commands.is_owner()
  async def blacklist_remove(self, ctx, member: discord.Member = None):
    try:
      remove_user_from_blacklist(member.id)
      embed = discord.Embed(
                title="User removed from blacklist",
                description=f"<:GreenTick:1029990379623292938> | **{member.name}** has been successfully removed from the blacklist",
                color=0x00FFE4
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
                color=0x00FFE4
            )
       # embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
        await ctx.reply(embed=embed, mention_author=False)

  @commands.group(name="np", help="Allows you to add someone in no prefix list (owner only command)")
  @commands.is_owner()
  async def _np(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_np.command(name="add", help="Add user to no prefix")
  @commands.is_owner()
  async def np_add(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id in np:
      embed = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:ellor:1056829282858573925> **Error:** `Data Already Exists!`\n<:rightshort:1053176997481828452> Given user is already in my `no prefix`",
                color=0xdbdbdb
       )
      #embed.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed)
    else:
      data["np"].append(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed1 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added given user to my `no prefix`",
                color=0xdbdbdb
       )
      #embed1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed1)

  @_np.command(name="remove", help="Remove user from no prefix")
  @commands.is_owner()
  async def np_remove(self, ctx, user: discord.User):
    with open('info.json', 'r') as idk:
      data = json.load(idk)
    np = data["np"]
    if user.id not in np:
      embed = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:ellor:1056829282858573925> **Error:** `Data Not Found!`\n<:rightshort:1053176997481828452> Given user is not in my `no prefix`",
                color=0xdbdbdb
       )
      #embed.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed)
    else:
      data["np"].remove(user.id)
    with open('info.json', 'w') as idk:
      json.dump(data, idk, indent=4)
      embed2 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully removed given user from my `no prefix`",
                color=0xdbdbdb
       )

      await ctx.reply(embed=embed2)

  @commands.group(name="bdg", help="Allows owner to add badges for a user")
  @commands.is_owner()
  async def _badge(self, ctx):
    if ctx.invoked_subcommand is None:
      await ctx.send_help(ctx.command)

  @_badge.command(name="add", aliases=["give"], help="Add some badges to a user.")
  @commands.is_owner()
  async def badge_add(self, ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["owner"]:
      idk = "**<:1spacer:1056545806943006760><:OwnerBadge:1053150626982408243> Owner**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed2 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Owner`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )
    
      await ctx.reply(embed=embed2)
    elif badge.lower() in ["staff", "support staff"]:
      idk = "**<:1spacer:1056545806943006760><:Mod:1051999330745209002> Staff**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed3 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Staff`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb)
      
      await ctx.reply(embed=embed3)
    elif badge.lower() in ["partner"]:
      idk = "**<:1spacer:1056545806943006760><a:partner:1051999447409766481> Partner**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed4 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Partner`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )
      
      await ctx.reply(embed=embed4)
    elif badge.lower() in ["sponsor"]:
      idk = "**<:1spacer:1056545806943006760><a:premium:1056725098641494167> Sponsor**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed5 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Sponser`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )
      
      await ctx.reply(embed=embed5)
    elif badge.lower() in ["friend", "friends"]:
      idk = "**<:1spacer:1056545806943006760><:CommunityUser:1056918137389461514> Owner`s Friend**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed1 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Friend`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )

      await ctx.reply(embed=embed1)
    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "**<:1spacer:1056545806943006760><:Earlybot:1056952426944544858> Early Supporter**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed6 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Early Supporter`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )
      
      await ctx.reply(embed=embed6)

    elif badge.lower() in ["vip"]:
      idk = "**<:1spacer:1056545806943006760><:VIP:1056953257458675712> Vip**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed7 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Vip`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )
      #embed7.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed7.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed7)

    elif badge.lower() in ["bug", "hunter"]:
      idk = "**<:1spacer:1056545806943006760><:bug2:1056953460232310815> Bug Hunter**"
      ok.append(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Bug Hunter`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )
      
      await ctx.reply(embed=embed8)
    elif badge.lower() in ["all"]:
      idk = "**<:1spacer:1056545806943006760><:OwnerBadge:1053150626982408243> Owner\n<:1spacer:1056545806943006760><:Mod:1051999330745209002> Staff\n<:1spacer:1056545806943006760><a:partner:1051999447409766481> Partner\n<:1spacer:1056545806943006760><a:premium:1056725098641494167> Sponsor\n<:1spacer:1056545806943006760><:CommunityUser:1056918137389461514> Owner`s Friend\n<:1spacer:1056545806943006760><:Earlybot:1056952426944544858> Early Supporter\n<:1spacer:1056545806943006760><:VIP:1056953257458675712> Vip\n<:1spacer:1056545806943006760><:bug2:1056953460232310815> Bug Hunter**"
      ok.append(idk)
      makebadges(member.id, ok)
      embedall = discord.Embed(
                title="Sputnik",
                description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Owner,Partner,Sponser, Friend,Early Supporter,Vip,Bug Hunter`\n<:rightshort:1053176997481828452> Successfully Added!",
                color=0xdbdbdb
       )

      await ctx.reply(embed=embedall)
    else:
      hacker = discord.Embed(
                title="Sputnik",
                description="**Invalid Badge**",
                color=0xdbdbdb
       )
      
      await ctx.reply(embed=hacker)

  @_badge.command(name="remove", help="Remove badges from a user.", aliases=["re","take"])
  @commands.is_owner()
  async def badge_remove(self, ctx, member: discord.Member, *, badge: str):
    ok = getbadges(member.id)
    if badge.lower() in ["owner"]:
      idk = "**<:1spacer:1056545806943006760><:OwnerBadge:1053150626982408243> Owner**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed2 = discord.Embed(
                title="Sputnik",
                description=f"**<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:Notification:1053149447506374666> **Victim:** `{member}`\n<:Badgee:1056902264276656178> **Badge:** `Owner`\n<:rightshort:1053176997481828452> Successfully Removed!**",
                color=0xdbdbdb
       )
      #embed2.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed2.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed2)

    elif badge.lower() in ["staff", "support staff"]:
      idk = "**<:1spacer:1056545806943006760><:Mod:1051999330745209002> Staff**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed3 = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Staff` Badge To {member}**",
                color=0x00FFE4
       )
      #embed3.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed3.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed3)

    elif badge.lower() in ["partner"]:
      idk = "**<:1spacer:1056545806943006760><a:partner:1051999447409766481> Partner**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed4 = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Partner` Badge To {member}**",
                color=0xdbdbdb
       )
      #embed4.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed4.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed4)

    elif badge.lower() in ["sponsor"]:
      idk = "**<:1spacer:1056545806943006760><a:premium:1056725098641494167> Sponsor**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed5 = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Sponsor` Badge To {member}**",
                color=0xdbdbdb
       )
      #embed5.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed5.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed5)

    elif badge.lower() in ["friend", "friends"]:
      idk = "**<:1spacer:1056545806943006760><:CommunityUser:1056918137389461514> Owner`s Friend**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed1 = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Owner's Friend` Badge To {member}**",
                color=0xdbdbdb
       )
      #embed1.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed1.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed1)

    elif badge.lower() in ["early", "supporter", "support"]:
      idk = "**<:1spacer:1056545806943006760><:Earlybot:1056952426944544858> Early Supporter**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed6 = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `Early Supporter` Badge To {member}**",
                color=0xdbdbdb
       )
      #embed6.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed6.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed6)

    elif badge.lower() in ["vip"]:
      idk = "**<:1spacer:1056545806943006760><:VIP:1056953257458675712> Vip**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed7 = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `VIP` Badge To {member}**",
                color=0xdbdbdb
       )
      #embed7.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed7.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed7)

    elif badge.lower() in ["bug", "hunter"]:
      idk = "**<:1spacer:1056545806943006760><:bug2:1056953460232310815> Bug Hunter**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embed8 = discord.Embed(
                title="Sputnik",
                description=f"**Successfully Removed `Bug Hunter` Badge To {member}**",
                color=0xdbdbdb
       )
      #embed8.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embed8.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embed8)
      await ctx.reply(f"<:GreenTick:1029990379623292938> | Successfully Removed `Bug Hunter` Badge From **{member}**")
    elif badge.lower() in ["all"]:
      idk = "**<:1spacer:1056545806943006760><:OwnerBadge:1053150626982408243> Owner\n<:1spacer:1056545806943006760><:Mod:1051999330745209002> Staff\n<:1spacer:1056545806943006760><a:partner:1051999447409766481> Partner\n<:1spacer:1056545806943006760><a:premium:1056725098641494167> Sponsor\n<:1spacer:1056545806943006760><:CommunityUser:1056918137389461514> Owner`s Friend\n<:1spacer:1056545806943006760><:Earlybot:1056952426944544858> Early Supporter\n<:1spacer:1056545806943006760><:VIP:1056953257458675712> Vip\n<:1spacer:1056545806943006760><:bug2:1056953460232310815> Bug Hunter**"
      ok.remove(idk)
      makebadges(member.id, ok)
      embedall = discord.Embed(
                title="Sputnik",
                description=f"<:GreenTick:1029990379623292938> | **Successfully Removed `All` Badges From {member}**",
                color=0xdbdbdb
       )
      #embedall.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #embedall.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=embedall)
    else:
      hacker = discord.Embed(
                title="Sputnik",
                description="**Invalid Badge**",
                color=0xdbdbdb
       )
      #hacker.set_footer(text=f"Made With 💖 By ~ Hacker_xD#0001",icon_url= "https://cdn.discordapp.com/avatars/980359292840472597/a_dbfc76aa89c069c0f1f0dd705e2a91c9.gif?size=2048")
      #hacker.set_thumbnail(url = "https://cdn.discordapp.com/avatars/977023331117199481/b0270586b291c69b396cd5a24aa11aff.webp?size=2048") 
      await ctx.reply(embed=hacker)

  
  @commands.command(name="syncs", help="Syncs Slash Commands.")
  @commands.is_owner()
  async def _sync(self, ctx) -> None:
      fmt = await ctx.bot.tree.sync(guild=ctx.guild)
      await ctx.send(
          f"Synced {len(fmt)} commands to the current guild."
        )
      channel = await ctx.message.author.create_dm()
      await channel.send('Sputnik Was Here')
      return



  @commands.command(help="Make the bot say something in a given channel.")
  @commands.is_owner()
  async def say(self, ctx: commands.Context, channel_id: int, *, message):
      channel = self.bot.get_channel(channel_id)
      guild = channel.guild
      channel = await ctx.message.author.create_dm()
      await ctx.send(f"Sending message to **{guild}** <#{channel.id}>\n> {message}")
      await channel.send(message)
