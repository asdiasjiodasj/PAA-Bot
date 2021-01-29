import discord
from discord.ext import commands

class Userinfo(commands.Cog):
  @commands.command(aliases=["whois"])
  async def userinfo(self, ctx, *,  target: discord.Member=None):
    if target is None:
      target = ctx.author
    roles = [role for role in target.roles if role != ctx.guild.default_role]
    embed = discord.Embed(title="User information", colour=discord.Color.gold(), timestamp=datetime.utcnow())

    embed.set_author(name=target.name, icon_url=target.avatar_url)

    embed.set_thumbnail(url=target.avatar_url)

    fields = [("Name", str(target), False),
    ("ID", target.id, False),
    ("Status", str(target.status).title(), False),
    (f"Roles ({len(roles)})", " ".join([role.mention for role in roles]), False),
    ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
    ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), False)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Userinfo(bot))