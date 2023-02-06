import os
#os.system("pip install git+https://github.com/NotHerHacker/jishaku && pip install tasksio && pip install httpx")
#os.system("pip install discord.py[speed] && pip install jishaku && pip install psutil && pip install pynacl")
#os.system("pip install git+https://github.com/NotHerHacker/jishaku")
#os.system("pip install git+https://github.com/NotHerHacker/Discord-Games")   
     


from core.Astroz import Astroz
import asyncio, time, aiohttp, json
import jishaku, cogs
import psutil
import discord
from discord.ext import commands
from discord import app_commands
import traceback
from discord.ui import Button, View



os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"


client = Astroz()
tree = client.tree

class Embed(discord.ui.Modal, title='Embed Configuration'):
    tit = discord.ui.TextInput(
        label='Embed Title',
        placeholder='Embed title here',
    )

    description = discord.ui.TextInput(
        label='Embed Description',
        style=discord.TextStyle.long,
        placeholder='Embed description optional',
        required=False,
        max_length=4000,
    )

    thumbnail = discord.ui.TextInput(
        label='Embed Thumbnail',
        placeholder='Embed thumbnail here optional',
        required=False,
    )

    img = discord.ui.TextInput(
        label='Embed Image',
        placeholder='Embed image here optional',
        required=False,
    )

    footer = discord.ui.TextInput(
        label='Embed footer',
        placeholder='Embed footer here optional',
        required=False,
    )

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title=self.tit.value, description=self.description.value,color=0x00FFE4)
        if not self.thumbnail.value is None:
          embed.set_thumbnail(url=self.thumbnail.value)
        if not self.img.value is None:
          embed.set_image(url=self.img.value)
        if not self.footer.value is None:
          embed.set_footer(text=self.footer.value)
        await interaction.response.send_message(embed=embed)

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)


        traceback.print_tb(error.__traceback__)


      
@tree.command(name="embed", description="Create A Embed Using Astroz")
async def _embed(interaction: discord.Interaction) -> None:
  await interaction.response.send_modal(Embed())



########################################



async def protect_vanity(guildid):
      start = time.perf_counter()
      with open('vanity.json') as idk:
        code = json.load(idk)
        if code[str(guildid)] != "":
          header = {"Authorization": "Bot MTAxMjYyNzA4ODIzMjE2NTM3Ng.GJf1Oc.bbThHhhDi8FaNDxQlxEYytiPuBNZl-x4tGCHFQ", "X-Audit-Log-Reason": "Astroz Security | Anti Vanity"}
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


@client.event
async def on_ready():
    print("Loaded & Online!")
    print(f"Logged in as: {client.user}")
    print(f"Connected to: {len(client.guilds)} guilds")
    print(f"Connected to: {len(client.users)} users")
    try:
        synced = await client.tree.sync()
        print(f"synced {len(synced)} commands")
    except Exception as e:
        print (e)




