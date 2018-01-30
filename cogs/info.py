import discord
from discord.ext import commands
import config

color = config.color

class Info:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='About bot')
    async def about(self):
        await self.bot.say(embed=discord.Embed(description='Разработчик: 321268938728144906, Исходники: https://github.com/DanilMirov/SimpleBot/', color=color))
    @commands.command(pass_context=True, description='Info', aliases=['serverinfo', 'sinfo'])
    async def server(self, ctx):
        server = ctx.message.server
        online = str(sum(1 for member in server.members if member.status == discord.Status.online or member.status == discord.Status.idle))
        msg = ''
        msg += "ID Сервера: `{0}`\n".format(server.id)
        msg += "Юзеров: {0} онлайн/{1} всего\n".format(online, len(server.members))
        msg += "Сервер создан в: `{0}`\n".format(str(server.created_at.strftime('%m/%d/%Y %H:%M:%S')))
        msg += "Создатель: `{0}`\n".format(server.owner)
        voice = 0
        text = 0
        for channel in server.channels:
            if channel.type == discord.ChannelType.text:
                text += 1
            if channel.type == discord.ChannelType.voice:
                voice += 1
        msg += "Каналов: `{0}` Текстовых | `{1}` Голосовых | **{2}** Всего\n".format(text, voice, str(len(server.channels)))
        msg += "Всего ролей: `{0}`\n".format(str(len(server.roles)))
        embed = discord.Embed(description=msg, color=color)
        await self.bot.say(embed=embed)
    @commands.command(pass_context=True, description='Avatar', aliases=['a'])
    async def avatar(self, ctx, user: discord.User=None):
        if user is None:
            try: user = ctx.message.mentions[0]
            except: user = ctx.message.author
        avt = user.avatar_url
        embed = discord.Embed(url=avt, color=color)
        embed.set_author(name=user.name)
        embed.set_author(name=user.name, icon_url=avt)
        embed.set_image(url=avt)
        await self.bot.say(embed=embed)
    @commands.command(pass_context=True, description='Роли на сервере')
    async def roles(self, ctx):
        msg = 'Сдесь есть такие роли:\n'
        for role in ctx.message.server.roles:
            msg += '`{0}` '.format(role.name)
        await self.bot.say(embed=discord.Embed(description=msg, color=color))

def setup(bot):
    bot.add_cog(Info(bot))
