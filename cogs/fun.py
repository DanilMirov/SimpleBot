import discord
from discord.ext import commands
from urllib.request import Request, urlopen
import random, json
import config

color = config.color
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept_Encoding': 'gzip, deflate',
           'Accept_Language': 'ru-RU,en-US;q=0.8',
           'Connection': 'keep-alive',
           'Referer': 'https://www.google.ru/',
           'X_Requested_With': 'simple.bot'}

class Fun:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cat', description='Рандомный кот')
    async def _cat(self):
        url = urlopen('https://random.cat/meow')
        cat = json.loads(url.read().decode())
        cat = cat['file']
        embed = discord.Embed(title="Рандомный кот", color=color)
        embed.set_footer(text=cat)
        embed.set_image(url=cat)
        await self.bot.say(embed=embed)
    @commands.command(name='dog', description='Рандомная собака')
    async def _dog(self):
        dog = "https://random.dog/{0}"
        dog_api = Request('https://random.dog/woof', headers=headers)
        idphoto = urlopen(dog_api).read().decode("utf-8")
        dog = dog.format(idphoto)
        embed = discord.Embed(title="Рандомный собакен", color=color)
        embed.set_footer(text=dog)
        embed.set_image(url=dog)
        await self.bot.say(embed=embed)
    @commands.command(name='birb', aliases=['bird'], description='Рандомная птичка :3')
    async def _birb(self):
        birb = "https://random.birb.pw/img/{0}"
        birb_api = Request("http://random.birb.pw/tweet/", headers=headers)
        idphoto = urlopen(birb_api).read().decode("utf-8")
        birb = birb.format(idphoto)
        embed = discord.Embed(title="Рандомная птичка :3", color=color)
        embed.set_footer(text=birb)
        embed.set_image(url=birb)
        await self.bot.say(embed=embed)
    @commands.command(description="Рандомное число")
    async def random(self, nb1=None, nb2=None):
        if nb1 is None: nb1 = 0
        if nb2 is None: nb2 = 10
        await self.bot.say(random.randint(int(nb1), int(nb2)))

def setup(bot):
    bot.add_cog(Fun(bot))
