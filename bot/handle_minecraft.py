import tailer
import asyncio
import re
import os
from threading import Thread

channel_id = "910710276360405025"

class minecraft_log_handler:
    def __init__(self, logfile, client):
        self.logfile = logfile
        self.client = client
        print(client.get_channel(channel_id))
    
    def run(self):
        t = Thread(target = lambda : asyncio.run(self._follower(self.logfile)))
        t.start()

    async def _follower(self, logfile):
        for line in tailer.follow(open(logfile)):
            print(line)
            await self._message_parser(line)

    async def create_and_send_invite_token(self, mc_user):
        channel = await self.client.get_channel(channel_id)
        invite = await channel.create_invite()
        os.system(f'''minecraft tellraw {user} {{"text":"Join our discord! {invite.url}"}}''')
        return ""

    async def _message_parser(self, message):
        match = re.search("INFO]: (.*) joined the game", message)
        print(match, message)
        if match:
            await self.create_and_send_invite_token(str(match[1]))
        

if __name__ == "__main__":
    mlh = minecraft_log_handler("./test.log", None)
    mlh.run()