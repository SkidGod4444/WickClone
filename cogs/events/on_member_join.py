import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb
from discord.colour import Color

logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;197m[\x1b[0m%(asctime)s\x1b[38;5;197m]\x1b[0m -> \x1b[38;5;197m%(message)s\x1b[0m",
    datefmt="%H:%M:%S",
)

class welcome_event(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.color = discord.Colour.green()
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://insane:op5@cluster0.5qyw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.connection["Spu"]["servers"]

    @commands.Cog.listener()
    async def on_member_join(self, user):
        try:
            guild = user.guild
            data = await self.db.find_one({"guild": guild.id})

            if data["welcome"]["enabled"] != True:
                return 
            if data["welcome"]["message"] == None:
                return
            if data["welcome"]["channel"] == None:
                return

            channel = self.client.get_channel(data["welcome"]["channel"])
            message = data["welcome"]["message"]
            if "{user.id}" in message:
                    message = message.replace("{user.id}", "%s" % (user.id))

            if "{user.mention}" in message:
                message = message.replace("{user.mention}", "%s" % (user.mention))

            if "{user.tag}" in message:
                message = message.replace("{user.tag}", "%s" % (user.discriminator))

            if "{user.name}" in message:
                message = message.replace("{user.name}", "%s" % (user.name))
                
            if "{user.avatar}" in message:
                message = message.replace("{user.avatar}", "%s" % (user.avatar_url))

            if "{server.name}" in message:
                message = message.replace("{server.name}", "%s" % (user.guild.name))
                
            if "{server.membercount}" in message:
                message = message.replace("{server.membercount}", "%s" % (user.guild.member_count))
                
            if "{server.icon}" in message:
                message = message.replace("{server.icon}", "%s" % (user.guild.icon_url))
            
            await channel.send(user.mention, embed=discord.Embed(
                description=message,
                color = 0x00FFE4))
        except Exception:
            pass