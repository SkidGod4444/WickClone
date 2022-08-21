from discord.ext import commands
from core import Darkz, Cog, Context
from utils.Tools import *
import discord, psutil, pathlib, shutil, os, sys
from discord.ui import View, Button
from typing import Optional

def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)


def get_ram_total():
    return int(psutil.virtual_memory().total)


class Extra(Cog):
  """Some extra commands which can't be listed in Moderation group are listed here."""
  def __init__(self, client: Darkz):
    self.client = client

  @commands.command(name="invite", aliases=['inv', 'vote', 'support'], help="What kindaa dumb you are that looking for invite help")
  @blacklist_check()
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _invite(self, ctx):
    button = Button(label="Invite", url = "https://discord.com/oauth2/authorize?client_id=852919423018598430&permissions=2113268958&redirect_uri=https://discord.gg/7QHkdV9Zte&response_type=code&scope=bot")
    button1 = Button(label="Support Server", url = "https://discord.gg/7QHkdV9Zte")
    button2 = Button(label="Vote", url = "https://top.gg/bot/852919423018598430/vote")


    embed = discord.Embed(color=discord.Colour(0x2f3136), description=">>> • [Click here to invite me](https://discord.com/oauth2/authorize?client_id=852919423018598430&permissions=2113268958&redirect_uri=https://discord.gg/7QHkdV9Zte&response_type=code&scope=bot)\n• [Click here to upvote me](https://top.gg/bot/852919423018598430/vote)\n• [Click here to join my support server](https://discord.gg/7QHkdV9Zte)")
    embed.timestamp = discord.utils.utcnow()
    view = View()
    view.add_item(button)
    view.add_item(button1)
    view.add_item(button2)
    await ctx.reply(embed=embed, mention_author=False, view=view)

  @commands.command(name="badges", help="Check what premium badges a user have.", aliases=["badge"])
  @blacklist_check()
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _badges(self, ctx: Context, user: Optional[discord.User] = None):
    mem = user or ctx.author
    badges = getbadges(mem.id)
    if badges == []:
      msg = f"<:error_ok:946729104126922802> | {mem} Have No Bot Badges For Now"
      await ctx.reply(msg, mention_author=False)
    else:
      embed = discord.Embed(title="Badges", description="Badge(s) of {}\n\n".format(mem), color=discord.Colour(0x2f3136))
      embed.set_author(name=mem, icon_url = mem.avatar.url if mem.avatar else mem.default_avatar.url)
      embed.set_thumbnail(url=mem.avatar.url if mem.avatar else mem.default_avatar.url)
      embed.timestamp = discord.utils.utcnow()
      for badge in badges:
        embed.description += f"**{badge}**\n"
      await ctx.reply(embed=embed, mention_author=False)
    
  @commands.command(name="info", aliases=['botinfo', 'stats', 'bi'], help="Check information about bot")
  @blacklist_check()
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _info(self, ctx):
    shards_guilds = {i: {"guilds": 0, "users": 0} for i in range(len(self.client.shards))}
    for guild in self.client.guilds:
            shards_guilds[guild.shard_id]["guilds"] += 1
            shards_guilds[guild.shard_id]["users"] += guild.member_count

    p = pathlib.Path('./')
    imp = cm = cr = fn = cl = ls = fc = 0
    for f in p.rglob('*.py'):
            if str(f).startswith("venv"):
                continue
            fc += 1
            with f.open() as of:
                for l in of.readlines():
                    l = l.strip()
                    if l.startswith('class'):
                        cl += 1
                    if l.startswith('def'):
                        fn += 1
                    if l.startswith('import'):
                        imp += 1
                    if l.startswith("from"):
                        imp += 1
                    if l.startswith('async def'):
                        cr += 1
                    if '#' in l:
                        cm += 1
                    ls += 1

    total, used, free = shutil.disk_usage("/")
    embed = discord.Embed(title="Bot Info", description=f"""[Invite Me](https://discord.com/oauth2/authorize?client_id=852919423018598430&permissions=2113268958&redirect_uri=https://discord.gg/7QHkdV9Zte&response_type=code&scope=bot) **|** [Support Server](https://discord.gg/7QHkdV9Zte) **|** [Vote Me](https://top.gg/bot/852919423018598430/vote)

I'm a discord bot developed by [@Eagle[.]#0831](https://discord.com/users/743431588599038003) and [@Alone†ᶜʸˡ#5428](https://discord.com/users/905396101274828821)

Supporters: [@~ Mafia_xD#0001](https://discord.com/users/968013339953352715) and [@⚘ *₊ ζ͜͡𝐓he𝐑eal𝐏ennywise#1234](https://discord.com/users/975012142640169020)

I've been on discord since {discord.utils.format_dt(ctx.me.created_at)} ({discord.utils.format_dt(ctx.me.created_at, style='R')})
I'm packed with lot of features such as AntiNuke, AntiRaid, Moderation and much more!
""", color=discord.Colour(0x2f3136))
    embed.add_field(name=f"__**Basic Information**__", value=f"""
Guilds: `{len(self.client.guilds):,}`
Users: `{len(self.client.users):,}`
Commands: `{len(set(self.client.walk_commands()))}`
Shards: `{len(self.client.shards)}`
                        """, inline=True)
    embed.add_field(name=f"__**System Info**__", value=f"""
PID: `{os.getpid()}`
CPU: `{round(psutil.cpu_percent())}%`/`100%`
RAM: `{int((psutil.virtual_memory().total - psutil.virtual_memory().available)
 / 1024 / 1024)}MB`/`{int((psutil.virtual_memory().total) / 1024 / 1024)}MB`
Disk: `{used // (2 ** 30)}GB`/`{total // (2 ** 30)}GB`
Python: `{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}`
                          """, inline=True)
    embed.add_field(name=f"__**Code Stats**__", value=f"""
Total Files: `{fc:,}`
Total Imports: `{imp:,}`
Lines Used: `{ls:,}`
Total Classes: `{cl:,}`
Functions Defined: `{fn:,}`
Total Courtines: `{cr:,}`
Total Comments: `{cm:,}`
                          """, inline=True)
    for shard_id, shard in self.client.shards.items():
            embed.add_field(name=f"__**Shard Id #{shard_id}**__", value=f"""
Latency: `{round(shard.latency * 1000)}`ms{' ' * (9 - len(str(round(shard.latency * 1000, 3))))}
Guilds: `{shards_guilds[shard_id]['guilds']:,}`
Users: `{shards_guilds[shard_id]['users']:,}`
            """, inline=True)

    await ctx.reply(embed=embed, mention_author=False)
  
  @commands.command(name="source", aliases=["src", "sourcecode", "source-code"], help="Sends bot's official source code")
  @blacklist_check()
  @commands.cooldown(1, 30, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _source(self, ctx):
    embed = discord.Embed(title="Source Code!", description="Here is my official source code:\n[Github](https://github.com/eagle37/Darkz)", color=discord.Colour(0x2f3136))
    embed.set_thumbnail(url="https://tenor.com/view/skid-stormfn-uni-skidder-skidders-gif-23470939")
    embed.set_footer(icon_url="https://tenor.com/view/skid-stormfn-uni-skidder-skidders-gif-23470939")
    await ctx.reply(embed=embed, mention_author=False)

  @commands.command(name="ping", aliases=["latency"], help="Check how the bot is doing")
  @blacklist_check()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
  @commands.guild_only()
  async def _ping(self, ctx):
    embed = discord.Embed(title='Pong <a:ping:920222208306073643>',
                          color=discord.Colour(0x2f3136),
                          description=f'**`{int(self.client.latency * 1000)}`**')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/emojis/885681753593872455.gif?size=2048'
    )
    await ctx.reply(embed=embed, mention_author=False)
