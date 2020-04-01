import discord
import asyncio
import re
import json
import discord
from discord.ext import commands
from discord import Permissions
import requests as r

class COVID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='corona')
    @commands.guild_only()
    async def corona(self, ctx):
        url = "http://apiland.site:81/kr_corona"
        
        #json 파일 다운로드
        with open("./config/COVID-19.json", "wb") as file:
            response = r.get(url)
            file.write(response.content)
            
        #다운로드한 json 파일에서 데이터 끌어오기
        with open("./config/COVID-19.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            checked = data["Confirmator"]
            clear = data["Cured"]
            death = data["Dead"]
            ing = data["Inspection"]

        embed=discord.Embed(title="코로나 현황",description="감염자 : %s\n완치자 : %s\n사망자 : %s\n검사중 : %s" % (checked, clear, death, ing), color=0x5C7EBB)
        embed.set_footer(text = "Copyright (c) 2019-2020 sevrino All rights reserved.")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(COVID(bot))