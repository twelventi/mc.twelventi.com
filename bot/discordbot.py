import discord
import random
from discord.ext import commands

TOKEN=""

#init secret
with open('secrets.txt', 'r') as f:
    lines=f.readlines();
    for line in lines:
        key, value = line.split('=')
        if key=="TWELVENTICRAFT_TOKEN":
            TOKEN=value
            break

client = commands.Bot(command_prefix='!')

#Startup Information
@client.event
async def on_ready():
    print(f"Connected to bot: {client.user.name}")
    print(f"Bot ID: {client.user.id}")

@client.event
async def on_message(m):
    if m.channel.name == "gh-updates":
        print(m.embeds[0].description)

print(TOKEN)
# Run the bot
client.run(TOKEN)