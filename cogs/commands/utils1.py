import discord
from discord.ext import commands


class hacker111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Utils commands"""
  
    def help_custom(self):
		      emoji = '<:Sputnik:1056733377073532978>'
		      label = "Utils"
		      description = ""
		      return emoji, label, description

    @commands.group()
    async def __Utils__(self, ctx: commands.Context):
        """`purge` , `purge contains` , `purge startswith` , `purge invites` , `purge user` ,`clear` , `clear all` , `clear bots` , `clear embeds` , `clear files` , `clear mentions` , `clear images` , `clear contains` , `clear reactions`\n\n**__Need more?__**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> Only commands you can use are displayed! If you lack permissions, you might use some other commands.\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452>  If you want to view more details about a command, type the command and add `helpcmd` before it, for an example: `s!helpcmd ban`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you have questions, [Join Our Support Server](https://discord.gg/3YmDAzbuRR)"""