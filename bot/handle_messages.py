import random
import os
real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)
token_path = f"{dir_path}/../simple_server/api/tokens.txt"

async def handle_message(m):
    if m.channel.name == "invite_links":
        if m.content == "!cil":
            token = ''.join([ str(random.randint(0,9)) for _ in range(32)])
            await m.channel.send(f"https://mc.twelventi.com/?it={token}")
            with open(token_path, 'a') as f:
                f.write(f"{token}\n")