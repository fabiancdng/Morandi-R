import discord
from utils import database
from discord.ext import commands

class Messages(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)
    
def setup(bot):
    bot.add_cog(Messages(bot))