@client.command(aliases=['setup_friends','setup_friend'])
async def setupfriendlodaaaajsnjsjsj(ctx, role:discord.Role=None):
  with open('friends.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('friends.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(f"white_check_mark Updated Friends Role To {role.name}")
       
@client.command()
async def friend(ctx, mem:discord.Member=None):
  with open("friends.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send('not found')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
     # await ctx.send('white_check_mark Added Role To The Mentioned User')
      skidgod1 = discord.Embed(title="Server Roles!", description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added `{ctx.command.name}` role to the given user",color=0xdbdbdb)         
      await ctx.reply(embed=skidgod1, mention_author=False)            
@client.command(aliases=['setup_staffs','setup_staff'])
async def setupstaffslodaaaajsnjsjsj(ctx, role:discord.Role=None):
  with open('staffs.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('staffs.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(f"white_check_mark Updated Friends Role To {role.name}")

@client.command(aliases=['staffs','official'])
async def staff(ctx, mem:discord.Member=None):
  with open("staffs.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send('not found')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
    #  await ctx.send('white_check_mark Added Role To The Mentioned User')
      skidgod = discord.Embed(title="Server Roles!", description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added `{ctx.command.name}` role to the given user",color=0xdbdbdb)         
      await ctx.reply(embed=skidgod, mention_author=False)      

@client.command(aliases=['setup_girls','setup_girl'])
async def setupgirls(ctx, role:discord.Role=None):
  with open('girls.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('girls.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(f"white_check_mark Updated Friends Role To {role.name}")

@client.command(aliases=['grl','girl'])
async def girls(ctx, mem:discord.Member=None):
  with open("girls.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send('not found')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
    #  await ctx.send('white_check_mark Added Role To The Mentioned User')
      skidgod2 = discord.Embed(title="Server Roles!", description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added `{ctx.command.name}` role to the given user",color=0xdbdbdb)         
      await ctx.reply(embed=skidgod2, mention_author=False)      

@client.command(aliases=['setup_vips','setup_vip'])
async def setupvips(ctx, role:discord.Role=None):
  with open('vips.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('vips.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(f"white_check_mark Updated Friends Role To {role.name}")

@client.command(aliases=['vvip','vip'])
async def vips(ctx, mem:discord.Member=None):
  with open("vips.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send('not found')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
    #  await ctx.send('white_check_mark Added Role To The Mentioned User')
      skidgod3 = discord.Embed(title="Server Roles!", description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added `{ctx.command.name}` role to the given user",color=0xdbdbdb)         
      await ctx.reply(embed=skidgod3, mention_author=False)    
      
@client.command(aliases=['setup_specials','setup_special'])
async def setupspecials(ctx, role:discord.Role=None):
  with open('specials.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('specials.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(f"white_check_mark Updated Friends Role To {role.name}")


@client.command(aliases=['special'])
async def specials(ctx, mem:discord.Member=None):
  with open("specials.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send('not found')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
    #  await ctx.send('white_check_mark Added Role To The Mentioned User')
      abc = discord.Embed(title="Server Roles!", description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added `{ctx.command.name}` role to the given user",color=0xdbdbdb)         
      await ctx.reply(embed=abc, mention_author=False)      


@client.command(aliases=['setup_guests','setup_guest'])
async def setupguests(ctx, role:discord.Role=None):
  with open('guests.json', 'r', encoding='utf-8') as f:
    key = json.load(f)
  key[str(ctx.guild.id)] = [str(role.id)]
  with open('guests.json', 'w', encoding='utf-8') as f:
    json.dump(key, f, indent=4)
    await ctx.send(f"white_check_mark Updated Friends Role To {role.name}")

@client.command(aliases=['guest'])
async def guests(ctx, mem:discord.Member=None):
  with open("guests.json", 'r') as f:
    key = json.load(f)
  if f'{ctx.guild.id}' not in key:
    await ctx.send('not found')
  elif f'{ctx.guild.id}' in key:
    for idk in key[str(ctx.guild.id)]:
      r = discord.utils.get(ctx.guild.roles, id=int(idk))
      await mem.add_roles(r)
    #  await ctx.send('white_check_mark Added Role To The Mentioned User')
      skidgod4 = discord.Embed(title="Server Roles!", description=f"<:person:1053178413478838312> **Executor:** `{ctx.author.name}`\n<:Mod:1051999330745209002> **Command:** `{ctx.command.name}`\n<:rightshort:1053176997481828452> Successfully added `{ctx.command.name}` role to the given user",color=0xdbdbdb)         
      await ctx.reply(embed=skidgod4, mention_author=False)      


@client.event
async def on_member_join(member):
    embed = discord.Embed(title="**Sputnik's Help Panel:**", description = f"<:Notification:1053149447506374666>** General Help:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you need help setting up Sputnik or knowing everything about it, You should check out the [Official Documentation](https://discord.gg/3YmDAzbuRR)\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you want to view `Sputnik's` commands, type: `<prefix>commands`, example `s!commands`\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you need further help pls join our [Support Server](https://discord.gg/3YmDAzbuRR)\n<a:premium:1056725098641494167> **Premium Help:**\n<:1spacer:1056545806943006760><:rightshort:1053176997481828452> If you are interested in getting a more advanced Sputnik with more features, please consider checking out our [Premium Version](https://discord.gg/3YmDAzbuRR)", color=0xdbdbdb)
      
    await member.send(f"- Sent From {member.guild.name}\nhttps://discord.gg/psychics",embed = embed , mention_author = True)


#os.system("pip install flask")
from flask import Flask
from threading import Thread

app = Flask(__name__) 
@app.route('/')
def home():
    return "Sputnik"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():  
  server=Thread(target=run)
  server.start()
keep_alive()




async def main():
    async with client:
      os.system("clear")
      await client.load_extension("cogs")
      await client.load_extension("jishaku")
      await client.start("MTA1MDc4NzUzMDk0Mjk5MjQ4NA.GuYyd2.4szUkpNN_umNxfkY0afIHP2mOi1-Qu57pJTVKI")

if __name__ == "__main__":
  asyncio.run(main())
