import discord
from discord.ext import commands
from difflib import get_close_matches
from contextlib import suppress
from core import Context
from core.darkz import Darkz
from core.Cog import Cog
from utils.Tools import getConfig
from itertools import chain
import json
client = Darkz()

class HelpView(discord.ui.Select):
  def __init__(self):
    opts = [discord.SelectOption(label="Antinuke", emoji="<:meri_sheild:916277086396755988>"), 
           discord.SelectOption(label="Antiraid", emoji="<:stolen_emoji:973119620842139658>"), 
           discord.SelectOption(label="Moderation", emoji="<:mod:939046461407125554>"), 
           discord.SelectOption(label="Extra", emoji="<a:header:920230682993762325>"), 
           discord.SelectOption(label="Logging", emoji="<:zzlogging:993035141825957899>"), 
          discord.SelectOption(label="Games", emoji="<:games:1007201363735871489>")]
    super().__init__(placeholder="Select a category...", max_values=1, min_values=1, options=opts)

  async def callback(self, interaction: discord.Interaction):
      antinuke = interaction.client.get_cog("Antinuke")
      embed_anti = discord.Embed(title=f"{antinuke.qualified_name.title()}", description=antinuke.description, color=discord.Colour(0x2f3136))
      fox = ', '.join([cmd.qualified_name for cmd in antinuke.get_commands() if not cmd.hidden])
      embed_anti.add_field(name="Commands...\n", value=fox, inline=False)
      antiraid = interaction.client.get_cog("Antiraid")
      embed_raid = discord.Embed(title="{}".format(antiraid.qualified_name.title()), description=antiraid.description, color=discord.Colour(0x2f3136))
      lmao = ', '.join([cmd.qualified_name for cmd in antiraid.get_commands() if not cmd.hidden])
      embed_raid.add_field(name="Commands...\n", value=lmao, inline=False)
      mod = interaction.client.get_cog("Moderation")
      embed_mod = discord.Embed(title=mod.qualified_name.title(), description=mod.description, color=discord.Colour(0x2f3136))
      popcorn = ', '.join([cmd.qualified_name for cmd in mod.get_commands() if not cmd.hidden])
      embed_mod.add_field(name="Commands...\n", value=popcorn, inline=False)
      extra = interaction.client.get_cog("Extra")
      embed_extra = discord.Embed(title=extra.qualified_name.title(), description=extra.description, color=discord.Colour(0x2f3136))
      duck = ', '.join([cmd.qualified_name for cmd in extra.get_commands() if not cmd.hidden])
      embed_extra.add_field(name="Commands...\n", value=duck, inline=False)
      logs = interaction.client.get_cog("Logging")
      embed_logs = discord.Embed(title=logs.qualified_name.title(), description=logs.description, color=discord.Colour(0x2f3136))
      aaa = ', '.join([cmd.qualified_name for cmd in logs.get_commands() if not cmd.hidden])
      embed_logs.add_field(name="Commands...\n", value=aaa, inline=False)
      game = interaction.client.get_cog("Games")
      embed_game = discord.Embed(title=game.qualified_name.title(), description=game.description, color=discord.Colour(0x2f3136))
      mmmm = ', '.join([cmd.qualified_name for cmd in game.get_commands()])
      embed_game.add_field(name="Commands...\n", value=mmmm, inline=False)
      if self.values[0] == "Antinuke":
        await interaction.response.send_message(embed=embed_anti, ephemeral=True)
      elif self.values[0] == "Antiraid":
        await interaction.response.send_message(embed=embed_raid, ephemeral=True)
      elif self.values[0] == "Moderation":
        await interaction.response.send_message(embed=embed_mod, ephemeral=True)
      elif self.values[0] == "Extra":
        await interaction.response.send_message(embed=embed_extra, ephemeral=True)
      elif self.values[0] == "Logging":
        await interaction.response.send_message(embed=embed_logs, ephemeral=True)
      elif self.values[0] == "Games":
        await interaction.response.send_message(embed=embed_game, ephemeral=True)

