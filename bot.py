#imp---
import logging
import nextcord
from nextcord.ext import commands
from nextcord.ui import Button, View
import os
from dotenv import load_dotenv
#---

load_dotenv() # env var for token

logging.basicConfig(filename="discord.log", level=logging.INFO, format="%(asctime)s: %(levelname)s - %(message)s", filemode="w")  # log file

#discrd---
client = commands.Bot(command_prefix="$")

@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(f"Numerical latency: {latency} ms")

@client.command()
async def menu(ctx):

    #mainMenu---    
    nm_btn = Button(label="NMCS", style=nextcord.ButtonStyle.danger)
    async def btn_cb(interaction):
        #btns---
        btn1 = Button(label="Portions", style=nextcord.ButtonStyle.blurple)
        async def btn1_cb(interaction):
            await interaction.response.edit_message(content="Physics: Ray Optics, Wave Optics\nChemistry: Amines, Aldehydes, Electrochemistry\nEnglish:\nComputer: Data Structures, Computer Networks, SQL with Python\nMaths: Integrals, Probability ")
        btn2 = Button(label="Midterm Timetable", style=nextcord.ButtonStyle.blurple)
        async def btn2_cb(interaction):
            await interaction.response.edit_message(content="14th - Chemistry\n15th - English\n16th - Math\n17th - Computer\n18th - Physics")

        btn1.callback = btn1_cb
        btn2.callback = btn2_cb

        view_nm = View()
        view_nm.add_item(btn1)
        view_nm.add_item(btn2)
        #---

        await interaction.response.edit_message(content="Nirmala Matha Central Shit", view=view_nm)

    music_btn = Button(label="Music", style=nextcord.ButtonStyle.green)
    async def m_btn_cb(interaction):
        await interaction.response.edit_message(content="HMMMM")
    
    nm_btn.callback = btn_cb
    music_btn.callback = m_btn_cb

    view = View()
    view.add_item(nm_btn)
    view.add_item(music_btn)
    #---

    await ctx.send("Slave reporting for duty!", view=view)

@client.event
async def on_ready():
    logging.info("BOT ONLINE")


client.run(os.getenv("DISCORD_TOKEN"))
#---
