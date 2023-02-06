import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.Astroz import Astroz
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
import json
from discord.ui import Button, View
from utils import help as vhelp


client = Astroz()







class HelpCommand(commands.HelpCommand):
  async def on_help_command_error(self, ctx, error):
    damn = [commands.CommandOnCooldown, 
           commands.CommandNotFound, discord.HTTPException, 
           commands.CommandInvokeError]
    if not type(error) in damn:
      await self.context.reply(f"Unknown Error Occurred\n{error.original}", mention_author=False)
    else:
      if type(error) == commands.CommandOnCooldown:
        return
      
        return await super().on_help_command_error(ctx, error)

  async def command_not_found(self, string: str) -> None:
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
      await self.context.reply(embed=embed, mention_author=True)
    else:
      

      if string in ("oknchhfehheng3g", "oknchhfehheng3g"):
        cog = self.context.bot.get_cog("Antinuke")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("oknchhfehheng3g"):
        cog = self.context.bot.get_cog("Games")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      else:
        msg = f"Command `{string}` is not found...\n"
        cmds = (str(cmd) for cmd in self.context.bot.walk_commands())
        mtchs = get_close_matches(string, cmds)
        if mtchs:
          for okaay, okay in enumerate(mtchs, start=1):
            msg += f"Did You Mean: \n`[{okaay}]`. `{okay}`\n"
        embed1 = discord.Embed(color=0x00FFE4,title=f"Command `{string}` is not found...\n",description=f"Did You Mean: \n`[{okaay}]`. `{okay}`\n")
        embed1.set_footer(name="Reminder : Hooks such as <> must not be used when executing commands.")
        return embed1

  
  async def send_bot_help(self, mapping):
    await self.context.typing()
    with open('blacklist.json', 'r') as f:
      bled = json.load(f)
    if str(self.context.author.id) in bled["ids"]:
      embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
      return await self.context.reply(embed=embed, mention_author=False)
    data = getConfig(self.context.guild.id)
    prefix = data["prefix"]
    perms = discord.Permissions.none()
    perms.read_messages = True
    perms.external_emojis = True
    perms.send_messages = True
    perms.manage_roles = True
    perms.manage_channels = True
    perms.ban_members = True
    perms.kick_members = True
    perms.manage_messages = True
    perms.embed_links = True
    perms.read_message_history = True
    perms.attach_files = True
    perms.add_reactions = True
    perms.administrator = True
    inv = discord.utils.oauth_url(self.context.bot.user.id, permissions=perms)
    embed = discord.Embed(title="Commands Overview :",description=f"<:sarrow:1053149614003462174> **General** | <:tixk:1053178188613820468> [Documentation](https://discord.gg/3YmDAzbuRR)\n<:sarrow:1053149614003462174> **Moderation** | <:xross:1053176060759515218> **No Documentation Yet**\n<:sarrow:1053149614003462174> **Security** | <:tixk:1053178188613820468> [Documentation](https://discord.gg/3YmDAzbuRR)\n<:sarrow:1053149614003462174> **Trusted** | <:xross:1053176060759515218> **No Documentation Yet**\n<:sarrow:1053149614003462174> **RaidMode** | <:tixk:1053178188613820468> [Documentation](https://discord.gg/3YmDAzbuRR)\n<:sarrow:1053149614003462174> **ServerRoles** | <:xross:1053176060759515218> **No Documentation Yet**\n<:sarrow:1053149614003462174> **Extras** | <:xross:1053176060759515218> **No Documentation Yet**\n\n**__Need more?__**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> Only commands you can use are displayed! If you lack permissions, you might use some other commands.\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452>  If you want to view more details about a command, type the command and add `helpcmd` before it, for an example: `s!helpcmd ban`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you have questions, [Join Our Support Server](https://discord.gg/3YmDAzbuRR)",color=0xdbdbdb)
 #\n<:sarrow:1053149614003462174> **Logging** | <:tixk:1053178188613820468> [Documentation](https://discord.gg/3YmDAzbuRR)\n<:sarrow:1053149614003462174> **Voice** | <:tixk:1053178188613820468> [Documentation](https://discord.gg/3YmDAzbuRR)\n<:sarrow:1053149614003462174> **Utils** | <:tixk:1053178188613820468> [Documentation](https://discord.gg/3YmDAzbuRR)  
    #embed.set_thumbnail(url="https://media.discordapp.net/attachments/1036538198236614676/1037664035186954270/blue_circle.jpg")
    embed.set_footer(text="Reminder : Hooks such as <> must not be used when executing commands.")
