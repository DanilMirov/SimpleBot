from discord.ext import commands
class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('Ready!')

def setup(bot):
    bot.add_cog(Events(bot))
