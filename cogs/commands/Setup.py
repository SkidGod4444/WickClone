
import discord
import re
import urllib
import typing as t

from discord.ext import commands
import emojis
from datetime import datetime
from re import search
from collections import Counter
from typing import Optional, Union
from utils.message import wait_for_msg
#from utils.embed import error_embed, success_embed
#from utils.checks import getConfig, updateConfig, is_admin
#from config import (
   # BADGE_EMOJIS, EMOJIS, RED_COLOR
#)
#from utils.bot import EpicBot

#prefix = ">"

class AntiAltsSelectionView(discord.ui.View):
    def __init__(self, context):
        super().__init__(timeout=None)
        self.level = 0
        self.context = context
        self.cancelled = False

             if config is None:
            return await ctx.reply(embed=info_embed)

        if config.lower() == 'setup':

            log_channel = None

            view = AntiAltsSelectionView(context=ctx)
            msg = await ctx.reply(f"""
**Anti Nuke setup**
- {EMOJIS['idle']} Punishment.
- {EMOJIS['dnd']} Log channel.
Please select a protection level.
                                """, view=view)

            await view.wait()

            if view.cancelled:
                return await msg.edit(
                    content="",
                    embed=discord.Embed(title=f"{EMOJIS['tick_no']} Cancelled", color=RED_COLOR),
                    view=None
                )
            await msg.edit(f"""
**Anti Nuke setup**
- {EMOJIS['online']} Punishment `{view.level}`
- {EMOJIS['idle']} Log channel.
Please enter a log channel.
Type `create` to automatically create a channel.
Type `cancel` to cancel the command.
                            """, view=None)
            m = await wait_for_msg(ctx, 60, msg)
            if m == 'pain':
                return
            if m.content.lower() == 'create':
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
                }
                created_channel = await ctx.guild.create_text_channel('summrs-log', overwrites=overwrites)
                log_channel = created_channel.id
            else:
                try:
                    lul_channel = await commands.TextChannelConverter().convert(ctx=ctx, argument=m.content)
                    log_channel = lul_channel.id
                except commands.ChannelNotFound:
                    return await msg.reply(content="", (
                        f"{EMOJIS['tick_no']} Not found!",
                        f"I wasn't able to find the channel {m.content}, please try again."
                    ), view=None)

            await msg.edit(f"""
**Setup complete**
Here are you settings:
- {EMOJIS['online']} Level: `{view.level}`
- {EMOJIS['online']} Log channel: <#{log_channel}>
                            """)

          #  g['Punishment'] = int(view.level)
            g['log_channel'] = log_channel
            updateConfig(ctx.guild.id, g)
            return


        if config.lower() == 'channel':
            if config is None:
                return await ctx.reply(embed=discord.embed(description=f" Invalid Usage", f"Please use `{prefix}antinuke channel #channel`"))
            if not isinstance(setting, discord.TextChannel):
                return await ctx.reply(f"{EMOJIS['tick_no']} Not found!", f"I wasn't able to find channel {setting}, please try again."))
            g['log_channel'] = setting.id
            updateConfig(ctx.guild.id, g)
            return await embed=discord.embed(description=f"lund!"(
              #  f"{EMOJIS['tick_yes']} Updated!",
              #  f"The log channel has been updated to {setting.mention}"
            ))

        else:
            return await ctx.reply(embed=embed)      