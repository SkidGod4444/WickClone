import discord
from discord.ext import commands


class himanshu4444(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """ServerRole commands"""
  
    def help_custom(self):
		      emoji = '<:Sputnik:1056733377073532978>'
		      label = "ServerRoles"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __ServerRoles__(self, ctx: commands.Context):
        """`setup_girls <role>` , `setup_vip <role>` , `setup_friend <role>` , `setup_staff <role>` , `setup_guest <role>` , `setup_special <role>` , `girl <user>` , `vip <user>` , `friend <user> ` , `staff <user>` , `guest <user>` , `special <user>` , `rgirl <user>` , `rvip <user>` , `rfriend <user> ` , `rstaff <user>` , `rguest <user>` , `rspecial <user>` \n\n**__Need more?__**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> Only commands you can use are displayed! If you lack permissions, you might use some other commands.\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452>  If you want to view more details about a command, type the command and add `helpcmd` before it, for an example: `s!helpcmd ban`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you have questions, [Join Our Support Server](https://discord.gg/3YmDAzbuRR)"""