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
    for filename in os.listdir('./cogs'):
        if filename[-3:] == '.py':
            bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    with open('conf.json', mode='r') as f:
        conf = json.loads(f.read())
    bot.run(conf['token'])
    # bot.run('')
