from discord import Embed
from discord.ext import commands
from discord.ext.commands import Context

class Status(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def serverCount(self, ctx: Context):
        servers = self.bot.guilds
        string = '\n'.join(f'{guild.name} ({guild.id}) / {guild.member_count}' for guild in servers)
        totalMemberCount = sum(guild.member_count for guild in servers)
        totalMemberCountNoRepeat = []
        for guild in servers:
            for member in guild.members:
                totalMemberCountNoRepeat.append(member.id)
        totalMemberCountNoRepeat = len(set(totalMemberCountNoRepeat))
        fields = [['\u200b', '\u200b', True],
                 ['Total Server Count', len(self.bot.guilds), True], 
                 ['\u200b', '\u200b', True],
                 ['Total Member Count with Repeat', totalMemberCount, True], 
                 ['Total Member Count with No Repeat', totalMemberCountNoRepeat, True]]

        embed = Embed(title=ctx.author, description=f'```{string}```', color=0x2F3136)
        for i in fields:
            embed.add_field(name=i[0], value=i[1], inline=i[2])
        
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Status(bot))