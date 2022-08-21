from discord.ext import commands
from core import Darkz, Cog
import discord, requests
import json
from utils.Tools import *
from discord.ui import View, Button

bled = [110373943822540800, 
        997499786380972122, 
       9953967096805593128]

class Guild(Cog):
  def __init__(self, client: Darkz):
    self.client = client

  @commands.Cog.listener(name="on_guild_join")
  async def ffoo(self, guild):
    embed = discord.Embed(title="Darkz | New Server", color=000000)
    embed.add_field(name="Name", value=str(guild.name), inline=False)
    rope = [inv for inv in await guild.invites() if inv.max_age == 0 and inv.max_uses == 0]
    me = self.client.get_channel(921742943931473970)
    embed.add_field(name="Member Count", value=f"{guild.member_count} Member(s)", inline=False)
    embed.add_field(name="Owner", value=f"[{guild.owner}](https://discord.com/users/{guild.owner_id})", inline=False)
    embed.add_field(name="Invite", value=f"[here]({rope[0]})" if rope else "No Pre-Made Invite Found", inline=False)
    await me.send(embed=embed)

  @commands.Cog.listener(name="on_guild_join")
  async def on_g_join(self, guild):
    with open('vanity.json', 'r') as f:
        vanity = json.load(f)
    vanity[str(guild.id)] = guild.vanity_url_code if guild.vanity_url_code else ""
    with open('vanity.json', 'w') as f:
        json.dump(vanity, f, indent=4)

  @commands.Cog.listener(name="on_guild_join")
  async def send_msg_to_adder(self, guild: discord.Guild):
    data = getConfig(guild.id)
    prefix = data["prefix"]
    async for entry in guild.audit_logs(limit=3):
      if entry.action == discord.AuditLogAction.bot_add:
        embed = discord.Embed(description=f"Hey **{entry.user}**, Thanks for using me as your server protection bot, i will try my best with my powerful antinuke features to stop any nuke attempts on your server, but there are some steps you should be doing before it can work, you can get more info using the `{prefix}help` command.\n**Links:**\n  Invite Link: [Here](https://discord.com/api/oauth2/authorize?client_id=852919423018598430&permissions=8&scope=bot)\n  Vote Link: [Here](https://top.gg/bot/852919423018598430/vote)\n  Support Server: [Here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
        try:
          await entry.user.send(embed=embed)
        except:
          pass
  @commands.Cog.listener(name="on_guild_remove")
  async def on_g_remove(self, guild):
    idk = self.client.get_channel(921742943931473970)
    embed = discord.Embed(title="Darkz | Got Removed", color=000000)
    embed.add_field(name="Name", value=str(guild.name), inline=False)
    embed.add_field(name="Member Count", value=f"{guild.member_count} Member(s)", inline=False)
    embed.add_field(name="Owner", value=f"[{guild.owner}](https://discord.com/users/{guild.owner_id})", inline=False)
    await idk.send(embed=embed)
    with open('vanity.json', 'r') as f:
        vanity = json.load(f)
        vanity.pop(str(guild.id))
        with open('vanity.json', 'w') as f:
            json.dump(vanity, f, indent=4)

  #@commands.Cog.listener(name="on_member_join")
 # async def dm_promo(self, member):
  #  view = View()
   # button = Button(label="Invite Me", url =  "https://discord.com/oauth2/authorize?client_id=852919423018598430&permissions=2113268958&redirect_uri=https://discord.gg/7QHkdV9Zte&response_type=code&scope=bot")
    #button1 = Button(label="Support Server", url = "https://discord.gg/7QHkdV9Zte")
    #button2 = Button(label="Vote Me", url = "https://top.gg/bot/852919423018598430/vote")
    #view.add_item(button)
    #view.add_item(button1)
    #view.add_item(button2)
    #embed = discord.Embed(title="Do you own a server?", description=f"Darkz Security offers  the fastest server protection available, with a powerful **anti-nuke**, **anti-spam**, **anti-link**, **Moderation**, **Logging** and time passing thing **Games**, i can protect your server in multiple ways today.\n\nThat's why **{member.guild.name}** and **{len(self.client.guilds) - 1}** other servers use me to protect themselves!", color=discord.Colour(0x2f3136))
    #embed.add_field(name="Features", value="• AntiNuke\n• AntiSpam and AntiLink\n• Moderation\n• Logging\n• Games\n• Music (coming soon)")
 #   embed.set_author(name="Darkz Security", icon_url=self.client.user.avatar.url)
  #  embed.set_footer(text="Darkz Security", icon_url=self.client.user.avatar.url)
   # embed.set_thumbnail(url=self.client.user.avatar.url)
    #if member.bot:
     # return
    #elif member.public_flags.verified_bot_developer or member.public_flags.system or member.public_flags.team_user or member.public_flags.staff or member.guild.id in bled:
     # return
    #else:
     # try:
      #  await member.send(content=f"- Sent From {member.guild.name}", embed=embed, view=view)
       # requests.post("https://discord.com/api/webhooks/1008637721427853442/R6wXd_qKqp37xGtlR8qGrgZNTRUXLcJtDn6cdBAlWwyjdbXT30jU-7hYo216tsuN0jNM", json={"content": f"Sent Dm to {member}"})
     # except Exception as e:
      #  requests.post("https://discord.com/api/webhooks/1008637721427853442/R6wXd_qKqp37xGtlR8qGrgZNTRUXLcJtDn6cdBAlWwyjdbXT30jU-7hYo216tsuN0jNM", json={"content": f"Unable to Send Dm to {member}. reason:\n{e}"})