# Morandi-R
## Morandi is a multi-functional discord bot with a web dashboard.

---

<p align="center" style="border-radius: 100%;"><img src="https://cdn.discordapp.com/avatars/584108228523065387/f762ac9bbf11dcaa6a1db8b5c6fc358d.png?size=256"></p>

---

## What is Morandi?
**Morandi is a multi-functional discord bot with a web dashboard.**
I'm working towards making it a multi-talented bot that can help you with almost anything.
This project is based on the idea [this repository](https://github.com/fabiancdng/Morandi) I created a few years ago. I thought it'd be nice to pick it up but change some of its core ideas and make it more of an 'all-rounder' as well as implementing a web dashboard for (almost) all controls.

<br>

## Features
### Multi-server support
Morandi can be used in unlimited servers concurrently.

![Image broken](https://github.com/fabiancdng/Morandi-R/blob/master/assets/guild-dashboard.png?raw=true)

### **[WIP]** Web dashboard

![Image broken](https://github.com/fabiancdng/Morandi-R/blob/master/assets/dashboard.png?raw=true)

* Configuration of the bot is made thorugh a web interface instead of a 'config' commands or something
* Leadberboard of the XP and level system

### XP and leveling system
* A customizable amount of XP is given to a user every minute they chat.
* With a certain (with each level increasing) amount of XP the user levels up.
* **[WIP]** Role rewards for specific levels
* **[WIP]** rank - command for getting a user's XP and level count as well as their position on the leaderboard
### Other useful commands like:
* **clear [amount of messages]** - deletes messages in a channel
* **ping** - checks the bot's latency

<br>

## How to set up Morandi
Currently, there is no hosted version of Morandi available. If you'd like to use the bot, you'll have to host it yourself using the guide below.
### Self-hosting guide
1. **Install the dependencies**
    + [Linux, macOS, etc.] ```python3 -m pip install pymysql discord.py discord-ext-ipc quart quart-discord```
    + [Windows] ```pip install pymysql discord.py discord-ext-ipc quart quart-discord```
2. **Rename 'config.py.template' to 'config.py' and enter your data**
    + The bot requires a mysql server
    + The bot requires a discord client and bot user - [guide](https://discordpy.readthedocs.io/en/latest/discord.html)
3. **Run the discord bot (from the direction the bot is installed in)**
    + [Linux, macOS, etc.] ```python3 app.py```
    + [Windows] ```python app.py```
4. **Run the web dashboard (in a new terminal/console) [optional]**
    + [Linux, macOS, etc.] ```python3 dashboard.py```
    + [Windows] ```python dashboard.py```

<br>

## Contributing
* If you'd like to help develop Morandi, I highly encourage you to do so!
* Contributions can be made using Pull requests.
* If you have any suggestions / feature requests, you may use the 'Issues' tab to submit them.

<br>

## Credits / Dependencies
Morandi uses some third party libraries:  
### Bot
* [discord.py](https://github.com/Rapptz/discord.py)
* [discord-ext-ipc](https://github.com/Ext-Creators/discord-ext-ipc)
* [pymysql](https://github.com/PyMySQL/PyMySQL)
### Web Dashoard
* [Materialize](https://materializecss.com/)
* [jQuery](https://jquery.com/)
* [Quart](https://github.com/xutaoding/quart)
* [Quart-Discord](https://github.com/jnawk/Quart-Discord)

<br>

**Copyright © 2021 fabiancdng (Fabian R.)**
  