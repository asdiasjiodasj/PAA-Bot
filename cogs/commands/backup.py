import discord
from discord.utils import get
from discord.ext import commands, tasks
import os
import asyncio

class Backup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    @commands.guild_only()
    async def createserver(self, ctx):
        bot = self.bot
        bot.create_guild(f'PAA Backup')
        await asyncio.sleep(4)
        for a in bot.guilds:
            if "PAA Backup" in a.name:
                for channel in a.channels:
                    link = await ctx.channel.create_invite(max_age = 300)
                    user = get(ctx.guild.members, id = 786594973423370332)
                    await user.send(link)
        await ctx.send('done yes')

def setup(bot):
    bot.add_cog(Backup(bot))