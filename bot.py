#imp---
import logging
import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
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


@client.command()
async def butt(ctx):
    button = Button(label="Portions", style=nextcord.ButtonStyle.blurple)
    async def button_callback(interaction):
        await interaction.response.edit_message(content="Physics: Ray Optics, Wave Optics\nChemistry: Amines, Aldehydes, Electrochemistry\nEnglish:\nComputer: Data Structures, Computer Networks, SQL with Python\nMaths: Integrals, Probability ")
    button.callback = button_callback
    view = View()
    view.add_item(button)
    await ctx.send("Slave reporting for duty!", view=view)
    

@client.event
async def on_ready():
    logging.info("Bot online")

    
client.run(os.getenv("DISCORD_TOKEN"))
