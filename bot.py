#imp---
import logging
import nextcord
from nextcord.ext import commands
#---

client = commands.Bot(command_prefix="$") # custom prefix command?

@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(f"Numerical latency: {latency} ms")

@client.event
async def on_ready():
    print("")

    
client.run("OTM4NzI2NzA1NDI0NjQ2MjA0.YfufXw.KJtG08ZgjTdbH2CkhlYpr-PgNSo")

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s-%(message)s")
