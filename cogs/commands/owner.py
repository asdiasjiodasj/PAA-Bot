import discord
from discord.utils import get
import os
from discord.ext import commands
class Owner(commands.Cog):
  @commands.command(name="poll")
  @commands.has_role("Owner")
  async def poll(self,ctx, *, arg: str):
    channel = get(ctx.guild.channels, name = "polls")
    message = await channel.send(f'<@&769980203865866250>, {ctx.author.mention} created a new poll: {arg}')
    emojis = ['<a:agree:757181111163027528>', '<a:disagree:757181140443463780>']
    for emoji in emojis:
      await message.add_reaction(emoji)
    await ctx.message.delete()
  @commands.command(name="announce")
  @commands.has_role("Owner")
  async def announce(self, ctx, *, arg: str):
    channel = get(ctx.guild.channels, name = "announcements")
    await channel.send(f'<@&801464789469495296> \n {ctx.author.mention} made an announcement! \n announcement contains: \n {arg}')
    await ctx.message.delete()
    await ctx.send(f'announcement made succesfully, {ctx.author}')
def setup(bot):
    bot.add_cog(Owner(bot))