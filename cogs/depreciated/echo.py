import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&')

class EchoCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='echo')

    async def echo(self, ctx, chan: discord.TextChannel, *tuplemessage):
        echomessage =  ' '.join(tuplemessage)
        if ctx.author.id == 252597184761954304:
            await chan.send(echomessage)
def setup(bot):
    bot.add_cog(EchoCog(bot))
