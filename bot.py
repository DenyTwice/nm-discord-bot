#imp---
import logging
import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv
#---

load_dotenv()

logging.basicConfig(filename="discord.log", level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s")

client = commands.Bot(command_prefix="$") # custom prefix command?

@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(f"Numerical latency: {latency} ms")


@client.event
async def on_ready():
    logging.info("Bot online")


client.run(os.getenv("DISCORD_TOKEN"))
