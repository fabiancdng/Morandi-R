import config
from quart import Quart, render_template, request, session, redirect, url_for
from quart_discord import DiscordOAuth2Session
from discord.ext import ipc

app = Quart(__name__, static_folder="web/public", template_folder="web/templates")
ipc_client = ipc.Client(secret_key=config.ipc_key)

app.config["SECRET_KEY"] = config.secret_key
app.config["DISCORD_CLIENT_ID"] = config.discord_client_id
app.config["DISCORD_CLIENT_SECRET"] =  config.discord_client_secret
app.config["DISCORD_REDIRECT_URI"] = config.discord_redirect_uri

discord = DiscordOAuth2Session(app)

@app.route("/")
async def home():
    return await render_template("index.html")

@app.route("/login")
async def login():
    return await discord.create_session()

@app.route("/callback")
async def callback():
    try:
        await discord.callback()
    except:
        return redirect(url_for("login"))
    
    user = await discord.fetch_user()
    return f"{user}"

@app.route("/dashboard")
async def dashboard():
    guild_ids = await ipc_client.request("get_mutual_guilds")
    user_guilds = await discord.fetch_guilds()
    owned_guilds = []
    mutual_guilds = []

    for guild in user_guilds:
        if guild.is_owner == True and guild.id not in guild_ids:
            owned_guilds.append(guild)
        elif guild.is_owner == True and guild.id in guild_ids:
            mutual_guilds.append(guild)

    return await render_template("dashboard.html", owned_guilds=owned_guilds, mutual_guilds=mutual_guilds)

app.run("127.0.0.1", 5000)