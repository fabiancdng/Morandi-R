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

    @ipc.server.route()
    async def get_display_name_by_id(self, data):
        display_name = self.bot.get_user(int(data.user_id)).display_name
        return display_name

def setup(bot):
    bot.add_cog(IpcRoutes(bot))