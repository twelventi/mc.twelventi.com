import discord
import random
import re
import os
from discord.ext import commands

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)

TOKEN=""

#init secret
with open(f'{dir_path}/../secrets.txt', 'r') as f:
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
        matches = re.findall("\[.*:(.*)\]" ,m.embeds[0].title)
        if len(matches) > 0:
            branch = matches[0]
            if branch == "main":
                os.system(f"{dir_path}/../update-server.sh")

print(TOKEN)
# Run the bot
client.run(TOKEN)
