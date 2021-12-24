import discord
import os
import asyncio
from discord.ext import commands
from cogs import modules
from key import TOKEN
import time




bot = commands.Bot(command_prefix='&')

#client = commands.Bot(command_prefix='$')
bot.remove_command('help') #Remove default help
bot.load_extension("cogs.modules")
bot.load_extension("cogs.wolf")
bot.load_extension("cogs.helpcommand")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game('&help | Swimming in the ocean'))
    starttime = time.monotonic()

bot.run(TOKEN)

