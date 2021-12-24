import discord
from discord.ext import commands
from key import TOKEN
import time
import sys
import os

ownerID = 252597184761954304

class RestartCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="restart")
    async def restart(self, ctx, timer = None):
        if ctx.author.id == ownerID and type(timer) == str and timer.isnumeric():
            x = int(timer)
            if x <= 10:
                await ctx.send('Restarting the bot in ' + timer + ' second(s).')
                time.sleep(x)
                await self.bot.close()
                time.sleep(1)
                exec(open("main.py").read())
        else:
            await ctx.send('Restarting the bot.')
            await self.bot.close()
            time.sleep(1)
            exec(open("main.py").read())

def setup(bot):
    bot.add_cog(RestartCog(bot))

