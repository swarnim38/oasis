from discord.ext.commands import Cog


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.cogs_ready:
            self.bot.cogs_ready.ready_up("test")
        #await self.bot.general.send("Fun cog is ready")
        print("Test cog is ready")


def setup(bot):
    bot.add_cog(Fun(bot))
