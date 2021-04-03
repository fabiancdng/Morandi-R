import discord
import requests
from discord.ext import commands

class Covid(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def covid(self, ctx, country="US"):
        endpoint = "https://api.covid19api.com/summary"

        response = requests.request("GET", url=endpoint).json()["Countries"]

        for data in response:
            if data["Country"] == country or data["CountryCode"] == country:
                embed = discord.Embed(
                    color=discord.Color.orange(),
                    title=f"Current Covid-19 data for **{data['Country']}**"
                ).add_field(
                    name="Disclamer",
                    value="We are not responsible for the data below nor do we provide any kind of warranty or liability for it. The data's origin is [covid19api](https://covid19api.com/). It is used by a lot of projects and according to their own statements, the data they serve is from [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19). Please do your own research and don't rely on the data in this message.",
                    inline=False
                ).add_field(
                    name="\u200B",
                    value="\u200B",
                    inline=False
                ).add_field(
                    name="New cases",
                    value=f"**_{data['NewConfirmed']}_**"
                ).add_field(
                    name="New recovered",
                    value=f"**_{data['NewRecovered']}_**"
                ).add_field(
                    name="New deaths",
                    value=f"**_{data['NewDeaths']}_**"
                ).add_field(
                    name="Total cases",
                    value=f"**_{data['TotalConfirmed']}_**"
                ).add_field(
                    name="Total recovered",
                    value=f"**_{data['TotalRecovered']}_**"
                ).add_field(
                    name="Total deaths",
                    value=f"**_{data['TotalDeaths']}_**"
                ).add_field(
                    name="\u200B",
                    value="\u200B",
                    inline=False
                ).add_field(
                    name="What does '0' mean?",
                    value="The 0 means that the data for this query isn't in yet, try again in a few hours.\n\n",
                    inline=False
                ).add_field(
                    name="Source",
                    value=f"Source: _[covid19api](https://covid19api.com)_\nTimestamp: _{data['Date']}_"
                )

                await ctx.send(embed=embed)
                return

        await ctx.send(embed=discord.Embed(color=discord.Color.red(), description="❌ Country not found."))
    
def setup(bot):
    bot.add_cog(Covid(bot))