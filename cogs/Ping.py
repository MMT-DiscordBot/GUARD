from discord.ext import commands
from discord.ext.commands import Context

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def ping(self, ctx: Context) -> None:
        await ctx.send("Hi, this is a slash command from a cog!")

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Ping(bot))