#    embed.add_field(name="Modules Panel", value="""<:general:1056332988176150648> `:` **General**\n<:IconHeadphones:1053891931484201010> `:` **Music**\n<:Mod:1051999330745209002> `:` **Moderation**\n<:antiNuke:1053153914712756245> `:` **AntiMode**\n<:raid_icon:1056334420640018503> `:` **RaidMode**\n<:logsx:1053178328846188565> `:` **Logging**\n<a:Welcome:1053890957566812231> `:` **Welcome**\n<:voice:1053890454757851217> `:` **Voice**\n<:utils:1056335562233098240> `:` **Utils**\n<:xtra:1053892585086787716> `:` **Extras**""", inline=False) 
    embed.set_author(name=self.context.author.name, icon_url=self.context.author.display_avatar.url)
    embed.timestamp = discord.utils.utcnow()
   #  i = Button(label='Invite Me', style=discord.ButtonStyle.link, url='https://discord.gg/3DekMhun')
        
    view = vhelp.View(mapping = mapping, ctx = self.context, homeembed = embed, ui = 2)
   # view.add_item(i)
    await self.context.reply(embed=embed, mention_author=False, view = view)

    
  async def send_command_help(self, command):
    with open('blacklist.json', 'r') as f:
       data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
       embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
       await self.context.reply(embed=embed, mention_author=False)
    else:
       hacker = f"{command.help}" if command.help else 'No Description Provided...'
       embed = discord.Embed( title="Here's some help",description=f"<:urrow:1053243283549204520> **[Join Support Server](https://discord.gg/3YmDAzbuRR)** ***[discord.gg/3YmDAzbuRR]***\n<:urrow:1053243283549204520> **[Documentation](https://discord.gg/3YmDAzbuRR)**", color=0xdbdbdb)
       alias = ' | '.join(command.aliases)

       embed.add_field(name="**Command Category:**", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Category:** `{command.cog.qualified_name.title()}`")
       embed.add_field(name="Command Aliases:",value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Aliases:** `{alias}`" if command.aliases else "<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Aliases:** `No Aliases found!`", inline=False)
       embed.add_field(name="**Command Usage:**", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Usage:** `{self.context.prefix}{command.signature}`\n")
       embed.add_field(name="**Command Description:**", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Description:** `{hacker}`")
      
       embed.set_footer(text="Reminder : Hooks such as <> must not be used when executing commands.", icon_url="")
    
       embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/l7vKMv604vRFUX251EGvc9MWNmFqwBYmcF_8IVYRmug/https/cdn.discordapp.com/emojis/1053153617353396234.png")
       await self.context.reply(embed=embed, mention_author=False)

  def get_command_signature(self, command: commands.Command) -> str:
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = ' | '.join(command.aliases)
            fmt = f'[{command.name} | {aliases}]'
            if parent:
                fmt = f'{parent}'
            alias = f'[{command.name} | {aliases}]'
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

  def common_command_formatting(self, embed_like, command):
        embed_like.title = self.get_command_signature(command)
        if command.description:
            embed_like.description = f'{command.description}\n\n{command.help}'
        else:
            embed_like.description = command.help or 'No help found...'

  
  async def send_group_help(self, group):
    with open('blacklist.json', 'r') as f:
        idk = json.load(f)
    if str(self.context.author.id) in idk["ids"]:
        embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
        await self.context.reply(embed=embed, mention_author=False)
    else:
        await self.context.typing()
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]

        if not group.commands:
            return await self.send_command_help(group)

        embed = discord.Embed(color=0xdbdbdb)

        embed.title = f"Her's some help!"
        _help = group.help or "No description provided..."
        _cmds = "\n\n".join(f" • `{c.qualified_name}`\n{c.short_doc}" for c in group.commands)

        embed.description = f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Description:** `{_help}`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Commands Info:** \n`{_cmds}`"
        embed.set_footer(text="Reminder : Hooks such as <> must not be used when executing commands.")
       # embed.set_author(name=f"{group.qualified_name} Commands", icon_url=self.context.author.display_avatar.url)

      
        if group.aliases:
            #embed.add_field(name="Aliases", value=", ".join(f"`{aliases}`" for aliases in group.aliases), inline=False)
             embed.timestamp = discord.utils.utcnow()
        await self.context.send(embed=embed)

  async def send_cog_help(self, cog):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<:xross:1053176060759515218> Blacklisted User", description="You Are Blacklisted From Using My Commands.\n<:person:1053178413478838312> **Moderator:** `Auto Detection`\n<:Notification:1053149447506374666> ***Reason:** `Spamming My Commands`", color=0xdbdbdb)
      return await self.context.reply(embed=embed, mention_author=False)
    await self.context.typing()
    embed = discord.Embed( color=0xdbdbdb)
    embed.title ="Here's some help!"
    embed.description = f"<:urrow:1053243283549204520> **[Join Support Server](https://discord.gg/3YmDAzbuRR)** ***[discord.gg/3YmDAzbuRR]***\n<:urrow:1053243283549204520> **[Documentation](https://discord.gg/3YmDAzbuRR)**"
    for cmd in cog.get_commands():
      if not cmd.hidden:
        _brief = cmd.short_doc if cmd.short_doc else "No Help Provided..."
     # otay = ', '.join(f"`<{param}>`" for param in cmd.clean_params)
      #params = [param for param in cmd.clean_params]
        embed.add_field(name=f"Command Details:", value=f"<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Name:** `{self.context.prefix}{cmd.name}`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> **Description:** `{_brief}`\n\n", inline=False)
    embed.timestamp = discord.utils.utcnow()
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/l7vKMv604vRFUX251EGvc9MWNmFqwBYmcF_8IVYRmug/https/cdn.discordapp.com/emojis/1053153617353396234.png")    
        
    embed.set_footer(text="Reminder : Hooks such as <> must not be used when executing commands.", icon_url="")
    await self.context.send(embed=embed)

class Help(Cog, name="help "):
  def __init__(self, client:Astroz):
    self._original_help_command = client.help_command
    attributes = {
            'name': "Commands",
            'aliases': ['command','cmd','cmds','helpcmd','helpcmds','hc'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user),
            'help': 'Shows commands of this bot'
        }
    client.help_command = HelpCommand(command_attrs=attributes)
    client.help_command.cog = self

  async def cog_unload(self):
    self.help_command = self._original_help_command
