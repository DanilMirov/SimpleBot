import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import random

def color(ctx):
    color = '6553855'
    if ctx.message.server is not None:
        color = ctx.message.server.me.color

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Рандомный кот')
    async def cat(self, ctx):
        cat = urlopen('https://random.cat/meow')
        cat = str(cat.read())
        cat = cat[11:]
        cat = cat[:len(cat) - 3]
        cat = cat.replace("\\", "")
        embed = discord.Embed(title="Рандомный кот", color=color(ctx))
        embed.set_footer(text="{}".format(str(cat)))
        embed.set_image(url=str(cat))
        await self.bot.say(embed=embed)
    @commands.command(pass_context=True, description='Рандомная собака')
    async def dog(self, ctx):
        dog = urlopen('https://random.dog/woof')
        dog = str(dog.read())
        dog = dog[2:]
        dog = dog[:len(dog) - 1]
        embed = discord.Embed(title="Рандомный собакен", color=color(ctx))
        embed.set_footer(text="{}".format("http://random.dog/" + str(dog)))
        embed.set_image(url="http://random.dog/" + str(dog))
        await self.bot.say(embed=embed)
    @commands.command(description="Рандомное число")
    async def random(self, nb1=None, nb2=None):
        if nb1 is None: nb1 = 0
        if nb2 is None: nb2 = 10
        await self.bot.say(random.randint(int(nb1), int(nb2)))

def setup(bot):
    bot.add_cog(Fun(bot))
