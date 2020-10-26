# -*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2019-2020 sevrino All rights reserved.
"""
import discord
import json
import logging
import os
from discord.ext import commands

# Logging part
logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)
handler = logging.FileHandler(
    filename='./log/bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Json Part
with open('./config/setting.json') as json_file:
    json_data = json.load(json_file)

    token = json_data["bot_token"]
    token_beta = json_data["bot_token_beta"]
    prefix = json_data["default_prefix"]
    ver = json_data["ver"]

# beta bot activation
beta = False
if beta == True:
    token_release = token_beta
else:
    token_release = token

# Bot Part
client = commands.Bot(command_prefix=prefix)
bot = discord.Client()


@client.event
async def on_ready():
    logger.critical("BOT STARTED")
    print("\n봇을 실행해주셔서 감사합니다! 현재 Neon의 버전은 %s 입니다. github에서 최신 버전이 있는지 확인해 주세요.\ngithub link : https://github.com/sevrino/neonbot\n" % ver)
    print(client.user.name)
    print(client.user.id)

    game = discord.Game("%s도움말" % prefix + " | " + "v.%s" % ver)
    await client.change_presence(status=discord.Status.online, activity=game)

# Cogs Part
extension = ["cogs.command", "cogs.manage", "cogs.league"]

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token_release)
