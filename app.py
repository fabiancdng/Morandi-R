import discord
import config
import time
from utils import database
import os
from discord.ext import commands

async def get_server_prefix(bot, message):
    if message.guild:
        prefix = database.get_config(message.guild.id)["prefix"]
        return prefix
    else:
        return "."


bot = commands.Bot(command_prefix=get_server_prefix)

@bot.event
async def on_ready():
    database.setup_database()
    print(">>> Bot is now running.")

@bot.event
async def on_command(ctx):
    tm = time.strftime("%d/%m/%Y - %H:%M:%S")
    print(f">> [{tm}] Command '{ctx.command.name}' executed by {ctx.author.name} in guild '{ctx.guild}' ({ctx.guild.id}).")

for file in os.listdir("./modules"):
    if file.endswith(".py"):
        print(f"'{file}' has been loaded successfully.")
        bot.load_extension(f"modules.{file[:-3]}")

bot.run(config.token)