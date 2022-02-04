import logging
import discord


client = discord.Client()

@client.event
async def on_ready():
    print("LOL")

client.run("OTM4NzI2NzA1NDI0NjQ2MjA0.YfufXw.KJtG08ZgjTdbH2CkhlYpr-PgNSo")