from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Hi, this is a slash command from a cog!")

def setup(bot):
    bot.add_cog(Ping(bot))
