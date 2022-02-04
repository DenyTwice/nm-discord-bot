import logging
import discord
from discord.ext import commands
import Music

cogs = [music]

client = commands.Bot(command_prefix = '?', intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTM4NzI2NzA1NDI0NjQ2MjA0.YfufXw.KJtG08ZgjTdbH2CkhlYpr-PgNSo")

