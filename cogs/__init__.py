from __future__ import annotations
from core import Astroz



#____________ Commands ___________

#####################3
from .commands.help import Help
from .commands.general import General
#from .commands.music import Music
#from .commands.Setup import AntiAltsSelectionView
from .commands.moderation import Moderation
from .commands.Anti_cmds import Security
from .commands.raidmode import Raidmode
from .commands.logging import Logging
#from .commands.welcome import Welcome
#from .commands.vc import Voice
#from .commands.utils import Utils
from .commands.extra import Extra
from .commands.owner import Owner
from .commands.timer import timer
#from .commands.ignore import ignore 

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

from .events.join import Join
from .events.Errors import Errors
from .events.on_guild import Guild
from .events.on_member_join import welcome_event
from .events.ready import ready



##############33cogs#############
from .commands.general1 import hacker1
#from .commands.music1 import hacker11
from .commands.mod2 import hacker111
from .commands.anti1 import hacker1111
from .commands.trusted1 import trusted69
from .commands.raidmode1 import hacker11111
#from .commands.logging2 import hacker111111
#from .commands.welcome1 import hacker1111111
#from .commands.vc1 import hacker11111111
##from .commands.utils1 import hacker111111111
from .commands.extra1 import hacker1111111111
from .commands.ServerRoles1 import himanshu4444







async def setup(bot: Astroz):
  await bot.add_cog(Help(bot))
  await bot.add_cog(General(bot))
 # await bot.add_cog(Music(bot))
  await bot.add_cog(Moderation(bot))
  await bot.add_cog(Security(bot))
 # await bot.add_cog(Trusted(bot))
  await bot.add_cog(Raidmode(bot))
 # await bot.add_cog(Logging(bot))
 # await bot.add_cog(Welcome(bot))
 # await bot.add_cog(Voice(bot))
 # await bot.add_cog(Utils(bot))
  await bot.add_cog(Extra(bot))
  await bot.add_cog(Owner(bot))
  await bot.add_cog(timer(bot))
  #await #bot.add_cog(AntiAltsSelectionView(bot))
#  await bot.add_cog(ignore(bot))
 # await bot.add_cog(ServerRoles(bot))
  
####################

  await bot.add_cog(hacker1(bot))
 # await bot.add_cog(hacker11(bot))
  await bot.add_cog(hacker111(bot))
  await bot.add_cog(hacker1111(bot))
  await bot.add_cog(trusted69(bot))
  await bot.add_cog(hacker11111(bot))
  
#  await bot.add_cog(hacker111111(bot))
 # await bot.add_cog(hacker1111111(bot))
 # await bot.add_cog(hacker11111111(bot))
  #utils wala hawait bot.add_cog(hacker111111111(bot))
  await bot.add_cog(hacker1111111111(bot))
  await bot.add_cog(himanshu4444(bot))


###########################events################3
  
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
  await bot.add_cog(Errors(bot))
  await bot.add_cog(welcome_event(bot))
  await bot.add_cog(Join(bot))
 # await bot.add_cog(Dropdown(bot))