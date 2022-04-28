from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from discord import Embed, File
from datetime import datetime
from ..db import db

PREFIX = "o!"
OWNER_IDS = [556801303595188227]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX,
            owner_ids=OWNER_IDS,
            intents=Intents.all()
        )

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

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong `0_0`")

        else:
            channel = self.get_channel(928595300828987445)
            await channel.send("Something is wrong")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(928595300828987442)
            self.scheduler.start()

            #channel = self.get_channel(928595300828987445)
            #await channel.send("Oasis is formed!")

            #embed = Embed(title="Oasis is formed!",
             #             description="The bot is up and running",
              #            color=0Xf59e4c,
               #           timestamp=datetime.utcnow())

            #embed.set_footer(text="Chrysus")
            #embed.set_author(name="Oasis", icon_url=self.guild.icon_url)

            #await channel.send(embed=embed)
            #await channel.send(file=File("./data/images/oasis_banner.png"))

            print("Oasis is ready")

        else:
            print("Oasis recontructing...")

            async def on_message(self, message):
                pass


bot = Bot()
