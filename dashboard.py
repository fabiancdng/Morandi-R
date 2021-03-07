from flask import Flask, render_template, request, session
import oauth

app = Flask(__name__, static_folder="web/public", template_folder="web/templates")
app.config["SECRET_KEY"] = "owALkS5wbEkNpyk8u"

@app.route("/")
def home():
    return render_template("index.html", discord_url=oauth.discord_login_url)

@app.route("/login")
def login():
    oauth_code = request.args["code"]
    access_token = oauth.get_access_token(oauth_code)
    session["token"] = access_token
    
    user = oauth.get_user(access_token)
    user_name = user["username"]
    user_id = user["discriminator"]

    return user_name + user_id

app.run("127.0.0.1", 5000)