import discord
from discord.ext import commands
import wolframalpha
import io
import aiohttp
import json
import time
import sys
client = wolframalpha.Client('WOLFRAM_API_KEY_GOES_HERE')

class Utilities(commands.Cog):
    """
    Home of most commands.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(title='wolfram',name='wolfram', description="Send a query to wolfram. Still very experimental command so hanging/errors are expected from time to time.")

    async def wolfram(self, ctx, *tuplequery):
        """&wolfram <query>\n Returns wolfram's provided query, results may vary\n (Experimental feature)"""
        singlequery =  ' '.join(tuplequery)
        res = client.query(singlequery)
        loopbreak = 0
        #if ctx.author.id == 252597184761954304: This is probably skeleton for adding a &wolframfull command. Or perhaps add secondary argument to equal something. (tuple, full)
            #loopbreak = -100
        for pod in res.pods:
            for sub in pod.subpods:
                if loopbreak == 2:
                    break
                else:
                    loopbreak += 1
                #await ctx.send(sub.plaintext)
                ##await ctx.send(sub['img'].get('@src'))
                    await ctx.send(sub['img']['@src'])
                #await ctx.send(list(sub.img))
                #for img in sub.img:
                    #await ctx.send(img['@src'])
                    
                    #async with aiohttp.ClientSession() as session:
                        #async with session.get(sub.img) as resp:
                            #if resp.status != 200:
                                #return await ctx.send('Could not download file...')
                            #data = io.BytesIO(await resp.read())
                            #await ctx.send(file=discord.File(data, ''))
    
    @commands.command(title='ping',name='ping', description="Pong!")

    async def ping(self, ctx):
        """&ping \nPing! Pong! What more is there to say?
        """
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")
        print(f'Ping {int(ping)}ms')


def setup(bot):
    bot.add_cog(Utilities(bot))


