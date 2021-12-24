import discord
from discord.ext import commands

class CogTester(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Cog was reloaded. Good job jaxon.")

def setup(bot):
    bot.add_cog(CogTester(bot))
