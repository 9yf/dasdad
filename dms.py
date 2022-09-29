from roblox import Client
import discord
import random
import aiohttp
import requests
import asyncio
import json
import base64
import linecache
import os
import time
import urllib
import string
from discord.ext import commands
from datetime import datetime
from itertools import cycle
import SimpleEconomy as Seco
from discord.utils import get
from mcstatus import JavaServer
from discord.utils import get
client = Client()
token = "MTAwMDUwNjA0MzkyMDU1MjAxNw.GwA5Ij.x9hDYCALpIsh6SdQezqCYYxjmvXKdltvE9Viz4"


bot = commands.Bot(self_bot=True, command_prefix="sdada")


blm = []

@bot.event
async def on_message(message):
	if message.channel.type == discord.ChannelType.private:
		time.sleep(2)
		user = message.author
		id = message.author.id
		if id in blm:
			pass
		else:
			await user.send("https://discord.gg/sm4BCHmtKU j4j u first ")
			blm.append(id)
			print(blm)
	else:
		pass


bot.run(token, bot=False, reconnect=True) ##
