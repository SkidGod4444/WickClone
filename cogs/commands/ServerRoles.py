from __future__ import annotations
from discord.ext import commands
from utils.Tools import *
from utils.config import OWNER_IDS, No_Prefix
import json, discord
import typing
from typing import Optional
class Owner(commands.Cog):
  def __init__(self, client):
    self.client = client

@client.command(aliases=['setup-friends'])
