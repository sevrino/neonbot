# -*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2019-2020 sevrino All rights reserved.
"""
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import discord
import random


class command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='도움말')
    async def help(self, ctx):

        embed = discord.Embed(title="Neon 명령어", colour=0x5C7EBB)
        embed.add_field(name="기본적인 명령어들", value="도움말 : 도움말을 호출합니다.\n\n"
                        + "초대 : Neon의 초대 링크를 보내줍니다.\n\n" + "깃허브 : Neon의 Github 저장소 링크를 보여줍니다.\n\n" +
                        "개발서버 : Neon의 개발 서버의 초대 링크를 보내줍니다.\n\n핑 : 네온봇의 지연율을 반응 속도에 따라 확인합니다.\n\n 개발자 : Neon의 개발자를 보여줍니다.\n", inline=False)
        embed.add_field(name="게임 명령어들", value="주사위 [number] : 주사위를 굴려 number과 맞는지 확인합니다.\n사용 예시 : [prefix]주사위 [number]\n\n" +
                        "솔랭 [소환사명]: 리그 오브 레전드의 현재 솔로 랭크 티어를 조회합니다.\n\n" + "자랭 [소환사명] : 리그 오브 레전드의 현재 자유 랭크 티어를 조회합니다.", inline=False)
        embed.add_field(name="서버 관리 명령어들", value="삭제 : 메시지를 [number]개 만큼 삭제합니다.\n사용 예시 : [prefix]삭제 [number]\n\n" +
                        "킥 [@username] : 서버에서 강제 추방합니다.\n사용 예시 : [prefix]킥 @username [reason]\n\n" +
                        "밴 [@username] : @username을 [reason]이라는 이유로 서버에서 차단합니다.\n사용 예시 : [prefix]밴 @username [reason]\nㅤ", inline=False)
        embed.set_thumbnail(url="http://i.imgur.com/VOKVy0m.jpg")
        embed.set_footer(
            text="Copyright (c) 2019-2020 sevrino All rights reserved.")
        await ctx.send(embed=embed)

    @commands.command(name='핑')
    async def ping(self, ctx):
        embed = discord.Embed(colour=0x5C7EBB)
        embed.add_field(name="PING", value="퐁!")
        embed.set_footer(
            text="Copyright (c) 2019-2020 sevrino All rights reserved.")
        await ctx.send(embed=embed)

    @commands.command(name='초대')
    async def invite(self, ctx):
        embed = discord.Embed(
            title="네온봇 추가 링크입니다.", url="https://discordapp.com/api/oauth2/authorize?client_id=559709567903072256&permissions=8&scope=bot", colour=0x5C7EBB)
        embed.set_author(name="Neon", url="https://discordapp.com/api/oauth2/authorize?client_id=559709567903072256&permissions=8&scope=bot",
                         icon_url="http://i.imgur.com/VOKVy0m.jpg")
        await ctx.send(embed=embed)

    @commands.command(name='깃허브')
    async def github(self, ctx):
        embed = discord.Embed(title="네온봇 Github 주소", url="https://github.com/sevrino/neonbot",
                              description="네온봇 오류나, 건의사항을 이곳에 이슈로 작성해주세요!", colour=0x5C7EBB)
        embed.set_author(name="sevrino", url="https://github.com/sevrino",
                         icon_url="https://avatars1.githubusercontent.com/u/39475513?s=460&v=4")
        await ctx.send(embed=embed)

    @commands.command(name='개발서버')
    async def server(self, ctx):
        embed = discord.Embed(title="네온봇 개발서버 주소", url="https://discord.gg/PAC6dvw",
                              description="네온봇 오류나, 건의사항을 이곳에 보내주세요!", colour=0x5C7EBB)
        embed.set_author(name="sevrino", url="https://github.com/sevrino",
                         icon_url="https://avatars1.githubusercontent.com/u/39475513?s=460&v=4")
        await ctx.send(embed=embed)

    @commands.command(name='주사위')
    async def roll(self, ctx, num):
        num = int(num)
        await ctx.send("주사위 굴리는중...")
        rollnum = randint(1, 6)
        await asyncio.sleep(3.0)

        if rollnum == num:
            await ctx.send("당첨되셨습니다!")
        else:
            await ctx.send("안타깝게 실패하셨습니다!")
            await ctx.send("원래 주사위의 숫자 : %d" % rollnum)

    @commands.command(name='오이')
    async def egg(self, ctx):
        await ctx.send("오이 저따 버려!")

    @commands.command(name='개발자')
    async def egg(self, ctx):
        await ctx.send("신수#4495")


def setup(bot):
    bot.add_cog(command(bot))
    bot.remove_command('help')
