from discord.ext import commands
from utils import api

class Safety(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def safety(self, ctx):
        everyone = api.get_everyone_role(ctx.guild)
        mentionable = api.is_everyone_mentionable(everyone)
        
        embed = api.safety_embed_message(
            {
                "everyone_mentionable": mentionable,
            }
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Safety(bot))
