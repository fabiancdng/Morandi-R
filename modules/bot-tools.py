import discord
from utils import database
from discord.ext import commands

class BotTools(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print(database.change_config(ctx.guild.id, "prefix", "!"))
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)} ms.")

    
def setup(bot):
    bot.add_cog(BotTools(bot))