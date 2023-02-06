import os 
os.system("pip install wavelink")
import discord, wavelink, asyncio
from discord.ext import commands
import datetime as dt
OPTIONS = {
    "1️⃣": 0,
    "2⃣": 1,
    "3⃣": 2,
    "4⃣": 3,
    "5⃣": 4,
}

class Music(commands.Cog):
    emoji = "🥀"
    def __init__(self, client: commands.Bot):
        self.client = client
        self.client.loop.create_task(self.connect_nodes())
    
    async def connect_nodes(self):
        await self.client.wait_until_ready()
        try:
          await wavelink.NodePool.create_node(
            bot=self.client,
         host="ssl.freelavalink.ga",
            port=443,
            password="www.freelavalink.ga",
            https=True
        )
        except Exception as e:
          print(e)
    
    async def choose_one(self, ctx, tracks):
        def _check(r, u):
            return (
                r.emoji in OPTIONS.keys()
                and u == ctx.author
                and r.message.id == msg.id
            )

        embed = discord.Embed(
            title="Choose a song",
            description=(
                "\n".join(f"**`[{i+1}]` | {t.title}**" for i, t in enumerate(tracks[:5]))
            ),
            color=0x00FFE4
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
        msg = await ctx.send(embed=embed)
        for emoji in list(OPTIONS.keys())[:min(len(tracks), len(OPTIONS))]:
            await msg.add_reaction(emoji)
        
        try: 
            reaction, _ = await self.client.wait_for('reaction_add', timeout=60.0, check=_check)
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.message.delete()
        else:
            await msg.delete()
            return tracks[OPTIONS[reaction.emoji]]
    
    @commands.hybrid_command(name="connect",help="connect to your channel .", aliases=["join","jvc"], usage="connect [channel]")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def connect(self, ctx: commands.Context, *, channel: discord.VoiceChannel=None):
        """Connects to a voice channel."""
        if not getattr(ctx.author, "voice", None):
            nv = discord.Embed(description=f'<:error:1018174714750976030> | You are not connected to a voice channel.', color=0x00FFE4)
            await ctx.send(embed=nv)
            return
        if channel is None:
            channel = ctx.author.voice.channel
        elif ctx.voice_client:
            av = discord.Embed(description=f"<:error:1018174714750976030> | I am already connected to a voice channel.", color=0x00FFE4)
            await ctx.send(embed=av)
            return
        vc: wavelink.Player = await channel.connect(cls=wavelink.Player)
        sc = discord.Embed(description=f"<:GreenTick:1018174649198202990> | Successfully connected to `{channel.name}`.", color=0x00FFE4)
        await ctx.send(embed=sc)
    
    @commands.hybrid_command(name="disconnect",help="Stops playing song and clears the queue.", aliases=['leave','dc'], usage="disconnect [channel]")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def disconnect(self, ctx: commands.Context, *, channel: discord.VoiceChannel=None):
        """Disconnects from a voice channel."""
        if not getattr(ctx.author, "voice", None):
            mnv = discord.Embed(description=f"<:error:1018174714750976030> | You are not connected to a voice channel.", color=0x00FFE4)
            await ctx.send(embed=mnv)
            return
        if channel == None:
            channel = ctx.author.voice.channel
        elif not ctx.voice_client:
            mnc = discord.Embed(description=f"<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4)
            await ctx.send(embed=mnc)
            return
        elif ctx.author.voice.channel != ctx.voice_client.channel:
            svc = discord.Embed(description=f"<:error:1018174714750976030> | You should be in the same voice channel that I'm in.", color=0x00FFE4)
            await ctx.send(embed=svc)
            return
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()
        await ctx.send(embed=discord.Embed(description=f"<:GreenTick:1018174649198202990> | Successfully disconnected from `{vc.channel.name}`", color=0x00FFE4))
    
    @commands.hybrid_command(name="play",help="Plays song in your voice channel.", aliases=['p'], usage="play <query>")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def play(self, ctx: commands.Context, *, query: str):
        """Listen to lag-free music."""
        if not getattr(ctx.author, "voice", None):
            nvc = discord.Embed(description=f"<:error:1018174714750976030> | You are not connected to a voice channel.", color=0x00FFE4)
            await ctx.send(embed=nvc)
            return
        elif not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
            svc = discord.Embed(description=f"<:GreenTick:1018174649198202990> | Successfully connected to {ctx.author.voice.channel.name}", color=0x00FFE4)
            await ctx.send(embed=svc)
        else:
            vc: wavelink.Player = ctx.voice_client
        
        tracks = await wavelink.YouTubeTrack.search(query=query)
        song = await self.choose_one(ctx, tracks)
        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(song)
            await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{song.title} [{ctx.author.mention}]", color=0x00FFE4))
        else:
            await vc.queue.put_wait(song)
            await ctx.send(embed=discord.Embed(title="Music Queue", description=f"Added {song.title} to the queue.", color=0x00FFE4))
        vc.ctx = ctx
        setattr(vc, "loop", False)
    
    @commands.Cog.listener()
    async def on_wavelink_track_end(self, player: wavelink.Player, track: wavelink.Track, reason):
        ctx = player.ctx
        vc: player = ctx.voice_client

        if player.loop:
            await player.play(track)
            await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{track.title} [{ctx.author.mention}]", color=0x00FFE4))
        
        if not player.queue.is_empty:
            next_track = await vc.queue.get_wait()
            await vc.play(next_track)
            await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{next_track.title} [{ctx.author.mention}]", color=0x00FFE4))

    @commands.hybrid_command(name="loop",help="Switches the players loop to queue mode.", usage="loop")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loop(self, ctx: commands.Context):
        if not ctx.voice_client:
            svc = discord.Embed(description=f"<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4)
            await ctx.send(embed=svc)
            return
        elif not getattr(ctx.author, "voice", None):
            nvc = discord.Embed(description=f"<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4)
            await ctx.send(embed=nvc)
            return
        else:
            vc: wavelink.Player = ctx.voice_client
        if not vc.is_playing():
            bvc = discord.Embed(description=f"<:error:1018174714750976030> | I am not playing anything.", color=0x00FFE4)
            await ctx.send(embed=bvc)
            return
        vc.loop = True if not vc.loop else False
        mvc = discord.Embed(description=f"<:GreenTick:1018174649198202990> | Looping set to {'**true**.' if vc.loop else '**false**.'}", color=0x00FFE4)
        await ctx.send(embed=mvc)
    
    @commands.hybrid_command(name="stop", usage="stop",help="Stops playing song and clears the queue.")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stop(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description=f"<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4))
            return
        else:
            vc: wavelink.Player = ctx.voice_client
        if vc.is_playing() is False:
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | I am not playing anything.", color=0x6509f5))
            return

        await vc.stop()
        vc.queue.clear()
        await ctx.send(embed=discord.Embed(description=f"<:GreenTick:1018174649198202990> | Destroyed the player.", color=0x00FFE4))
    
    @commands.group(name="queue", usage="queue",help="Shows you the upcoming tracks of the player.")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def queue(self, ctx: commands.Context):
        if ctx.invoked_subcommand is None:
            if not ctx.voice_client:
                await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | There is nothing playing yet.", color=0x00FFE4))
            elif not getattr(ctx.author.voice, "channel", None):
                await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4))
            else:
                vc: wavelink.Player = ctx.voice_client
            
            if vc.queue.is_empty:
                return await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | There are no more tracks in the queue.", color=0x00FFE4))
            
            embed = discord.Embed(title="Music Queue", color=0x00FFE4)
            queue = vc.queue.copy()
            description = ""
            for num, track in enumerate(queue):
                description += f"`[{num + 1}]` | " + f"{track.title}" + "\n"
            embed.description = description
            await ctx.send(embed=embed)

    @queue.command(name="clear", usage="queue clear",help="Clears the queue.")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        vc.queue.clear()
        await ctx.send(embed=discord.Embed(description="Cleared the queue.", color=0x00FFE4))
    
    @commands.hybrid_command(name="pause", usage="pause",help="Pauses the player.")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pause(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            return await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | There is nothing playing yet.", color=0x00FFE4))
        await vc.pause()
        await ctx.send(embed=discord.Embed(description="Paused the player.", color=0x00FFE4))
    
    @commands.hybrid_command(name="resume", usage="resume",help="Resumes a currently paused song.")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def resume(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            return await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | There is nothing playing yet.", color=0x00FFE4))
        await vc.resume()
        await ctx.send(embed=discord.Embed(description="<:GreenTick:1018174649198202990> | Resumed the player.", color=0x00FFE4))
     
    @commands.hybrid_command(name="skip", usage="skip",help="Skips the currently playing song.")
    @commands.is_owner()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skip(self, ctx: commands.Context):
        if not ctx.voice_client:
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | I am not connected to a voice channel.", color=0x00FFE4))
            return
        elif not getattr(ctx.author, "voice", None):
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | You are not connected to a voice channel to do this.", color=0x00FFE4))
            return
        else:
            vc: wavelink.Player = ctx.voice_client

        if not vc.is_playing():
            await ctx.send(embed=discord.Embed(description="<:error:1018174714750976030> | There is nothing playing yet.", color=0x00FFE4))
            return
        track = await vc.queue.get_wait()
        await vc.play(track)
        await ctx.send(embed=discord.Embed(description="<:GreenTick:1018174649198202990> | Skiped the track.", color=0x00FFE4))
        await ctx.send(embed=discord.Embed(title="Now Playing", description=f"{track.title} [{ctx.author.mention}]", color=0x00FFE4))








