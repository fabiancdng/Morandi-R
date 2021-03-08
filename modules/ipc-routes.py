from discord.ext import commands, ipc

class IpcRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ipc.server.route()
    async def get_mutual_guilds(self, data):
        guild_ids = []
        for guild in self.bot.guilds:
            guild_ids.append(guild.id)
        return guild_ids


def setup(bot):
    bot.add_cog(IpcRoutes(bot))