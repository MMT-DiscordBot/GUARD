import os
import json

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
    with open('conf.json', mode='r') as f:
        conf = json.loads(f.read())
    bot.run(conf['token'])
