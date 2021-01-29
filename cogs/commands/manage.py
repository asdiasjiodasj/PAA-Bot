import discord
import os
from discord.utils import get
from discord.ext import commands

class Manage(commands.Cog):
  @commands.command(name='promote')
  @commands.has_permissions(administrator=True)
  @commands.guild_only()
  async def promote(self, ctx, member: discord.Member):
    trial = get(ctx.guild.roles, name = "trial moderator")
    mod = get(ctx.guild.roles, name = "Moderator")
    headmod = get(ctx.guild.roles, name = "Head Moderator")
    admin = get(ctx.guild.roles, name = "Administrator")
    staffteam = get(ctx.guild.roles, name = "Staff team")
    serverman = get(ctx.guild.roles, name = "server manager")
    staffman = get(ctx.guild.roles, name = "Staff manager")
    cowoner = get(ctx.guild.roles, name = "Co Owner")
    if trial in member.roles:
      await member.remove_roles(trial)
      await member.add_roles(mod)
      await ctx.send(f'promoted {member.mention} to Moderator')
    elif mod in member.roles:
      await member.remove_roles(mod)
      await member.add_roles(headmod)
      await ctx.send(f'promoted {member.mention} to Head Moderator')
    elif headmod in member.roles:
      await member.remove_roles(headmod)
      await member.add_roles(admin)
      await ctx.send(f'promoted {member.mention} to Administrator')
    elif admin in member.roles:
      await member.remove_roles(admin)
      await member.add_roles(staffman)
      await ctx.send(f'promoted {member.mention} to Staff manager')
    elif staffman in member.roles:
      await member.remove_roles(staffman)
      await member.add_roles(serverman)
      await ctx.send(f'promoted {member.mention} to server manager')
    elif serverman in member.roles:
      await member.remove_roles(serverman)
      await member.add_roles(cowoner)
      await ctx.send(f'{member.mention} just got promoted to co woner, and reached the highest they can achieve, WOW!')
    else:
      await member.add_roles(trial)
      await member.add_roles(staffteam)
      await ctx.send(f'welcome, {member.mention}, to the PAA Staff Team!')

def setup(bot):
  bot.add_cog(Manage(bot))