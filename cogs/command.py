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
from discord.ext.commands import Bot
import discord
import random as r
from time import sleep

class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='command')
    async def help(self, ctx):

        embed=discord.Embed(title="Neon 명령어", colour=0x5C7EBB)
        embed.add_field(name="기본적인 명령어들",value="command : 도움말을 호출합니다.\n\n"
        + "invite : 네온봇 초대 링크를 보내줍니다.\n\n" + "github : 네온봇의 Github 저장소 링크를 보여줍니다.\n\n" +
        "server : 네온봇의 개발 서버의 초대 링크를 보내줍니다.\n\nping : 네온봇의 지연율을 반응 속도에 따라 확인합니다.\nㅤ", inline=False)
        embed.add_field(name="게임 명령어들", value="roll : 주사위를 굴립니다.\n사용 예시 : [prefix]roll [number]\n\n" +
                            "lol : 리그 오브 레전드의 현재 티어를 조회합니다.\n주의사항 : 닉네임은 무조건 붙여서 입력하셔야 합니다. 그렇지 않으면 Neon은 소환사명을 인식하지 못해요.\nㅤ", inline=False)
        embed.add_field(name="서버 관리 명령어들",value="clean : 메시지를 [number]개 만큼 삭제합니다.\n사용 예시 : [prefix]clean [number]\n\n" + 
                            "kick : 서버에서 강제 추방합니다.\n사용 예시 : [prefix]ban @username [reason]\n\n" + 
                            "ban : @username을 [reason]이라는 이유로 서버에서 차단합니다.\n사용 예시 : [prefix]ban @username [reason]\nㅤ", inline=False)
        embed.add_field(name="코로나 명령어",value="corona : 코로나-19(COVID-19) 현황을 불러옵니다.", inline=False)
        embed.set_thumbnail(url="http://i.imgur.com/VOKVy0m.jpg")
        embed.set_footer(text="Copyright (c) 2019-2020 sevrino All rights reserved.")
        await ctx.send(embed=embed)
        
    @commands.command(name='ping')
    async def ping(self, ctx):
        embed=discord.Embed(colour=0x5C7EBB)
        embed.add_field(name="PING", value="퐁!")
        embed.set_footer(text="Copyright (c) 2019-2020 sevrino All rights reserved.")
        await ctx.send(embed=embed)
        
    @commands.command(name='invite')
    async def invite(self, ctx):
        embed=discord.Embed(title="네온봇 추가 링크입니다.", url="https://discordapp.com/api/oauth2/authorize?client_id=559709567903072256&permissions=8&scope=bot", colour=0x5C7EBB)
        embed.set_author(name="Neon", url="https://discordapp.com/api/oauth2/authorize?client_id=559709567903072256&permissions=8&scope=bot", icon_url="http://i.imgur.com/VOKVy0m.jpg")
        await ctx.send(embed=embed)
        
    @commands.command(name='github')
    async def github(self, ctx):
        embed=discord.Embed(title="네온봇 Github 주소", url="https://github.cim/sevrino/neonbot", description="네온봇 오류나, 건의사항을 이곳에 이슈로 작성해주세요!", colour=0x5C7EBB)
        embed.set_author(name="sevrino", url="https://github.com/sevrino", icon_url="https://avatars1.githubusercontent.com/u/39475513?s=460&v=4")
        await ctx.send(embed=embed)

    @commands.command(name='server')
    async def server(self, ctx):
        embed=discord.Embed(title="네온봇 개발서버 주소", url="https://discord.gg/PAC6dvw", description="네온봇 오류나, 건의사항을 이곳에 보내주세요!", colour=0x5C7EBB)
        embed.set_author(name="sevrino", url="https://github.com/sevrino", icon_url="https://avatars1.githubusercontent.com/u/39475513?s=460&v=4")
        await ctx.send(embed=embed)

    @commands.command(name='roll')
    async def roll(self, ctx, num):
        num = int(num)
        await ctx.send("주사위 굴리는중...")
        rollnum = r.randint(1, 6)
        await asyncio.sleep(3.0)

        if rollnum == num:
            await ctx.send("당첨되셨습니다!")
        else:
            await ctx.send("안타깝게 실패하셨습니다!")
            await ctx.send("원래 주사위의 숫자 : %d" % rollnum)
            
def setup(bot):
    bot.add_cog(command(bot)) 
    bot.remove_command('help')