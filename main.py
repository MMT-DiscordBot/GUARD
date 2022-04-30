import os
import json

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='g.', intents=discord.Intents.all())

# @bot.event
# async def on_message(msg: discord.Message) -> None:
#     print(msg)
#     await bot.process_commands(msg)

@bot.event
async def on_ready() -> None:
    print('-- Bot ready --')
    filename = slice(5, -3)
    for path in glob.glob('cogs/*.py'):
        bot.load_extension('cogs.' + path[filename])

if __name__ == '__main__':
    with open('conf.json', mode='r') as f:
        conf = json.loads(f.read())
    bot.run(conf['token'])
    # bot.run('')
