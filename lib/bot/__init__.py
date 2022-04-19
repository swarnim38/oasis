from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase

PREFIX = "o!"
OWNER_IDS = [556801303595188227]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.SCHEDULER = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Creating an Oasis...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Oasis connected")

    async def on_disconnect(self):
        print("Oasis disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(928595300828987442)
            print("Oasis is ready")

        else:
            print("Oasis recontructing...")

    async def on_message(self, message):
        pass


bot = Bot()