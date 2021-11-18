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
    random_token = None
    for token_channel in client.get_all_channels():
        if token_channel.name=='invite-tokens':
            break
    if m.content == '!create_invite_link':
        permissions = m.channel.permissions_for(m.author)
        if permissions.administrator:
            random_token= ''.join([str(random.randint(0,9)) for _ in range(32)])
            await m.channel.send(f"https://mc.twelventi.com/?it={random_token}")
            await token_channel.send(random_token)
        return
    if m.channel.name=='whitelist':
        tokens = [msg.content for msg in await token_channel.history(limit=100).flatten()]
        name = ""; auth=False
        print(m.content)
        for line in m.content.split('\n'):
            key, value = line.split(':')
            if key == "name":
                name = value
            if key == "code":
                if value in tokens:
                    auth=True
        if not auth:
            await m.delete()
            return

        with open('whitelist.txt', 'a') as f:
            f.write(f'{name}\n');


print(TOKEN)
# Run the bot
client.run(TOKEN)