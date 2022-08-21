import os
os.system("pip install git+https://github.com/eagle37/Discord-Games && pip install tasksio && pip install httpx")
os.system("pip install discord.py[speed] && pip install jishaku && pip install psutil && pip install pynacl")
from core.darkz import Darkz
import asyncio, time, aiohttp, json
import jishaku, cogs
import psutil

#from keep_alive import keep_alive

#keep_alive()

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"


client = Darkz()

async def protect_vanity(guildid):
      start = time.perf_counter()
      with open('vanity.json') as idk:
        code = json.load(idk)
        if code[str(guildid)] != "":
          header = {"Authorization": "Bot ODUyOTE5NDIzMDE4NTk4NDMw.GoxHP1.xHwxbepouv5-7IJbvyL5Espvi6j_JOMvwMm1mY", "X-Audit-Log-Reason": "Darkz Security | Anti Vanity"}
          async with aiohttp.ClientSession(headers=header) as session:
            jsonn = {"code": code[str(guildid)]}
            async with session.patch(f"https://ptb.discord.com/api/v10/guilds/{guildid}/vanity-url", json=jsonn) as response:
              end = time.perf_counter()
              print(f"{end - start} | {response.status}")
        else:
          return

@client.listen("on_guild_update")
async def on_vanity_update(before, after):
  with open("vanity.json", "r") as f:
    data = json.load(f)
  if before.vanity_url_code != after.vanity_url_code:
    await asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[asyncio.gather(*[protect_vanity(before.id)])])])])])])])])])])])])
  else:
    return


async def main():
    async with client:
      os.system("clear")
      await client.load_extension("cogs")
      await client.load_extension("jishaku")
   #   await client.load_extension("pynacl")
      await client.start("ODUyOTE5NDIzMDE4NTk4NDMw.GoxHP1.xHwxbepouv5-7IJbvyL5Espvi6j_JOMvwMm1mY")

if __name__ == "__main__":
  asyncio.run(main())