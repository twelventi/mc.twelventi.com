import tailer
import asyncio
import re
import requests
import os
from threading import Thread


real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)


channel_id = 910710276360405025
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
        if key=="GAME_JOIN_WEBOOK":
            WEBHOOK_URL=value

class minecraft_log_handler:
    def __init__(self, logfile, client):
        self.logfile = logfile
        self.client = client

    def run(self):
        t = Thread(target= lambda: asyncio.run(self._follower(self.logfile)))
        t.start()

    async def _follower(self, logfile):
        for line in tailer.follow(open(logfile)):
            print(line)
            await self._message_parser(line)

    async def create_and_send_invite_token(self, mc_user):
        requests.post(WEBHOOK_URL, data={"message": mc_user})

    async def _message_parser(self, message):
        match = re.search("INFO]: (.*) joined the game", message)
        print(match, message)
        if match:
            await self.create_and_send_invite_token(str(match[1]))


if __name__ == "__main__":
    mlh = minecraft_log_handler("./test.log", None)
    mlh.run()
