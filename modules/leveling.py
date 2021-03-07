import discord
import random
import time
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
        tm = time.strftime("%d/%m/%Y - %H:%M:%S")
        print(f"> [{tm}] Leveling: User {user_id} in guild {guild_id} just advanced to level {level_new}.")
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
        
        upated_xp = await add_xp(message.guild.id, message.author.id)
        await adjust_level(message.guild.id, message.author.id, upated_xp, message.channel)

    
def setup(bot):
    bot.add_cog(Levling(bot))