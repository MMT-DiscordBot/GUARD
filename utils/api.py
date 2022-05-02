from typing import List

import discord
from discord.commands import slash_command

TESTING_SERVER = [873588604922908763]

DEV = 0
PRODUCTION = 1

def command(mode):
    return [ 
        slash_command(guild_ids=TESTING_SERVER),
        slash_command(),
    ][mode]

def get_everyone_role(guild: discord.Guild) -> discord.Role:
    return guild.roles[0]

def is_everyone_mentionable(role: discord.Role) -> bool:
    return role.permissions.mention_everyone

def safety_embed_field(info: dict) -> List[Field]:
    return everyone_mentionable_field(info['everyone_mentionable']) + link_info(info['link']

def safety_embed_message(info: dict) -> discord.Embed:
    embed = discord.Embed(title='安全檢測', description='檢測有可能危害伺服器的問題')

    for field in safety_embed_field(info):
        embed.add_field(
            name='**everyone**可以**@everyone**',
            value='`解決方法`: 將**everyone**的**@everyone**權限關掉', 
            inline=False,
        )
    return embed


