<div align="center">
    <img src="https://cdn.discordapp.com/avatars/584108228523065387/f762ac9bbf11dcaa6a1db8b5c6fc358d.png?size=256" width="230px" />
    <h1>Morandi</h1>
    <h3>
        Morandi is a multi-purpose Discord bot with a web dashboard.
    </h3>
</div>

---

<div align="center">
    <h2>⚠️ DEPRECATED ⚠️</h2>
    <p>⚠️ This project is no longer used or maintained. ⚠️</p>
    <p> Hence, <i><b>I do not recommend using this in production!</b></i></p>
</div>

---

<br>

## Why am I not working on this project anymore?
Recently, Discord announced a couple of changes to their bot API(s) that are both good and bad. Although what they call ["Slash Commands"](https://blog.discord.com/slash-commands-are-here-8db0a385d9e6) is certainly a cool concept, I do not agree with their philosophy of forcing developers to use it by [deprecating message content access](https://support-dev.discord.com/hc/en-us/articles/4404772028055-Message-Content-Access-Deprecation-for-Verified-Bots) as it is, which is how commands are currently implemented in (I would say) 99% of all bots.

Due to these changes (and more), [Rapptz](https://github.com/Rapptz), maintainer of the [discord.py API wrapper](https://github.com/Rapptz/discord.py), [announced the end of the discord.py library](https://gist.github.com/Rapptz/4a2f62751b9600a31a0d3c78100287f1), which is also used in this project. Although there are maintained forks and the library is probably still usable, I don't want to keep developing features for this bot that will soon stop working anyway. Implementing "Slash Commands" is essentially rewriting the whole bot, which I don't feel like doing right now.

However, if there are more community-made packages available for easily implementing Slash Commands, I might pick up on this project or do a rewrite.

<br>

## What is Morandi?
**Morandi is a multi-purpose Discord bot with a web dashboard.**
I'm working towards making it a multi-talented bot that can help you with almost anything.
This project is based on the idea of [this repository](https://github.com/fabiancdng/Morandi) I created a few years ago. I thought it'd be nice to do a rewrite of it but change some of its core ideas and make it more of an 'all-rounder' as well as implementing a web dashboard for (almost) all controls.

<br>

## Features
### Multi-server support
Morandi can be used in multiple servers concurrently.

![Image broken](https://github.com/fabiancdng/Morandi-R/blob/master/assets/guild-dashboard.png?raw=true)

### Web dashboard

![Image broken](https://github.com/fabiancdng/Morandi-R/blob/master/assets/dashboard.png?raw=true)

* Configuration of the bot can be done using a web interface instead of a 'config' command or something
* Leadberboard of the XP and level system

### XP and leveling system
* A customizable amount of XP is given to a user every minute they chat.
* With a certain (with each level increasing) amount of XP the user levels up.
* Role rewards for specific levels
* rank - command for getting a user's XP and level count as well as their position on the leaderboard
### Other useful commands like:
* **clear [amount of messages]** - deletes messages in a channel
* **ping** - checks the bot's latency

<br>

## Third party dependencies

### Bot
* [discord.py](https://github.com/Rapptz/discord.py)
* [discord-ext-ipc](https://github.com/Ext-Creators/discord-ext-ipc)
* [pymysql](https://github.com/PyMySQL/PyMySQL)
### Web Dashoard
* [Quart](https://github.com/xutaoding/quart)
* [Quart-Discord](https://github.com/jnawk/Quart-Discord)
* [Materialize](https://materializecss.com/)

<br>

**Copyright © 2021 Fabian Reinders (fabiancdng)**
  
