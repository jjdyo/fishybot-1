import discord
from discord.ext import commands
import time

async def is_owner(ctx):
    return ctx.author.id == 252597184761954304

class Admin(commands.Cog):
    """
    Maintnence and other technicals
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="shutdown", description="Shutdown the bot.")
    @commands.check(is_owner)
    async def shutdown(self, ctx, timer = None):
        """Shutdown the bot."""
        if type(timer) == str and timer.isnumeric():
            x = int(timer)
            if x <= 10:
                await ctx.send('Closing the bot in ' + timer + ' second(s).')
                time.sleep(x)
                await self.bot.close()
        else:
            await ctx.send('Closing the bot.')
            await self.bot.close()
    @shutdown.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("<:abby_irl:676523172480417795>")


    @commands.command(name='echo', description="Causes an echo of input at channel ID")
    @commands.check(is_owner)
    async def echo(self, ctx, chan: discord.TextChannel, *tuplemessage):
        """Make Fishy echo"""
        echomessage =  ' '.join(tuplemessage)
        formattedecho1 = echomessage.replace("'", "\'")
        formattedecho2 = formattedecho1.replace('"', '\"')
        if ctx.author.id == 252597184761954304:
            await chan.send(formattedecho2)
            print(formattedecho2)
    @echo.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("<:abby_irl:676523172480417795>")

    @commands.command()
    @commands.check(is_owner)
    async def load(self, ctx, *, module):
        """Loads a module."""
        try:
            self.bot.load_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send('✅')
    @load.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("<:abby_irl:676523172480417795>")

    @commands.command()
    @commands.check(is_owner)
    async def unload(self, ctx, *, module):
        """Unloads a module."""
        try:
            self.bot.unload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send('✅')
    @unload.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("<:abby_irl:676523172480417795>")

    @commands.group(name='reload')
    @commands.check(is_owner)
    async def _reload(self, ctx, *, module):
        """Reloads a module."""
        try:
            self.bot.reload_extension(module)
        except commands.ExtensionError as e:
            await ctx.send(f'{e.__class__.__name__}: {e}')
        else:
            await ctx.send('✅')
    @_reload.error
    async def command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("<:abby_irl:676523172480417795>")



        

def setup(bot):
    bot.add_cog(Admin(bot))
