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

def get_everyone_role(guild):
    return guild.roles[0]

def is_everyone_mentionable(role):
    return role.permissions.mention_everyone




def safety_embed_message(info):
    embed = discord.Embed(title='安全檢測', description='檢測有可能危害伺服器的問題')

    if info['everyone_mentionable']:
        embed.add_field(
            name='**everyone**可以**@everyone**',
            value='`解決方法`: 將**everyone**的**@everyone**權限關掉', 
            inline=False,
        )
    return embed


