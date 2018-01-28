import discord
from discord.ext import commands

class Info:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='About bot')
    async def about(self):
        await self.bot.say('Разработчик: 321268938728144906, Исходники: https://github.com/DanilMirov/SimpleBot/')

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
        await self.bot.say(msg)

def setup(bot):
    bot.add_cog(Info(bot))
