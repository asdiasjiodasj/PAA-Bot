from discord.ext import commands
import discord
import os
import json
import datetime
from discord.utils import get
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../db/username.json')
from pyrblx import BadArgument
class Events(commands.Cog):
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"Commands On Cooldown,try again after {error.retry_after:.2f}",delete_after=10)
        elif isinstance(error,commands.CommandNotFound):
            await ctx.send("Commands Not Found",delete_after=5)
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.send(f'Am Missing Perms - \n'
                           "".join([error.missing_perms]))
        elif isinstance(error,commands.PrivateMessageOnly):
            await ctx.send("This Commands Can Only Run In DMS",delete_after=10)
        elif isinstance(error,commands.NoPrivateMessage):
            await ctx.send("This Commands Can Not run in Dms",delete_after=10)
        elif isinstance(error,BadArgument):
            await ctx.send("ok i errored fuck you")
        elif isinstance(error,commands.MissingPermissions):
            print(error.missing_perms)
            await ctx.send(f' Miss Perms - `{" & ".join(error.missing_perms)}`')
                        
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        print(f"I Was Added To A New Server\nSever Name: {guild.name}\nGuild ID: {guild.id} Sever Owner Name: {guild.owner.id}\nOwner ID:{guild.owner.id}")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        print(f"I Was Removed From A Server\nSever Name: {guild.name}\nGuild ID: {guild.id} Sever Owner Name: {guild.owner.id}\nOwner ID:{guild.owner.id}")
def setup(bot):
    bot.add_cog(Events(bot))