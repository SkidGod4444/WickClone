from __future__ import annotations
#____________ Commands ___________
from .commands.help import Help
from .commands.Moderation import Moderation
from .commands.extras import Extra
from .commands.Anti_cmds import Antinuke
from .commands.Owner import Owner
from .commands.Antiraid_cmds import Antiraid
from .commands.Logging import Logging
from .commands.Games import Games
#____________ Events _____________
from .events.antiban import antiban
from .events.antichannel import antichannel
from .events.antiguild import antiguild
from .events.antirole import antirole
from .events.antibot import antibot
from .events.antikick import antikick
from .events.antiprune import antiprune
from .events.antiwebhook import antiwebhook
from .events.antiping import antipinginv
from .events.antiemostick import antiemostick
from .events.antintegration import antintegration
from .events.antispam import AntiSpam
from .events.autoblacklist import AutoBlacklist
from .events.antiemojid import antiemojid
from .events.antiemojiu import antiemojiu
from .events.Errors import Errors
from .events.on_guild import Guild
#
#
from core import Darkz

async def setup(bot: Darkz):
  await bot.add_cog(Help(bot))
  print('Help Command Loaded')
  await bot.add_cog(Moderation(bot))
  print("Moderation Cog Loaded")
  await bot.add_cog(Extra(bot))
  print("Extras Cog Loaded")
  await bot.add_cog(Antinuke(bot))
  print("Antinuke commands Cog Loaded")
  await bot.add_cog(Owner(bot))
  print("Owner commands Cog Loaded")
  await bot.add_cog(Antiraid(bot))
  print("Antiraid commands Cog Loaded")
  await bot.add_cog(antiban(bot))
  await bot.add_cog(antichannel(bot))
  await bot.add_cog(antiguild(bot))
  await bot.add_cog(antirole(bot))
  await bot.add_cog(antibot(bot))
  await bot.add_cog(antikick(bot))
  await bot.add_cog(antiprune(bot))
  await bot.add_cog(antiwebhook(bot))
  await bot.add_cog(antipinginv(bot))
  await bot.add_cog(antiemostick(bot))
  await bot.add_cog(antintegration(bot))  
  await bot.add_cog(AntiSpam(bot))
  await bot.add_cog(AutoBlacklist(bot))
  await bot.add_cog(antiemojid(bot))
  await bot.add_cog(antiemojiu(bot))
  await bot.add_cog(Guild(bot))
  print("Cog loaded: Guild")
  await bot.add_cog(Errors(bot))
  await bot.add_cog(Logging(bot))
  print("Logging Cog loaded")
  await bot.add_cog(Games(bot))
  print("Cog Loaded: Games")