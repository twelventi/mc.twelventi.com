import tailer
import asyncio
import re
import os
from threading import Thread

class minecraft_log_handler:
    def __init__(self, logfile, client):
        self.logfile = logfile
        self.client = client
    
    def run(self):
        t = Thread(target = lambda : asyncio.run(self._follower(self.logfile)))
        t.start()

    async def _follower(self, logfile):
        for line in tailer.follow(open(logfile)):
            self._message_parser(line)
            print(line)

    async def create_and_send_invite_token(self, mc_user):
        channel = await client.get_channel(channel_id)
        invite = await channel.create_invite()
        os.system(f'''minecraft tellraw {user} {{"text":"Join our discord! {invite.url}"}}''')

    async def _message_parser(self, message):
        try:
            user = re.search("INFO]: (.*) joined the game", message)[1]
            await self.create_and_send_invite_token(message)
        except e:
            pass

if __name__ == "__main__":
    mlh = minecraft_log_handler("./test.log", None)
    mlh.run()