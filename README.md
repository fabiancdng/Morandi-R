<div align="center">
    <img src="https://cdn.discordapp.com/avatars/584108228523065387/f762ac9bbf11dcaa6a1db8b5c6fc358d.png?size=256" width="230px" />
    <h1>Morandi</h1>
    <h3>
        Morandi is a multi-purpose Discord bot with a web dashboard.
    </h3><br><br>
</div>

---

## What is Morandi?
**Morandi is a multi-purpose Discord bot with a web dashboard.**
I'm working towards making it a multi-talented bot that can help you with almost anything.
This project is based on the idea [this repository](https://github.com/fabiancdng/Morandi) I created a few years ago. I thought it'd be nice to do a rewrite of it but change some of its core ideas and make it more of an 'all-rounder' as well as implementing a web dashboard for (almost) all controls.

<br>

## Why am I not working on this project anymore?
I originally took a break from this project to start learning the programming language 'Go'. As I participated in a Hackathon around that time, I started getting into [discordgo](https://github.com/bwmarrin/discordgo). I discovered that Go has a major advantage over Python when working on a project like this and that is its incredibly good built-in concurrency. I am currently working on a new bot written in Go that uses the built-in concurrency and channels for communicating between API and Bot. I'm not saying I'll never work on this project again. But it is on hold.

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
  
