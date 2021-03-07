import os
import time
import discord
from discord.ext import commands, tasks, ipc
import config
from utils import database


async def get_server_prefix(bot, message):
    if message.guild:
        prefix = database.get_config(message.guild.id)["prefix"]
        return prefix
    else:
        return "."

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.ipc = ipc.Server(self, secret_key = config.ipc_key)

    async def on_ipc_ready(self):
        print(">>> IPC server ready.")

    async def on_ipc_error(self, endpoint, error):
        print(endpoint, "raised", error)

bot = Bot(command_prefix=get_server_prefix)

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

bot.ipc.start()
bot.run(config.token)