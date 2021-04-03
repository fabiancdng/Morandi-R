import discord
import random
import time
from app import get_server_prefix
from utils import database
from discord.ext import commands

async def add_xp(guild_id, user_id):
    return database.add_user_xp(guild_id, user_id, random.randint(10, 20))

async def adjust_level(guild_id, user_id, user_xp, message_channel):
    level_old = database.get_user_level(guild_id, user_id)
    level_new = int(user_xp ** (1/4))

    if level_old < level_new:
        database.user_level_up(guild_id, user_id)
        emb = discord.Embed(color=discord.Color.blue(), title="Level up! 🏆", description=f"Congrats, <@{user_id}>!!\nYou just advanced to level {level_new}.")
        await message_channel.send(embed=emb)
        print(f"> [{database.get_date_time()}] Leveling: User {user_id} in guild {guild_id} just advanced to level {level_new}.")
        return True
    else:
        return False

class Levling(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot == True:
            return
        
        if message.guild is None:
            return
        
        prefix = get_server_prefix(self.bot, message)
        if message.content.startswith(prefix):
            return
        
        upated_xp = await add_xp(message.guild.id, message.author.id)
        await adjust_level(message.guild.id, message.author.id, upated_xp, message.channel)

    @commands.command()
    async def rank(self, ctx):
        user_xp = database.get_user_xp(ctx.guild.id, ctx.author.id)["xp"]
        user_level = user_xp ** (1/4)
        user_progress = int(str(user_level)[2:4])
        
        bar_len = 20
        filled_len = int(round(bar_len * user_progress / float(100)))
        bar = '🟦' * filled_len + '⬜' * (bar_len - filled_len)
        
        user_progress_left = 1 - (user_progress / 100)
        xp_left = user_xp / (user_level + 1) - user_progress_left
        xp_left = round(xp_left * user_progress_left)

        await ctx.send(embed=discord.Embed(color=discord.Color.gold())
        .add_field(
            name="Name",
            value=ctx.author.display_name,
            inline=True
        )
        .add_field(
            name="Level",
            value=round(user_level),
            inline=True
        )
        .add_field(
            name="XP (total)",
            value=user_xp,
            inline=True
        )
        .add_field(
            name="Progress",
            value=f"{bar} {user_progress}%\n\nApproximately **{xp_left} XP** to next level.",
            inline=False
        ))


    
def setup(bot):
    bot.add_cog(Levling(bot))