import discord
from discord.ext import commands
import pyrblx
import asyncio
import json
import random
import os
from discord.utils import get
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../db/username.json')

class Verify(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(manage_nicknames=True)
    async def verify(self,ctx):
        if ctx.guild.me.top_role.position < ctx.author.top_role.position:
            return await ctx.send("Please make sure my role is higher than you ")
        if "alt" in ctx.author.roles:
          return await ctx.send("Sorry, but you have been prevented to verify!")
        with open(my_file,"r") as f:
            data1 = json.load(f)
        if str(ctx.author.id) in data1.keys():
            await ctx.send("You Are Already Verified\n You Can reverify by `;reverify` ")
            f.close()
            unverif = get(ctx.guild.roles, name = "Unverified")
            await ctx.author.remove_roles(unverif)
            verif = get(ctx.guild.roles, name = "Member")
            await ctx.author.add_roles(verif)
            return
        check = lambda m: m.author == ctx.author and m.channel.id == ctx.message.channel.id

        embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                              description="Please enter your roblox username")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 30 seconds")


        await ctx.send(content=ctx.author.mention, embed=embed)

        while True:

            try:
                username = await self.bot.wait_for('message', check=check, timeout=30)
            except asyncio.TimeoutError:
                return await ctx.send("You didnt Answer in time :/\n Please verify once more ")
            else:
                username = str(username.content)
                break
        if username == "cancel" or username == "Cancel":
            return await ctx.send("Verification Cancelled!")
        try:
            NOOB = pyrblx.Players(f"{username}")
        except pyrblx.PlayerNotFound:
            await ctx.send(f"No Player Found!\n Please Verify Once More")
            return
        else:
            sentences1 = [f"glasses or soda and soda and key or vase", "lego or soda and pants or book or bus",
                          "glasses or book or bus or nothing or vase", "book or vase or poo or human or something",
                          "vase bus or nothing or nothing", "sorry or nothing", "thank or bus or bus",
                          "nothing or bus and vase", "bye vase or bus", "bus vase and nothing ",
                          "soda or vase nothing ", "roblox cola bus vase ok", "vase or okay", "soda lemon or buy",
                          "cya", "its okay or nothing", "pee poo sodaa ee", "human vase or bye","Cute","eliz cute","Bss is epic","vase but also nothing","k but lemon"]
            sentences = random.choice(sentences1)
            sentences = sentences.strip()
            sentences = str(sentences)

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                                  description=f"Paste this in your roblox description\n`{sentences}`\n\nSay `done` when done\n Say `cancel` to cancel")
            embed.set_author(name=f"{ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 5 minutes")
            await ctx.send(content=ctx.author.mention,embed=embed)
            while True:

                try:
                    message = await self.bot.wait_for('message', check=check, timeout=300)
                except asyncio.TimeoutError:
                    return await ctx.send("You didn't Answer in time :/\n Please verify once more ")
                else:

                    if message.content == "cancel" or message.content == "Cancel":
                        return await ctx.send("Verification Cancelled")
                    elif message.content == "done" or message.content == "Done":
                        break
                    else:
                        await ctx.send(f" {ctx.author.mention}\nPlease Say `done` or `cancel`",delete_after=5)

            try:
                NOOB = pyrblx.Players(f"{username}")
            except pyrblx.PlayerNotFound:
                await ctx.send("You should not see this message tho")
            if NOOB.description() == sentences:
                await ctx.send("Working, Please wait", delete_after=10)
                await asyncio.sleep(1)
                with open(my_file, "r") as f:
                    data = json.load(f)
                data[ctx.author.id] = username
                with open(my_file, "w") as f:
                    json.dump(data, f, indent=3)
                f.close()
                try:
                    await ctx.author.edit(nick=username, reason="Verification")
                except discord.Forbidden:
                    pass
                finally:
                    await ctx.send(f"{ctx.author.mention},Welcome To `{ctx.message.guild.name}`!")
                    await ctx.message.delete()
                    member = get(ctx.guild.roles, name = "Member")
                    await ctx.author.add_roles(member)
                    unverified = get(ctx.guild.roles, name="Unverified")
                    await ctx.author.remove_roles(unverified)



            else:
                await ctx.send(f"You didnt changed your description\nPlease Verify once again")
                return
    @commands.command()
    @commands.guild_only()
    @commands.bot_has_permissions(manage_nicknames=True)
    async def reverify(self,ctx):
        if ctx.guild.me.top_role.position < ctx.author.top_role.position:
            return await ctx.send("Please make sure my role is higher than you ")
        with open(my_file,"r") as f:
            data1 = json.load(f)
        if str(ctx.author.id) not in data1.keys():
            await ctx.send("You First Need To verify first ")
            f.close()
            return
        embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                              description="Please enter your roblox username")
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 30 seconds")
        check = lambda m: m.author == ctx.author and m.channel.id == ctx.message.channel.id


        await ctx.send(content=ctx.author.mention, embed=embed)

        while True:

            try:
                username = await self.bot.wait_for('message', check=check, timeout=30)
            except asyncio.TimeoutError:
                return await ctx.send("You Didnt Answered in time :/ ")
            else:
                username = str(username.content)
                break

        if username == "cancel" or username == "Cancel":
            return await ctx.send("Verification Cancelled!!")

        try:
            NOOB = pyrblx.Players(f"{username}")
        except pyrblx.PlayerNotFound:
            return await ctx.send("You didnt answer in time :/\n Please verify once more ")

        else:
            sentences1 = [f"glasses or soda and soda and key or vase", "lego or soda and pants or book or bus",
                          "glasses or book or bus or nothing or vase", "book or vase or poo or human or something",
                          "vase bus or nothing or nothing", "sorry or nothing", "thank or bus or bus",
                          "nothing or bus and vase", "bye vase or bus", "bus vase and nothing ",
                          "soda or vase nothing ", "roblox cola bus vase ok", "vase or okay", "soda lemon or buy",
                          "cya", "its okay or nothing", "no nvm bye vase", "how trucks are made?", "oof bye vase ","Cute","eliz cute","Bss is epic","vase but also nothing","k but lemon"]
            sentences = random.choice(sentences1)
            sentences = sentences.strip()
            sentences = str(sentences)

            embed = discord.Embed(timestamp=ctx.message.created_at, title="Verification",
                                  description=f"Paste this in your roblox description\n`{sentences}`\n\nSay `done` when done\n Say `cancel` to cancel")
            embed.set_author(name=f"{ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_footer(icon_url=ctx.author.avatar_url, text=f"Prompt will expire in 35 minutes")
            await ctx.send(content=ctx.author.mention,embed=embed)
            while True:
                try:
                    message = await self.bot.wait_for('message', check=check, timeout=300)
                except asyncio.TimeoutError:
                    return await ctx.send("You didn't answer in time :/\n Please verify once more ")
                else:

                    if message.content == "cancel" or message.content == "Cancel":
                        return await ctx.send("Verification Cancelled")
                    elif message.content == "done" or message.content == "Done":
                        break
                    else:
                        await ctx.send(f" {ctx.author.mention}\nPlease Say `done` or `cancel`",delete_after=5)
            try:
                NOOB = pyrblx.Players(f"{username}")
            except pyrblx.PlayerNotFound:
                await ctx.send("You should not see this message tho")
            if NOOB.description() == sentences:
                await ctx.send("Working Please wait", delete_after=10)
                await asyncio.sleep(1)
                with open(my_file, "r") as f:
                    data = json.load(f)
                data.pop(str(ctx.author.id))
                with open(my_file, "w") as f:
                    json.dump(data, f, indent=3)
                f.close()
                with open(my_file, "r") as f:
                    data = json.load(f)
                data[ctx.author.id] = username
                with open(my_file, "w") as f:
                    json.dump(data, f, indent=3)
                f.close()
                try:
                    await ctx.author.edit(nick=username, reason="Verification")
                except discord.Forbidden:
                        pass
                finally:
                    await ctx.send(f"{ctx.author.mention},Welcome To `{ctx.message.guild.name}`!")
                    await ctx.message.delete()
                    unverif = get(ctx.guild.roles, name = "Unverified")
                    verif = get(ctx.guild.roles, name = "Member")
                    await ctx.author.add_roles(verif)
                    await ctx.author.remove_roles(unverif)

            else:
                await ctx.send(f"You did'nt changed your description\nPlease Verify once again")
                return


    @commands.command()
    @commands.guild_only()
    async def rbx(self,ctx,user:discord.Member=None):
        if user is None:
            user = ctx.author
        with open(my_file,"r") as f:
            l = json.load(f)
        if str(user.id) not in l.keys():
            return await ctx.send("Please Verify First")
        else:
            noob  = l[str(user.id)]
            await ctx.send(f"{user.mention} Roblox name is `{noob}`")


def setup(bot):
    bot.add_cog(Verify(bot))