# -*- coding:utf-8 -*-
"""
The GNU GENERAL PUBLIC LICENSE
Copyright (c) 2019-2020 sevrino All rights reserved.
"""
import discord
from discord.ext import commands
import json
import requests as r


class league(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='솔랭')
    async def lol(self, ctx, *, summonername):

        with open('./config/setting.json') as json_file:
            json_data = json.load(json_file)
            key = json_data["riot-api"]

        summoner = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
            summonername + "?api_key=" + key

        with open("./config/league/solo/id.json", "wb") as file:
            response = r.get(summoner)
            file.write(response.content)

        with open("./config/league/solo/id.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            try:
                id = data["id"]
                sumname = data["name"]
            except:
                embed = discord.Embed(colour=0xFF0000)
                embed.add_field(name="오류가 발생했습니다.",
                                value="해당 소환사는 존재하지 않는 소환사입니다.")
                embed.set_footer(
                    text="Copyright (c) 2019-2020 sevrino All rights reserved.")
                await ctx.send(embed=embed)

        tier = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + \
            id + "?api_key=" + key

        try:
            with open("./config/league/solo/info.json", "wb") as file:
                response = r.get(tier)
                file.write(response.content)

            with open("./config/league/solo/info.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                queue_type = data[0]["queueType"]
                try:
                    if queue_type == "RANKED_FLEX_SR":
                        solo_tier = data[1]["tier"]
                        solo_rank = data[1]["rank"]
                        point = data[1]["leaguePoints"]
                    elif queue_type == "RANKED_SOLO_5x5":
                        solo_tier = data[0]["tier"]
                        solo_tier = data[0]["rank"]
                        point = data[0]["leaguePoints"]
                except:
                    raise AttributeError

        except UnboundLocalError:
            embed = discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.",
                            value="LOL API 파싱중 오류가 발생했습니다. 개발서버에 문의해주세요.")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        except KeyError:
            embed = discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.",
                            value="너무 많은 요청으로 인해 오류가 발생했습니다. 나중에 시도해 주세요.")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        except IndexError:
            embed = discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.",
                            value="해당 플레이어는 현재 티어 미배치, 자체 오류 등으로 인해 솔로 랭크 티어가 표기되지 않습니다. 나중에 시도해 주세요.")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "IRON":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="IRON" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0x515A5A)
            embed.set_image(url="https://i.imgur.com/mpUoT5g.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "BRONZE":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="BRONZE" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0x6E2C00)
            embed.set_image(url="https://i.imgur.com/LfyvNkt.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "SILVER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="SILVER" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0xD0D3D4)
            embed.set_image(url="https://i.imgur.com/731l30m.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "GOLD":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="GOLD" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0xF7DC6F)
            embed.set_image(url="https://i.imgur.com/RRpiMqG.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "PLATINUM":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="PLATINUM" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0xABEBC6)
            embed.set_image(url="https://i.imgur.com/xOaoBtt.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "DIAMOND":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="DIAMOND" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0xBB8FCE)
            embed.set_image(url="https://i.imgur.com/RNFgHcM.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "MASTER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="MASTER" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0x8E44AD)
            embed.set_image(url="https://i.imgur.com/yAT4oPN.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "GRANDMASTER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="GRANDMASTER" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0xEC7063)
            embed.set_image(url="https://i.imgur.com/TuMPSw5.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if solo_tier == "CHALLENGER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % solo_tier + " " + "%s" % solo_rank,
                                  description="CHALLENGER" + " " + "%s" % solo_rank + " " + "%slp" % point, colour=0x0080FF)
            embed.set_image(url="https://i.imgur.com/9jfZLTn.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

    @commands.command(name='자랭')
    async def teamrank(self, ctx, *, name):
        with open('./config/setting.json') as json_file:
            json_data = json.load(json_file)
            key = json_data["riot-api"]

        summoner = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
            name + "?api_key=" + key

        with open("./config/league/flex/id.json", "wb") as file:
            response = r.get(summoner)
            file.write(response.content)

        with open("./config/league/flex/id.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            try:
                id = data["id"]
                sumname = data["name"]
            except:
                embed = discord.Embed(colour=0xFF0000)
                embed.add_field(name="오류가 발생했습니다.",
                                value="해당 소환사는 존재하지 않는 소환사입니다.")
                embed.set_footer(
                    text="Copyright (c) 2019-2020 sevrino All rights reserved.")
                await ctx.send(embed=embed)

        tier = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + \
            id + "?api_key=" + key
        try:
            with open("./config/league/flex/info.json", "wb") as file:
                response = r.get(tier)
                file.write(response.content)

            with open("./config/league/flex/info.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
                queue_type = data[1]["queueType"]
                if queue_type == "RANKED_FLEX_SR":
                    flex_tier = data[1]["tier"]
                    flex_rank = data[1]["rank"]
                    point = data[1]["leaguePoints"]
                elif queue_type == "RANKED_SOLO_5x5":
                    flex_tier = data[0]["tier"]
                    flex_rank = data[0]["rank"]
                    point = data[0]["leaguePoints"]

        except UnboundLocalError:
            embed = discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.",
                            value="LOL API 파싱중 오류가 발생했습니다. 개발서버에 문의해주세요.")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        except KeyError:
            embed = discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.",
                            value="너무 많은 요청으로 인해 오류가 발생했습니다. 나중에 시도해 주세요.")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        except IndexError:
            embed = discord.Embed(colour=0xFF0000)
            embed.add_field(name="오류가 발생했습니다.",
                            value="해당 플레이어는 현재 티어 미배치, 자체 오류 등으로 인해 자유 랭크 티어가 표기되지 않습니다. 나중에 시도해 주세요.")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "IRON":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="IRON" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0x515A5A)
            embed.set_image(url="https://i.imgur.com/mpUoT5g.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "BRONZE":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="BRONZE" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0x6E2C00)
            embed.set_image(url="https://i.imgur.com/LfyvNkt.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "SILVER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="SILVER" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0xD0D3D4)
            embed.set_image(url="https://i.imgur.com/731l30m.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "GOLD":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="GOLD" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0xF7DC6F)
            embed.set_image(url="https://i.imgur.com/RRpiMqG.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "PLATINUM":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="PLATINUM" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0xABEBC6)
            embed.set_image(url="https://i.imgur.com/xOaoBtt.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "DIAMOND":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="DIAMOND" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0xBB8FCE)
            embed.set_image(url="https://i.imgur.com/RNFgHcM.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "MASTER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="MASTER" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0x8E44AD)
            embed.set_image(url="https://i.imgur.com/yAT4oPN.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "GRANDMASTER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="GRANDMASTER" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0xEC7063)
            embed.set_image(url="https://i.imgur.com/TuMPSw5.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)

        if flex_tier == "CHALLENGER":
            embed = discord.Embed(title="%s님의 티어입니다." % sumname, value="%s" % flex_tier + " " + "%s" % flex_rank,
                                  description="CHALLENGER" + " " + "%s" % flex_rank + " " + "%slp" % point, colour=0x0080FF)
            embed.set_image(url="https://i.imgur.com/9jfZLTn.png")
            embed.set_footer(
                text="Copyright (c) 2019-2020 sevrino All rights reserved.")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(league(bot))
