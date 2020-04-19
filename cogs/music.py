#-*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2019-2020 sevrino All rights reserved.
"""
import discord
import json
from discord.ext import commands
from discord import Permissions
import youtube_dl

class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='join')
    @commands.guild_only()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect(timeout=120.0, reconnect=True)
        await ctx.send("음성 채널에 들어갔어요.")
        

    @commands.command(name='leave')
    @commands.guild_only()
    async def leave(self, ctx):
        channel = ctx.message.guild
        voice_client = ctx.guild.voice_client(channel)
        await voice_client.disconnect()
        await ctx.send("음성 채널에서 나갔어요.")

    @commands.command(name='play')
    @commands.guild_only()
    async def play(self, ctx, url):
        await ctx.send("음악을 준비하고 있어요.")
        
        #Music Player Part
        server = ctx.message.guild
        voice_client = ctx.guild.voice_client(channel)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

        await ctx.send("재생중인 곡 : %s" % players)
def setup(bot):
    bot.add_cog(music(bot))