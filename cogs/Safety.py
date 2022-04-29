from discord.ext import commands
from discord.ext.commands import Context
from utils import api

class Safety(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot: commands.Bot = bot

    @commands.command()
    async def safety(self, ctx: Context) -> None:
        everyone = api.get_everyone_role(ctx.guild)
        mentionable = api.is_everyone_mentionable(everyone)
        
        embed = api.safety_embed_message(
            {
                "everyone_mentionable": mentionable,
            }
        )

        await ctx.send(embed=embed)

def setup(bot: commands.Bot) -> None:
    bot.add_cog(Safety(bot))
