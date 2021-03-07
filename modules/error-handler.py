"""
If you are not using this inside a cog, add the event decorator e.g:
@bot.event
async def on_command_error(ctx, error)
For examples of cogs see:
https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be
For a list of exceptions:
https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#exceptions
"""
import discord
import traceback
import sys
from discord.ext import commands


class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NoPrivateMessage):
            await ctx.send(embed=discord.Embed(
                color=discord.Color.red(),
                description="❌ This command is only supported on servers."
            ))
        else:
            await ctx.send(embed=discord.Embed(
                title="An error occured during the command execution:",
                color=discord.Color.red(),
                description=f"```{error}```"
            ))

def setup(bot):
    bot.add_cog(ErrorHandler(bot))