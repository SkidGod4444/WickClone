import os
import discord
import aiohttp
from discord.ext import commands, tasks
from discord.colour import Color
import json
import random
from discord.ui import Button, View
#from utils.checks import getConfig, updateConfig

#https://cdn.discordapp.com/attachments/1027593292642275418/1028516662221226024/Proton.png

class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
         # data = getConfig(guild.id)
          #key = "".join(random.choice("aAbBcCdDeE1234567890nNmMkKiIuUyY") for _ in range(6))
         # data['backupkey'] = key
          #updateConfig(guild.id, data)
          embed = discord.Embed(
            title="Thnkx for choosing Sputnik!",description=f"<:tixk:1053178188613820468> `Sputnik` has been added to `{guild.name}` successfully!\n<:1spacer:1056545806943006760>\nYou can setup the whole bot in your server by  doing; **[s!help](https://discord.gg/3YmDAzbuRR)** and following the needed steps.\nYou can also read the **[Documentation](https://discord.gg/3YmDAzbuRR)** if your want to know more about.",
            color=0xdbdbdb
          )
          skidgod = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
          #web = Button(label='Website', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
          docs = Button(label='Documentation',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # premium = Button(label='Premium',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # vote = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
          view = View()
         # view.add_item(b)
          view.add_item(skidgod) 
          #view.add_item(web)
          view.add_item(docs)
            
          await guild.owner.send(embed=embed,view=view)

       #   himanshu = discord.Embed(
      #      title="Security!",description=f"Key - `{key}`\n<:1spacer:1056545806943006760>\nYou must keep this key safe this will be usefull in future!",
          #  color=0xdbdbdb
         # )
      

                   
         # await guild.owner.send(embed=himanshu)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
         
          embed = discord.Embed(
            title="It looks like someone has removed Sputnik!",description=f"<:ellor:1056829282858573925> `Sputnik` has been removed from `{guild.name}`\n<:1spacer:1056545806943006760>\nIf it was a mistake then re-add `Sputnik` to your server\nDon't worry you can restore all the settings by just re-adding!\nYou can also read the **[Documentation](https://discord.gg/3YmDAzbuRR)** if your want to know more about.",
            color=0xdbdbdb
          )
          skidgod = Button(label='Support Server', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
         # web = Button(label='Website', style=discord.ButtonStyle.link, url='https://discord.gg/3YmDAzbuRR')
          docs = Button(label='Documentation',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # premium = Button(label='Premium',style=discord.ButtonStyle.link,url='https://discord.gg/3YmDAzbuRR')
       # vote = Button(label='Vote Me', style=discord.ButtonStyle.link, url='https://discord.com/oauth2/authorize?client_id=1021416292185546854&permissions=2113268958&scope=bot')
          view = View()
         # view.add_item(b)
          view.add_item(skidgod) 
          #view.add_item(web)
          view.add_item(docs)          
          await guild.owner.send(embed=embed,view=view)

