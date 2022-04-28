import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='mb.', intents=discord.Intents.all())

@bot.event
async def on_ready():
    for root, _, files in os.walk('./cogs'):
        for file in files:
            if (path:=os.path.join(root, file)).endswith('.py'):
                bot.load_extension(path[2:-3].replace('\\', '.'))

if __name__ == '__main__':
    bot.run('')