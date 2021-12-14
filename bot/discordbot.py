import discord
import re
import os
from handle_messages import handle_message
from discord.ext import commands
from handle_minecraft import minecraft_log_handler
import requests

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)

TOKEN=""
MINECRAFT_LOG_PATH = "/home/dab/twelventicraft-server/logs/latest.log"
WEBHOOK_URL=""
channel_id = 910710276360405025

#init secret
with open(f'{dir_path}/../secrets.txt', 'r') as f:
    lines=f.readlines();
    for line in lines:
        key, value = line.split('=')
        if key=="TWELVENTICRAFT_TOKEN":
            TOKEN=value
        if key=="GAME_JOIN_WEBHOOK":
            WEBHOOK_URL=value

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
    if m.channel.name == "game-join":
        channel = client.get_channel(channel_id)
        invite = channel.create_invite()
        os.system(
            f"""minecraft tellraw {m.content} {{\"text\":\"Join our discord! {(await invite).url}\"}}"""
        )
    return await handle_message(m)

print(TOKEN)


mclh = minecraft_log_handler(MINECRAFT_LOG_PATH, client)

if __name__ == "__main__":
    mclh.run()
    # Run the bot
    client.run(TOKEN)
