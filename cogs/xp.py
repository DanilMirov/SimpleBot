import discord
from discord.ext import commands
import config

import sqlite3
data = sqlite3.connect('data.sqlite')

cur = data.cursor()
color = config.color

class XP:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author.bot: return
        cur.execute('SELECT * FROM xp WHERE id="{0}"'.format(message.author.id))
        try:
            res = cur.fetchone()[1] + len(message.content)
            cur.execute('UPDATE xp SET xp={0} WHERE id={1}'.format(res, message.author.id)); data.commit()
        except: pass
    @commands.command(pass_context=True, description='XP')
    async def xp(self, ctx):
        cur.execute('SELECT * FROM xp WHERE id="{0}"'.format(ctx.message.author.id))
        try: await self.bot.say(embed=discord.Embed(description='XP: {0}'.format(cur.fetchone()[1]), color=color))
        except:
            cur.execute('INSERT INTO xp VALUES ("{0}", 0)'.format(ctx.message.author.id)); data.commit()
            cur.execute('SELECT * FROM xp WHERE id="{0}"'.format(ctx.message.author.id))
            await self.bot.say(embed=discord.Embed(description='У вас нет XP\nXP: {0}'.format(cur.fetchone()[1]), color=color))

def setup(bot):
    bot.add_cog(XP(bot))
