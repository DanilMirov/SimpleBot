import discord
from discord.ext import commands
import config

class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print('Ready!')
        await self.bot.change_presence(game=discord.Game(name=config.game), status=config.status)

def setup(bot):
    bot.add_cog(Events(bot))
