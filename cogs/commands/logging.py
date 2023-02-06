import discord, json
from discord.ext import commands
import os
os.system("pip install pymongo[srv]")
import motor.motor_asyncio as mongodb
from utils.Tools import *

class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://insane:op5@cluster0.5qyw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.connection["Sputnik"]["servers"]

    @commands.group(name="logging", description="logging channel\nlogging config\nlogging delete", invoke_without_command=True)
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    async def logging(self, ctx):
      if ctx.subcommand_passed is None:
          await ctx.send_help(ctx.command)
          ctx.command.reset_cooldown(ctx)

    @logging.command(usage="logging channel <channel>")
    @blacklist_check()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def channel(self, ctx, c: discord.TextChannel):
        try:
            await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "log-channel" : c.id
                    }
                }
            )
            embed = discord.Embed(
        description = f'<:GreenTick:1029990379623292938>  | All logs channel are updated to <#{c.id}>',
        color=0x00FFE4
      )
            embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
            #embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/1024854362801057884/af987937665a69cc5fc01f587179d7ae.webp?size=2048")
            #embed.set_footer(text="Made With 💖 By ~ Hacker_xD",icon_url="https://media.discordapp.net/attachments/1004709672588161044/1005073754889654343/a_9a2d97cca8cf934ac4b3624051ed9baf.gif")

            await ctx.send(embed=embed)
        except Exception as e:
            return await ctx.send(f"An error occoured {e}")


    @logging.command(aliases=['show'], usage="logging config")
    @blacklist_check()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def config(self, ctx):
        data = await self.db.find_one({"guild": ctx.guild.id})     
        x = data["log-channel","mem-join-channel"]
        if x == None:
          embed = discord.Embed(title=f"Logging channel for {ctx.guild.name}", description=f"No Logging Channel Found", color=0x00FFE4)
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(title=f"Logging config for {ctx.guild.name}", description=f"<#{x}>",color=0x00FFE4)
          embed.set_author(name=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
          await ctx.send(embed=embed)

    @logging.command( usage="logging delete")
    @blacklist_check()
    @commands.is_owner()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx: commands.Context):
        await self.db.update_one(
                {
                    "guild": ctx.guild.id
                },
                {
                    "$set": {
                        "log-channel" : None
                    }
                }
            )

        embed = discord.Embed(
        description = f'<:GreenTick:1029990379623292938> | Successfully Deleted Logging Channel',
        color=0x00FFE4
      )
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar}")
       # embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/1024854362801057884/af987937665a69cc5fc01f587179d7ae.webp?size=2048")
        #embed.set_footer(text="Made With 💖 By ~ Hacker_xD",icon_url="https://media.discordapp.net/attachments/1004709672588161044/1005073754889654343/a_9a2d97cca8cf934ac4b3624051ed9baf.gif")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.bot:
            return
        data = await self.db.find_one({"guild": member.guild.id})     
        x = data["mem-log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          member1 = int(member.created_at.timestamp())
          embed = discord.Embed(title="A member has joined the server.", description=f"{member.mention} | {member.id}\n:bust_in_silhouette: Account created at <t:{member1}:D>", color=0x00FFE4)
          embed.timestamp = discord.utils.utcnow()          
          
          embed.set_footer(text="JOIN")
          await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.bot:
            return
        data = await self.db.find_one({"guild": member.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          member1 = int(member.created_at.timestamp())
          embed = discord.Embed(title="A member is no longer in the server.", description=f"{member.name} | {member.id}\n :bust_in_silhouette: Account created at <t:{member1}:D>", color=0x00FFE4)
          embed.timestamp = discord.utils.utcnow()      
          
          
          embed.set_footer(text="LEFT")
          await channel.send(embed=embed)

    # CHANNEL LOGGING

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        data = await self.db.find_one({"guild": channel.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          c = self.bot.get_channel(x)
          embed = discord.Embed(description=f"New channel ({channel.mention}) has beeen Created ", color=0x00FFE4)
          embed.add_field(name=f"Name", value=f"{channel.name} (ID: {channel.id})")
          embed.add_field(name=f"Position", value=f"{channel.position}")
          embed.set_footer(text="CHANNEL CREATE")
          embed.timestamp = discord.utils.utcnow()
          await c.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        data = await self.db.find_one({"guild": channel.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          c = self.bot.get_channel(x)
          embed = discord.Embed(description="A channel has been deleted", color = 0x886ad1)
          embed.add_field(name=f"Name", value=f"{channel.name} (ID: {channel.id})")
          embed.add_field(name=f"Position", value=f"{channel.position}")
          embed.set_footer(text="CHANNEL DELETE")
          embed.timestamp = discord.utils.utcnow()
          await c.send(embed=embed)
    
    # ROLE LOGGING
    
    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        data = await self.db.find_one({"guild": role.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"New role ({role.mention}) has been Created", color=0x00FFE4)
          embed.add_field(name="Name", value=f"{role.name} (ID: {role.id})")
          embed.add_field(name="Color", value=f"{role.colour}")
          embed.add_field(name="Postion", value=f"{role.position}")
          embed.set_footer(text="ROLE CREATE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        data = await self.db.find_one({"guild": role.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"Role ({role.mention}) has been Deleted", color=0x00FFE4)
          embed.add_field(name="Name", value=f"{role.name} (ID: {role.id})")
          embed.add_field(name="Color", value=f"{role.colour}")
          embed.add_field(name="Postion", value=f"{role.position}")
          embed.set_footer(text="ROLE DELETE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    # MESSAGE LOGGGING

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload: discord.RawMessageDeleteEvent):
        data = await self.db.find_one({"guild": payload.guild_id})     
        x = data["log-channel"]
        if x == None:
          return
        else: 
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f':put_litter_in_its_place: Message sent by {payload.cached_message.author.mention} deleted in <#{payload.channel_id}>', color=0x00FFE4)
          embed.add_field(name=f"Deleted By", value=f"{payload.cached_message.author.mention}")
          embed.add_field(name="Message", value=f"{payload.cached_message.content}")
          embed.set_footer(text="MESSAGE DELETE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if before.author.bot:
            return
        data = await self.db.find_one({"guild": before.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else: 
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f":pencil: Message sent by {before.author.mention} edited in {before.channel.mention} [Jump to message](https://discord.com/channels/{before.guild.id}/{before.channel.id}/{before.id})", color=0x00FFE4)
          embed.add_field(name="Before:", value=f"```{before.content}```")
          embed.add_field(name="After:", value=f"```{after.content}```")
          embed.set_author(name=before.author.name)
          embed.set_footer(text=f"EDITED")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    # BAN AND UNBAN
    @commands.Cog.listener()
    async def on_member_ban(self, member):
        data = await self.db.find_one({"guild": member.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description="Member has been unbanned from this server.",color=0x00FFE4)
          embed.add_field(name="User", value=f"{member.name}")
          embed.set_author(name=f"{member.name}#{member.discriminator}")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

        
    @commands.Cog.listener()
    async def on_member_unban(self, member):
        data = await self.db.find_one({"guild": member.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description="Member has been banned from this server.",color=0x00FFE4)
          embed.add_field(name="User", value=f"{member.name}")
          embed.set_author(name=f"{member.name}#{member.discriminator}")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)


        
    # EMOJI CREATE AND EMOJI REMOVE
    @commands.Cog.listener()
    async def on_guild_emoji_create(self, emoji):
        data = await self.db.find_one({"guild": emoji.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"Emoji ({emoji}) has been added.", color=0x00FFE4)
          embed.set_footer(text="EMOJI CREATE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_emoji_remove(self, emoji):
        data = await self.db.find_one({"guild": emoji.guild.id})     
        x = data["log-channel"]
        if x == None:
          return
        else:  
          channel = self.bot.get_channel(x)
          embed = discord.Embed(description=f"Emoji ({emoji}) has been deleted.", color=0x00FFE4)
          embed.set_footer(text="EMOJI DELETE")
          embed.timestamp = discord.utils.utcnow()
          await channel.send(embed=embed)
