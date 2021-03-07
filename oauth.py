import requests

client_id = "584108228523065387"
client_secret = "irx9jmOAUMnSfgXAJZwDOCYGTAyXH8ZJ"
redirect_uri = "http://127.0.0.1:5000/login"
discord_login_url = "https://discord.com/api/oauth2/authorize?client_id=584108228523065387&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Flogin&response_type=code&scope=identify%20email%20guilds"
discord_token_url = "https://discord.com/api/oauth2/token"
discord_api_url = "https://discord.com/api"
scope = "identify%20email%20guilds"

def get_access_token(oauth_code):
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "authorization_code",
        "code": oauth_code,
        "redirect_uri": redirect_uri,
        "scope": scope
    }

    access_token = requests.post(url=discord_token_url, data=data).json()
    return access_token["access_token"]

def get_user(access_token):
    url = f"{discord_api_url}/users/@me"
    headers = {"Authorization": f"Bearer {access_token}"}
    user = requests.get(url=url, headers=headers).json()
    return user