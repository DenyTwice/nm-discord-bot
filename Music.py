import discord
from discord.ext import commands 
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Dude, get in a fucking VC")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_channel is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_options = {'before_options':, '-reconnect 1 -reconnect_streamed 1 -reconenct_delay_max 5', 'options': '_vn'}
        YDL_options = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_options) as ydl:
            info = ydl.extract_info(url, download = false)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_options)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Paused ||")

    @commands.command()
    async def resume(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Playing ▶")


def setup(client):
    client.add_cog(music(client))
