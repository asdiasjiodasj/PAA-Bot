@commands.Cog.listener()
    async def on_member_join(self, member):
        with open(my_file,"r") as f:
            datad = json.load(f)
        if str(member.id) not in datad.keys():
            pass
            f.close()
        else:
            try:
                noob = datad[str(member.id)]
                await member.edit(nick=noob, reason="PAA bot Verification")
                f.close()
            except Exception as err:
                print(err)
                pass
      
        try:
            chennal = self.bot.get_channel(745904435372490823)
            noob = member.created_at
            now = datetime.datetime.utcnow()
            diff = now - noob
            dayss = diff.days
            months, days = divmod(dayss, 30)
            yrs, months = divmod(months, 12)
            embed = discord.Embed(color=discord.Color.green(), timestamp=datetime.datetime.utcnow())
            embed.set_author(name=f"{member} Just Joined", icon_url=member.avatar_url)
            embed.add_field(name="Account Age:",
                            value=f'{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}\n({yrs} Years, {months} Months, {days} Days)',
                            inline=False)
            embed.add_field(name=f"Joined {member.guild.name} on:",
                            value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(text=f"Member ID: {member.id}", icon_url=member.guild.icon_url)
            await chennal.send(content=member.mention, embed=embed)
            if dayss <= 7:
                rope = member.guild.get_role(776530576056254476)
                await member.add_roles(rope, reason="Alt Detected")
                try:
                    await member.send(
                        "It looks like your account is not old enough(Possibly Alt) to see all channels, If this was a mistake please contact any staff member.")
                    await chennal.send(f"{member.mention} Was Given Alt Role")
                except discord.Forbidden:
                    pass
        except Exception as err:
            print(err)
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        chennal = self.bot.get_channel(745904442246692896)
        noob = member.created_at
        now = datetime.datetime.utcnow()
        diff = now - noob
        dayss = diff.days
        months, days = divmod(dayss, 30)
        yrs, months = divmod(months, 12)
        embed = discord.Embed(color=discord.Color.from_rgb(165, 42, 42), timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member} Just Left The Server", icon_url=member.avatar_url)
        embed.add_field(name="Account Age:",
                        value=f'{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}\n({yrs} Years, {months} Months, {days} Days)',
                        inline=False)
        embed.add_field(name=f"Joined {member.guild.name} on:",
                        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Member ID: {member.id}", icon_url=member.guild.icon_url)
        await chennal.send(content=member.mention, embed=embed)
#-------------------------------------------
@commands.command(name='nick', aliases=["name", "nickname"])
  async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')
    chan = get(ctx.guild.channels, name = "command-usage-logs")
    embed=discord.Embed(title="Command used!", description=f"{ctx.author} used a command in {ctx.channel}")
    embed.set_author(name=f"{ctx.author}")
    embed.add_field(name="command used: ", value="nick", inline=False)
    embed.add_field(name="target: ", value=f"{member}", inline=False)
    embed.add_field(name="nickname: ", value=f"{nick}", inline=False)
    await chan.send(embed=embed)
  @commands.command()
  async def fix(ctx):
    await ctx.channel.edit(sync_permissions=True)
    await ctx.send("Fixed permissions succesfully!")