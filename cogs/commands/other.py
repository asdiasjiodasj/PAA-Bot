import discord
from discord.utils import get
import os
from discord.ext import commands
class Other(commands.Cog):
  @commands.command(name='avatar',aliases=["av"])
  async def avatar(self, ctx, *,  avamember : discord.Member=None):
    if avamember is None:
      avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
    chan = get(ctx.guild.channels, name = "command-usage-logs")
    embed=discord.Embed(title="Command used!", description=f"{ctx.author} used a command in {ctx.channel}")
    embed.set_author(name=f"{ctx.author}")
    embed.add_field(name="command used: ", value="avatar", inline=False)
    embed.add_field(name="target: ", value=f"{member}", inline=False)
    await chan.send(embed=embed)
  @commands.command()
  async def invite(self,ctx):
    await ctx.author.send("Here's your invite! https://discord.gg/CWSsGEm")

  @commands.command(name='members')
  async def members(self,ctx):
    await ctx.send(f'{ctx.guild.name} has {ctx.guild.member_count} members')
    def handle_custom(self, user):
      print(user.activities)
      a = [c for c in user.activities if c.type == ActivityType.custom]
      if not a:
        return None, ActivityType.custom
      a = a[0]
      c_status = None
      if not a.name:
        c_status = self.bot.get_emoji(a.emoji.id)
      if c_status:
        pass
      if a.name and a.emoji:
        c_status = f"{a.emoji} {a.name}"
      elif a.emoji and not c_status:
        c_status = f"{a.emoji}"
      elif a.name:
        c_status = a.name
      else:
        c_status = None
      return c_status, ActivityType.custom

    def handle_playing(self, user):
      p_acts = [c for c in user.activities if c.type == ActivityType.playing]
      p_act = p_acts[0] if p_acts else None
      act = p_act.name if p_act and p_act.name else None
      return act, ActivityType.playing
    def handle_streaming(self, user):
      s_acts = [c for c in user.activities if c.type == ActivityType.streaming]
      s_act = s_acts[0] if s_acts else None
      act = f"{s_act.name}{' | ' if s_act.game else ''}{s_act.game or ''}" if s_act and s_act.name and hasattr(s_act, "game") else s_act.name if s_act and s_act.name else None
      return act, ActivityType.streaming
    def handle_listening(self, user):
      l_acts = [c for c in user.activities if c.type == ActivityType.listening]
      l_act = l_acts[0] if l_acts else None
      act = f"{l_act.title}{' | ' if l_act.artists[0] else ''}{l_act.artists[0] or ''}" if l_act and hasattr(l_act, "title") else l_act.name if l_act and l_act.name else None
      return act, ActivityType.listening
    def handle_watching(self, user):
      w_acts = [c for c in user.activities if c.type == ActivityType.watching]
      w_act = w_acts[0] if w_acts else None
      act = w_act.name if w_act else None
      return act, ActivityType.watching
    
    @commands.command(name='userinfo', aliases=['whois', 'info'])
    @commands.guild_only()   
    async def userinfo(self, ctx, *, user: discord.Member = None):
        author = ctx.author
        guild = ctx.guild

        if not user:
            user = author

        roles = user.roles[-1:0:-1]
        names, nicks = await self.get_names_and_nicks(user)

        joined_at = user.joined_at
        since_created = (ctx.message.created_at - user.created_at).days
        if joined_at is not None:
          since_joined = (ctx.message.created_at - joined_at).days
          user_joined = joined_at.strftime("%d %b %Y %H:%M")
        else:
          since_joined = "?"
          user_joined = _("Unknown")
        user_created = user.created_at.strftime("%d %b %Y %H:%M")
        voice_state = user.voice
        member_number = (
          sorted(guild.members, key=lambda m: m.joined_at or ctx.message.created_at).index(user)
          + 1
        )

        created_on = _("{}\n({} days ago)").format(user_created, since_created)
        joined_on = _("{}\n({} days ago)").format(user_joined, since_joined)

        if user.status.name == "online":
          if user.is_on_mobile() is True:
            statusemoji = "https://cdn.discordapp.com/emojis/554418132953989140.png?v=1"
          else:
            statusemoji = "https://cdn.discordapp.com/emojis/642458713738838017.png?v=1"
        elif user.status.name == "offline":
          statusemoji = "https://cdn.discordapp.com/emojis/642458714074513427.png?v=1"
        elif user.status.name == "dnd":
          statusemoji = "https://cdn.discordapp.com/emojis/642458714145816602.png?v=1"
        elif user.status.name == "streaming":
          statusemoji = "https://cdn.discordapp.com/emojis/642458713692569602.png?v=1"
        elif user.status.name == "idle":
          statusemoji = "https://cdn.discordapp.com/emojis/642458714003210240.png?v=1"

        if roles:

          role_str = ", ".join([x.mention for x in roles])
            # 400 BAD REQUEST (error code: 50035): Invalid Form Body
            # In embed.fields.2.value: Must be 1024 or fewer in length.
          if len(role_str) > 1024:
                # Alternative string building time.
                # This is not the most optimal, but if you're hitting this, you are losing more time
                # to every single check running on users than the occasional user info invoke
                # We don't start by building this way, since the number of times we hit this should be
                # infintesimally small compared to when we don't across all uses of Red.
            continuation_string = _(
              "and {numeric_number} more roles not displayed due to embed limits."
            )
          available_length = 1024 - len(continuation_string)  # do not attempt to tweak, i18n

          role_chunks = []
          remaining_roles = 0

          for r in roles:
            chunk = f"{r.mention}, "
            chunk_size = len(chunk)

            if chunk_size < available_length:
              available_length -= chunk_size
              role_chunks.append(chunk)
            else:
              remaining_roles += 1

            role_chunks.append(continuation_string.format(numeric_number=remaining_roles))

            role_str = "".join(role_chunks)

        else:
            role_str = None

        if status is None:
          data = discord.Embed(description="{}".format(activity), colour=user.colour)
        else:
          data = discord.Embed(
            description="{}\nCustom Status: {}".format(activity, custom), colour=user.colour
          )
            
        data.add_field(name=_("Joined Discord on"), value=created_on)
        data.add_field(name=_("Joined this server on"), value=joined_on)
        if role_str is not None:
          data.add_field(name=_("Roles"), value=role_str, inline=False)
        if names:
            # May need sanitizing later, but mentions do not ping in embeds currently
          val = filter_invites(", ".join(names))
          data.add_field(name=_("Previous Names"), value=val, inline=False)
        if nicks:
            # May need sanitizing later, but mentions do not ping in embeds currently
          val = filter_invites(", ".join(nicks))
          data.add_field(name=_("Previous Nicknames"), value=val, inline=False)
        if voice_state and voice_state.channel:
          data.add_field(
              name=_("Current voice channel"),
              value="{0.mention} ID: {0.id}".format(voice_state.channel),
              inline=False,
            )
        data.set_footer(text=_("Member #{} | User ID: {}").format(member_number, user.id))

        name = str(user)
        name = " ~ ".join((name, user.nick)) if user.nick else name
        name = filter_invites(name)

        if user.avatar:
          avatar = user.avatar_url_as(static_format="png")
          data.set_author(name=name, url=avatar, icon_url=statusemoji)
          data.set_thumbnail(url=avatar)
        else:
          data.set_author(name=name)

        await ctx.send(embed=data)

def setup(bot):
    bot.add_cog(Other(bot))