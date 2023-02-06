import discord
import logging
from discord.ext import commands
import motor.motor_asyncio as mongodb

class ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.color = 0x2f3136
        self.connection = mongodb.AsyncIOMotorClient("mongodb+srv://insane:op5@cluster0.5qyw6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.connection["Sputnik"]["servers"]


    @commands.Cog.listener()
    async def on_ready(self):
        for server in self.bot.guilds:
            data = await self.db.find_one({"guild": server.id})
            if data == None:
                await self.db.insert_one(
                    {
                        "guild": server.id,
                        "log-channel": None,
                        "delete-after" : None,
                        "joinvc": {
                            "channelid": None,
                            "enabled": False
                        },
                        "vcrole": {
                            "roleid": None,
                            "enabled": False
                        },
                        "autorole": [],
                        "humans": [],
                        "bots": [],
                        "welcome": {
                            "message": None,
                            "channel": None,
                            "enabled": False,
                            "embed": False,
                            "title": None,
                            "description": None,
                            "thumbnail": None,
                            "image": None
                        }
                    }
                )

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        await self.db.insert_one(
            {
                "guild": guild.id,
                "log-channel": None, 
                "delete-after" : None,
                "joinvc": {
                    "channelid": None,
                    "enabled": False
                },
                "vcrole": {
                    "roleid": None,
                    "enabled": False
                },
                "autorole": [],
                "humans": [],
                "bots": [],
                "welcome": {
                    "message": None,
                    "channel": None,
                    "enabled": False,
                    "embed": False,
                    "title": None,
                    "description": None,
                    "thumbnail": None,
                    "image": None
                }
            }
        )

    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        logging.info("Shard #%s is ready" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_connect(self, shard_id):
        logging.info("Shard #%s has connected" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_disconnect(self, shard_id):
        logging.info("Shard #%s has disconnected" % (shard_id))

    @commands.Cog.listener()
    async def on_shard_resume(self, shard_id):
        logging.info("Shard #%s has resumed" % (shard_id))