import difflib
import discord
import json
import os

from discord.ext import commands

from scrape.rune_recommendation import League

file = open('data.json')
json_data = json.load(file)
champs = [i for i in json_data]


class Normal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    Rune = League()

    @commands.command()
    async def ping(self, context):
        await context.send(f"Bot's ping is {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def rune(self, context, champion, role=None):
        close_matches = difflib.get_close_matches(champion, champs, 1, 0.7)
        if close_matches:
            if role is None:
                role = json_data[close_matches[0]]
            else:
                role = difflib.get_close_matches(role, ['jungle', 'middle', 'adc', 'top', 'support'], 1, 0.4)[0]
            await context.send(f"{champion}'s rune", file=discord.File(self.Rune.get_rune(close_matches[0], role)))
            os.remove(f"{close_matches[0]}.png")
        else:
            await context.send("Sorry we cannot find this champion!")


def setup(bot):
    bot.add_cog(Normal(bot))
