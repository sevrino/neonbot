# -*- coding:utf-8 -*- 
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2019-2020 sevrino All rights reserved.
"""
import discord
import asyncio
import re
import json
from discord.ext import commands
from discord import Permissions

class manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='kick')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason):
        try:
            await member.kick(reason=reason)
            await ctx.send("해당 사용자를 추방하였습니다. 사유 : " + reason)
        except:
            embed=discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.", value="해당 사용자를 추방할 수 없습니다. 봇의 권한보다 사용자가 가진 권한이 상위 권한이거나 같은 권한일 경우 이 현상이 일어납니다. 봇의 권한을 다시 확인해 주세요.")
            embed.set_footer(text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)
    
    @commands.command(name='ban')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason):
        try:
            await member.ban(reason=reason)
            await ctx.send("해당 사용자를 차단하였습니다. 사유 : " + reason)
        except:
            embed=discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.", value="해당 사용자를 차단할 수 없습니다. 봇의 권한보다 사용자가 가진 권한이 상위 권한이거나 같은 권한일 경우 이 현상이 일어납니다. 봇의 권한을 다시 확인해 주세요.")
            embed.set_footer(text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)
    
    @commands.command(name='clean')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def clean(self, ctx, amount):
        try:
            amount = int(amount)
            await ctx.channel.purge(limit = amount)
            await ctx.send("%d개의 채팅을 삭제했습니다." % amount)
        except TypeError:
            await ctx.send("개수를 잘못 지정하셨거나 봇에 오류가 있습니다. 다시 시도해 주세요.")

    @commands.command(name='mute')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, member : discord.Member):
        try:
            role = discord.utils.get(ctx.guild.roles, name='뮤트')
            await member.add_roles(member, role)
            await ctx.send("해당 플레이어의 채팅을 제한했습니다.")
        except discord.errors.NotFound:
            pass

    @commands.command(name='unmute')
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, member : discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='뮤트')
        await member.remove_roles(member, role)
        await ctx.send("해당 플레이어의 채팅 제한을 해제했습니다.")

def setup(bot):
    bot.add_cog(manage(bot))