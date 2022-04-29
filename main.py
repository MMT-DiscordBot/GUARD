import os

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='g.', intents=discord.Intents.all())

@bot.event
async def on_message(msg):
    print(msg)
    await bot.process_commands(msg)

@bot.event
async def on_ready():
    print('-- Bot ready --')
    for root, _, files in os.walk('./cogs'):
        for file in files:
            if (path:=os.path.join(root, file)).endswith('.py'):
                bot.load_extension(path[2:-3].replace('/', '.'))

if __name__ == '__main__':
    bot.run('NjA5MjA0NzUzODUwODI2NzY0.XUzUIw.mN6r1FYrt8hg4bZrLZmtX_xMCW4')