class dropdown(discord.ui.View):
  def __init__(self, *, timeout=120):
     super().__init__(timeout=timeout)
     self.add_item(HelpView())
     self.response = None
    

  async def on_timeout(self):
    for child in self.children:
      child.disabled = True
    await self.response.edit(view=self)

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
      embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
      await self.context.reply(embed=embed, mention_author=False)
    else:
      

      if string in ("antinuke", "AntiNuke"):
        cog = self.context.bot.get_cog("Antinuke")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("AntiRaid", "antiraid"):
        cog = self.context.bot.get_cog("Antiraid")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("Mod", "moderation", "mod"):
        cog = self.context.bot.get_cog("Moderation")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("extra", "extras"):
        cog = self.context.bot.get_cog("Extra")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("logging", "logs"):
        cog = self.context.bot.get_cog("Logging")
        with suppress(discord.HTTPException):
          await self.send_cog_help(cog)
      elif string in ("games", "game", "gaming"):
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
        return msg

  
  async def send_bot_help(self, mapping):
    await self.context.typing()
    with open('blacklist.json', 'r') as f:
      bled = json.load(f)
    if str(self.context.author.id) in bled["ids"]:
      embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
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
    embed = discord.Embed(title=f"Help", description=f"• Global Prefix is `$` | (here) `{prefix}`\n• Total Commands: {len(set(self.context.bot.walk_commands()))}\n• [Get Darkz](https://discord.com/oauth2/authorize?client_id=852919423018598430&permissions=2113268958&redirect_uri=https://discord.gg/7QHkdV9Zte&response_type=code&scope=bot) | [Support Server](https://discord.gg/7QHkdV9Zte) | [Vote Me](https://top.gg/bot/852919423018598430/vote)\n• Type `{prefix}help [command/module]` for more info\n• ```<> - Required Argument | [] - Optional Argument```", color=discord.Colour(0x2f3136))
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/937666181295398922.png")
    embed.set_footer(text="Made With 💖 By Eagle[.]#0831", icon_url=self.context.author.display_avatar.url)
    embed.add_field(name="Darkz Security", value=f"<:meri_sheild:916277086396755988> help Antinuke\n<:stolen_emoji:973119620842139658> help Antiraid\n<:mod:939046461407125554> help Moderation\n<a:header:920230682993762325> help Extra\n<:zzlogging:993035141825957899> help Logging\n<:games:1007201363735871489> help Games", inline=False)
    embed.set_author(name="Darkz Security", icon_url=self.context.author.display_avatar.url)
    embed.timestamp = discord.utils.utcnow()
    #return embed
    view = dropdown()
    ok = await self.context.reply(embed=embed, mention_author=False, view=view)
    view.response = ok

  async def send_command_help(self, command):
    with open('blacklist.json', 'r') as f:
       data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
       embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
       await self.context.reply(embed=embed, mention_author=False)
    else:
       embed = discord.Embed(title=f"• {command.cog.qualified_name.title()}", description=f"```toml\n- [] = optional argument\n- <> = required argument\n- Do NOT Type These When Using Command```\n\n", color=discord.Colour(0x2f3136))
       alias = ' | '.join(command.aliases)
       embed.add_field(name="Help", value=f">>> {command.help}" if command.help else '>>> No Help Provided...', inline=False)
       embed.add_field(name="**Aliases**", value=f"{alias}" if command.aliases else "No Aliases", inline=False)
       embed.add_field(name="**Usage**", value=f"`{self.context.prefix}{command.name} {command.signature}`\n")
       #embed.set_author(name="- [] = optional argument\n- <> = required argument\nDo NOT Type These When Using Command ", icon_url=self.context.author.display_avatar.url)
       embed.set_footer(text=f"{self.context.author}", icon_url=self.context.author.display_avatar.url)
       embed.set_author(name="Darkz Security", icon_url=self.context.author.display_avatar.url if self.context.author.display_avatar else None)
       embed.set_thumbnail(url=self.context.author.display_avatar.url)
       embed.timestamp = discord.utils.utcnow()
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
        embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
        await self.context.reply(embed=embed, mention_author=False)
    else:
        await self.context.typing()
        data = getConfig(self.context.guild.id)
        prefix = data["prefix"]

        if not group.commands:
            return await self.send_command_help(group)

        embed = discord.Embed(color=discord.Colour(0x2f3136))

        embed.title = f"{group.qualified_name} {group.signature}"
        _help = group.help or "No description provided..."

        _cmds = "\n\n".join(f"`{prefix}{c.qualified_name}`\n{c.short_doc}" for c in group.commands)

        embed.description = f"> {_help}\n\n**Subcommands**\n{_cmds}"

        embed.set_footer(text=f'Use {prefix}help <command> for more information.')

        if group.aliases:
            embed.add_field(name="Aliases", value=", ".join(f"`{aliases}`" for aliases in group.aliases), inline=False)
        embed.timestamp = discord.utils.utcnow()
        await self.context.send(embed=embed)

  async def send_cog_help(self, cog):
    with open('blacklist.json', 'r') as f:
      data = json.load(f)
    if str(self.context.author.id) in data["ids"]:
      embed = discord.Embed(title="<:error_ok:946729104126922802> Blacklisted", description="You Are Blacklisted From Using My Commands.\nIf You Think That It Is A Mistake, You Can Appeal In Our Support Server By Clicking [here](https://discord.gg/7QHkdV9Zte)", color=discord.Colour(0x2f3136))
      return await self.context.reply(embed=embed, mention_author=False)
    await self.context.typing()
    embed = discord.Embed(color=discord.Colour(0x2f3136))
    embed.title = cog.qualified_name.title()
    desc = "No Description Provided..." if not cog.description else cog.description
    embed.description = f"> {desc}\n\n**Commands**\n\n\n"
    for cmd in cog.get_commands():
      if not cmd.hidden:
        _brief = cmd.short_doc if cmd.short_doc else "No Help Provided..."
     # otay = ', '.join(f"`<{param}>`" for param in cmd.clean_params)
      #params = [param for param in cmd.clean_params]
        embed.add_field(name=f"`{self.context.prefix}{cmd.name} {cmd.signature}`\n", value=f"{_brief}", inline=False)
    embed.timestamp = discord.utils.utcnow()
    await self.context.send(embed=embed)

class Help(Cog, name="help "):
  def __init__(self, client: Darkz):
    self._original_help_command = client.help_command
    attributes = {
            'name': "help",
            'aliases': ['h'],
            'cooldown': commands.CooldownMapping.from_cooldown(1, 5, commands.BucketType.user),
            'help': 'Shows help about bot, a command or a category'
        }
    client.help_command = HelpCommand(command_attrs=attributes)
    client.help_command.cog = self

  async def cog_unload(self):
    self.help_command = self._original_help_command