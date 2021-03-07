from discord.ext import commands, ipc

class IpcRoutes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @ipc.server.route()
    async def get_member_count(self, data):
        guild = self.bot.get_guild(
            data.guild_id
        )

        return guild.member_count


def setup(bot):
    bot.add_cog(IpcRoutes(bot))