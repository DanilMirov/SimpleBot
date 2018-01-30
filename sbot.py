import discord
from discord.ext.commands import Bot
import os, config

description = """
Simple Bot By DanilMirov
"""

def prefix(bot, msg):
    id = bot.user.id
    px = [f'<@!{id}> ', f'<@{id}> ']
    px.append('s.'); px.append('S.')
    if msg.server is None:
        px.append('!')
        px.append('?')
    return px

bot = Bot(command_prefix=prefix, description=description)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = 'cogs.'+file[:-3]
        try:
            bot.load_extension(name)
            print(f'Loaded {name}.')
        except Exception as e:
            print(f'Failed to load extension {name}. Error:\n{e}')

bot.run(config.token)
