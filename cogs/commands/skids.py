import discord
import os
from discord.ext import commands
from discord.utils import get
import asyncio
import json
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../db/skids.json')

class Skids(commands.Cog):
  @commands.command()
  @commands.guild_only()
  async def addskid(self, ctx):
    with open(my_file, "r") as f:
      data1 = json.load(f)
    check = lambda m: m.author == ctx.author and m.channel.id == ctx.message.channel.id

    embed = discord.Embed(timestamp=ctx.message.created_at, title="PAA Skid Database", description="Please give the skid's username")
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'this will expire in 30 seconds')
    await ctx.send(content=ctx.author.mention, embed=embed)

    while True:
      try:
        username = await self.bot.wait_for('message', check=check, timeout=30)
      except asyncio.TimeoutError:
        return await ctx.send("You didn't answer in time!")
      else:
        username = str(username.content)
        break
    if username == "cancel" or username == "Cancel":
      return await ctx.send("cancelled")
    await ctx.send('if confirmed, what exploit was the skid using?')
    while True:
      try:
        exploit = await self.bot.wait_for('message', check=check, timeout=300)
      except asyncio.TimeoutError:
        return await ctx.send("You didn't answer in time!")
      else:
        if exploit.content == "cancel" or exploit.content == "Cancel":
          return await ctx.send("cancelled")
        else:
          await ctx.send('what script were they using? if you don\'t know, say None')
      while True:
        try:
          script = await self.bot.wait_for('message', check=check, timeout=300)
        except asyncio.TimeoutError:
          return await ctx.send("You didn't answer in time!")
        else:
          await ctx.send("Any further information? if yes, type that below here :    ), otherwise, type None")
      while True:
        try:
          notes = await self.bot.wait_for('message', check=check, timeout=300)
        except asyncio.TimeoutError:
          return await ctx.send("You didn't answer in time!")
        else:
          await ctx.send("alright, noted.")
        with open(my_file, "r") as f:
          data = json.load(f)
        data[username] = "exploit: " + exploit + "script: " + script + "further notes: " + notes
        with open(my_file, "w") as f:
          json.dump(data, f, indent=3)
        f.close()


def setup(bot):
  bot.add_cog(Skids(bot))