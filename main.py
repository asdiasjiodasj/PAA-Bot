import keep_alive
import os
import discord
import json
import pyrblx
import random
import asyncio
from discord import Status
from discord.utils import get
import time
from discord.ext import commands,tasks
from datetime import datetime
import typing
from time import sleep
import requests
import io
from datetime import date
my_file = os.path.join('./cogs/db/username.json')

snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

with open("package.json","r") as f:
    data = json.load(f)
PREFIX = ';'
f.close()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(f"{PREFIX}"),intents=intents)
bot.launch_time = datetime.utcnow()
@bot.event
async def on_ready():
    print("BOT IS READY NOW")

keep_alive.keep_alive()

@bot.command()
async def uptime(ctx):
  await ctx.send(f'bot started at {bot.launch_time}')

Extensions = ["cogs.events.events", "cogs.commands.owner", "cogs.commands.other", "cogs.commands.music", "cogs.commands.manage", "cogs.commands.userinfo", "cogs.commands.skids", "cogs.commands.verify", "cogs.commands.purge", "cogs.events.reactions"]

@bot.command(name='nick', aliases=["name", "nickname"])
@commands.has_role("Staff team")
async def nick(ctx, member: discord.Member, nick):
  await member.edit(nick=nick)
  await ctx.send(f'Nickname was changed for {member.mention} ')
  chan = get(ctx.guild.channels, name = "command-usage-logs")
  embed=discord.Embed(title="Command used!", description=f"{ctx.author} used a command in {ctx.channel}")
  embed.set_author(name=f"{ctx.author}")
  embed.add_field(name="command used: ",value="nick", inline=False)
  embed.add_field(name="target: ", value=f"{member}", inline=False)
  embed.add_field(name="nickname: ", value=f"{nick}", inline=False)
  await chan.send(embed=embed)
@bot.command()
@commands.has_permissions(administrator=True)
async def fix(ctx):
  await ctx.channel.edit(sync_permissions=True)
  await ctx.send("Fixed permissions succesfully!")

if __name__ == '__main__':
    print("Starting the Bot.....")
    time.sleep(3)
    for extension in Extensions:
      try:
        bot.load_extension(extension)
        print(f'loaded {extension}')
      except Exception as eer:
        print(eer)

@bot.command()
@commands.is_owner()
async def roleid(ctx, role: discord.Role):
  await ctx.send(role.id)

@bot.event
async def on_connect():
  print("Connected to discord api\n Please wait for the bot to be ready!")
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching,name='Project Anti Abusers win!'))

class MemberRoles(commands.MemberConverter):
    async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]

@bot.command()
@commands.has_role("Staff team")
async def snipe(message):
  if snipe_message_content==None:
    await message.channel.send("There's nothing to snipe!")
  else:
    embed = discord.Embed(description=f"{snipe_message_content}")
    embed.set_footer(text=f"requested by {message.author}", icon_url=message.author.avatar_url)
    embed.set_author(name= f"{snipe_message_author}")
    await message.channel.send(embed=embed)
    return

@bot.command(name='8ball')
async def _8ball(ctx, *, question):
  responses = ['Maybe.','Certainly not.','I hope so.','Not in your wildest dreams.','There is a good chance.','Quite likely.','I think so.','I hope not.','I hope so.','Never!','Pfft.','Sorry, bucko.','Hell, yes.','Hell to the no.','The future is bleak.','The future is uncertain.','I would rather not say.','Who cares?','Possibly.','Never, ever, ever.','There is a small chance.','Yes!','lol no.','There is a high probability.','What difference does it make?','Not my problem.','Ask someone else.','go fuck yourself.','lol what?']
  await ctx.send(f'{random.choice(responses)}')

@bot.event
async def on_message_delete(message):
  if message.content.startswith(';'): return
  if message.author.bot: return
  if message.author.id == 786594973423370332: return
  global snipe_message_content
  global snipe_message_author
  global snipe_message_id

  snipe_message_content = message.content
  snipe_message_author = message.author
  snipe_message_id = message.id
  
  embed=discord.Embed(title="Message deleted", description=f"Message deleted in {message.channel}", color=0x09c8e1)
  embed.set_author(name="Python bot made by Chaotic Mind#0666")
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/9N6fDrzHGpppwDrzpfGKVPPzNxsYT3nGKQ78coAH6dI/%3Fsize%3D128/https/cdn.discordapp.com/icons/738013984757645333/1d5ccefec3e79257b3aedd691daeca98.png")
  embed.add_field(name="Message author:", value=f"{message.author}", inline=True)
  embed.add_field(name="Message content:", value=f"{message.content}", inline=True)
  chan = get(message.guild.channels, name="deletedlogs")
  await chan.send(embed=embed)
  await asyncio.sleep(60)
  if message.id == snipe_message_id:
    snipe_message_author = None
    snipe_message_content = None
    snipe_message_id = None

@bot.event
async def on_message_edit(old, new):
  if old.author.bot: return
  if old == new: return
  embed=discord.Embed(title="Message edited", description=f"Message edited in {old.channel}", color=0x09c8e1)
  embed.set_author(name="Python bot made by Chaotic Mind#0666")
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/9N6fDrzHGpppwDrzpfGKVPPzNxsYT3nGKQ78coAH6dI/%3Fsize%3D128/https/cdn.discordapp.com/icons/738013984757645333/1d5ccefec3e79257b3aedd691daeca98.png")
  embed.add_field(name="Message author:", value=f"{old.author}", inline=True)
  embed.add_field(name="Message content before: ", value=f"{old.content}", inline=True)
  embed.add_field(name="message content after: ", value=f"{new.content}", inline=True)
  channel = get(old.guild.channels, name="editlogs")
  await channel.send(embed=embed)


funny = ["why have i been pinged?", "what?", "ping?", 'y do', 'shut the fuck up', 'oi leave me alone']

@bot.event
async def on_message(message):
  if message.guild is None: return
  if message.author.bot: return
  if message.author.id == 774564327809744916:
    return
  if message.author.id == 597778690667053066:
    return
  role = get(message.guild.roles, name = "blacklist bot")
  if role in message.author.roles:
    return
  if message.content == "F":
    await message.channel.send(f'{message.author} has paid respects 🙏')
  if message.content == 'f':
    await message.channel.send(f'{message.author} has paid respects 🙏')
  if "discord.gg/" in message.content.lower():
    role = get(message.guild.roles, name = "Staff team")
    role2 = get(message.guild.roles, name = "Partner")
    if role in message.author.roles: return
    if role2 in message.author.roles: return
    await message.delete()
    await message.channel.send(f"Invite links are not allowed here, {message.author.mention}")
  if "penis dinner" in message.content.lower():
    await message.channel.send('https://tenor.com/view/penis-dinner-watermelon-eat-devour-messy-gif-17623973')
  for member in message.mentions:
    if member.id == 786594973423370332:
      if message.author.id != 265953382441680907:
        return await message.channel.send("stfu?")
    elif member.id == 265953382441680907:
      if message.author.id != 786594973423370332:
        return await message.channel.send("Since you aren't Brandon who pinged, I will politely ask you to shut the fuck up and not ping this person again.")
    elif member.id == 788513931101995048:
      return await message.channel.send(random.choice(funny))

  await bot.process_commands(message)

@bot.command(name="find")
async def find(ctx, arg):
  try:
    plr = pyrblx.Players(arg)
  except pyrblx.PlayerNotFound:
    await ctx.send("i couldn't find this user.")
  embed=discord.Embed(title=f"user: {plr.user_name()}", description=f"id: {plr.user_id()}", color=0x00e1ff)
  embed.set_thumbnail(url=f"{plr.thumbnail()}")
  embed.add_field(name="description: ", value=f"{plr.description()}", inline=True)
  embed.add_field(name="creation date: ", value=f"{plr.created_at()}", inline=True)
  embed.add_field(name="friends count: ", value=f"{plr.friends_count()}", inline=True)
  embed.add_field(name="latest friend: ", value=f"{plr.latest_friend()}", inline=True)
  embed.add_field(name="oldest friend: ", value=f"{plr.oldest_friend()}", inline=True)
  embed.add_field(name="group count: ", value=f"{plr.groups_count()}", inline=True)
  embed.add_field(name="url to profile: ", value=f"{plr.direct_url()}", inline=True)
  await ctx.send(embed=embed)

@bot.command(name='ghostping', hidden=True)
@commands.has_role("Owner")
async def ghostping(ctx, member: discord.Member):
  await ctx.message.delete()
  await ctx.author.send(f"ghostpinged {member} succesfully")
  for channel in ctx.guild.channels:
    msg = await channel.send(member.mention)
    await msg.delete()

@bot.command(name="role")
@commands.has_role("Staff team")
async def giverole(ctx, user: discord.Member, role: discord.Role):
  await user.add_roles(role)
  await ctx.send(f'added {role} to {user} succesfully')
  chan = get(ctx.guild.channels, name = "command-usage-logs")
  embed=discord.Embed(title="Command used!", description=f"{ctx.author} used a command in {ctx.channel}")
  embed.set_author(name=f"{ctx.author}")
  embed.add_field(name="command used: ",value="role", inline=False)
  embed.add_field(name="target: ", value=f"{user}", inline=False)
  embed.add_field(name="role: ", value=f"{role}", inline=True)
  await chan.send(embed=embed)

@bot.command()
async def ping(ctx):
  embed = discord.Embed(title=f'pong! latency is  {round (bot.latency * 1000)}ms')
  await ctx.send(embed=embed)
  chan = get(ctx.guild.channels, name = "command-usage-logs")
  embed=discord.Embed(title="Command used!", description=f"{ctx.author} used a command in {ctx.channel}")
  embed.set_author(name=f"{ctx.author}")
  embed.add_field(name="command used: ", value="Ping", inline=False)
  await chan.send(embed=embed)

@bot.command(name="say")
@commands.has_role("Staff team")
async def say(ctx, *, arg):
  await ctx.send(arg)
  await ctx.message.delete()
  chan = get(ctx.guild.channels, name = "command-usage-logs")
  embed=discord.Embed(title="Command used!", description=f"{ctx.author} used a command in {ctx.channel}")
  embed.set_author(name=f"{ctx.author}")
  embed.add_field(name="command used: ", value="say", inline=False)
  embed.add_field(name="arguments: ", value=f"{arg}", inline=True)
  await chan.send(embed=embed)

@bot.event
async def on_member_join(member):
  print("Recognised that a member called " + member.name + " joined")
  chan = get(member.guild.channels, name = "joins")
  embed=discord.Embed(title="Member joined", color=0x05e2ff)
  embed.set_author(name="Project Anti Abusers Bot")
  embed.add_field(name=f"Welcome, {member} to Project Anti Abusers", value=f"{member.mention}", inline=False)
  embed.add_field(name="member id: ", value=f"{member.id}", inline=True)
  await chan.send(content=member.mention, embed=embed)
  with open(my_file,"r") as f:
    datad = json.load(f)
  if str(member.id) not in datad.keys():
    pass
    f.close()
  else:
    try:
      noob = datad[str(member.id)]
      await member.edit(nick=noob, reason="PAA bot Verification")
      unverif = get(member.guild.roles, name = "Unverified")
      verif = get(member.guild.roles, name = "Member")
      await member.remove_roles(unverif)
      await member.add_roles(verif, reason="PAA Auto Verification Found")
      f.close()
    except Exception as err:
      print(err)
      pass
  now = datetime.utcnow()
  day = member.created_at
  age = now - day
  asd = age.days
  if asd < 8:
    altdet = get(member.guild.roles, name = "alt")
    unverif = get(member.guild.roles, name = "Unverified")
    await member.remove_roles(unverif)
    await member.add_roles(altdet, reason="PAA Alt detection")
    try:
      await member.send("It looks like you are an alt, and have been prevented to access the server for the most part. if you believe that this is an issue, please contact staff.")
    except discord.Forbidden:
      pass
  try: 
    await member.send(f'Hi there, {member.mention}, Welcome to Project Anti Abusers')
    channel = get(ctx.guild.channels, name = "verify-tutorial")
    await member.send(f'Please verify in order to continue (check {channel.mention} on how to)')
    print("Sent message to " + member.name)
  except:
    print("Couldn't message " + member.name)

    # give member the steam role here
    ## to do this the bot must have 'Manage Roles' permission on server, and role to add must be lower than bot's top role
    role = get(member.guild.roles, name="Unverified")
    await member.add_roles(role)
    print("Added role '" + role.name + "' to " + member.name)

@bot.event
async def on_member_remove(member):
    serverchannel = get(member.guild.channels, name = "leaves")
    msg = "goodbye, {0}".format(member)
    await serverchannel.send(msg)
    
@bot.command()
@commands.has_role("Owner")
async def createmute(ctx):
  role = get(ctx.guild.roles, name = "Muted")
  hell = get(ctx.guild.channels, name = "Muted-Hell")
  if not role:
    try:
      muted = await ctx.guild.create_role(name = "Muted")
      for channel in ctx.guild.channels:
        await channel.set_permissions(muted, send_messages=False, read_message_history=False, read_messages=False)
    except discord.Forbidden:
      return await ctx.send("Seems like i am missing permissions.")
    await ctx.send("created muted role succesfully")
  else:
    await ctx.send("Muted role already exists!")
  if not hell:
    perms = {ctx.guild.default_role: discord.PermissionOverwrite(read_message_history=False), ctx.guild.me: discord.PermissionOverwrite(send_messages=True), muted: discord.PermissionOverwrite(read_message_history=True)}
    try:
      channel = await ctx.guild.create_text_channel("Muted-Hell", overwrites=perms)
    except discord.Forbidden:
      return await ctx.send("i don't have perms what?")
    await ctx.send("Created channel Muted-Hell succesfully!")

@bot.command(name='unban')
@commands.has_role("Staff team")
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f'unbanned {user}')

  
@bot.command()
@commands.has_role("Staff team")
async def ban(ctx, member: discord.Member, reason):
  if "Staff team" in member.roles:
    return await ctx.send("You cannot punish staff!")
  try:
    await member.send(f"You have been banned in Project Anti Abusers for the reason: {reason}")
    asd = reason
    await ctx.guild.ban(member, reason=asd)
    await ctx.send(f'banned {user} succesfully!')
  except discord.Forbidden:
    return await ctx.send("i couldn't ban what?")
@bot.command()
@commands.has_role("Staff team")
async def softban(ctx, member: discord.Member, reason=None):
  if "Staff team" in member.roles:
    return await ctx.send("You cannot softban staff!")
  try:
    await member.send(f'you got softbanned lol(reason: {reason}, executor: {ctx.author})')
    await ctx.guild.ban(member)
    await ctx.guild.unban(member)
  except discord.Forbidden:
    return await ctx.send("i have no perms what?")
@bot.command()
@commands.has_role("Staff team")
async def mute(ctx, member:discord.Member, reason):
  if "Staff team" in member.roles:
    return await ctx.send("You cannot mute staff")
  else:
    muted = get(member.guild.roles, name = "Muted")
    await member.add_roles(muted)
    await ctx.send(f'muted {member} succesfully!')
    await member.send(f"You have been muted in Project Anti Abusers for the reason: {reason} (muted by {ctx.author})")
@bot.command()
@commands.has_role("Staff team")
async def kick(ctx, member: discord.Member, reason=None):
  if "Staff team" in member.roles:
    return await ctx.send("You cannot kick staff!")
  try:
    await member.send(f"You have been kicked from Project Anti Abusers for the reason: {reason}")
    await member.guild.kick(member, reason=reason)
  except discord.Forbidden:
    return await ctx.send("no perms okfuckyou")
@bot.command()
@commands.has_role("Staff team")
async def unmute(ctx, user: discord.Member):
  await user.remove_roles(get(ctx.guild.roles, name = "Muted"))
  await ctx.send(f'{user.mention} got unmuted succesfully')

@bot.command()
@commands.has_role("Staff team")
async def luc(ctx, user: discord.Member):
  role = get(ctx.guild.roles, name = "Staff team")
  if role in member.roles: return await ctx.send("You cannot lock this person out!")
  if not role in member.roles: await ctx.set_permission(user, send_messages=False)
  await ctx.send(f"locked {user.mention} out of {ctx.channel.mention} succesfully")

@bot.command()
@commands.has_role("Staff team")
async def unluc(ctx, user: discord.Member):
  await ctx.set_permission(user, send_messages=True)
  await ctx.send(f"Unlocked {user.mention} from {ctx.channel.mention} succesfully!")

@bot.command()
@commands.is_owner()
async def rules(ctx):
  embed=discord.Embed(title="Project Anti Abusers: Server Rules", description="Breaking any of these will be punished accordingly", color=0x00ff59)
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/738013984757645333/8dba563139cb334dbaed76ba5db675a4.jpg")
  embed.add_field(name="Swearing / slurs", value="Swearing is allowed in this server. However, the use of slurs is not allowed.", inline=False)
  embed.add_field(name="Media", value="For the use of media: you'll need to follow the following rules \nNo loud audio's or video's \nNo nsfw outside of the horny jail \nNo nsfl content anywhere \n (ofc) no discord crashers \n no disallowed file types (images, gifs, txt files, videos and audio files are allowed)", inline=False)
  embed.add_field(name="usage of channels", value="Only use a channel for their specific purpose (eg. no bot commands outside bot commands)", inline=False)
  embed.add_field(name="raiding / spamming", value="raiding of any kind will result in a ban (no exceptions). spamming will be punished accordingly. spamming any bot anywhere will result into a punishment accordingly (which can range from bot blacklists to permanent bans)", inline=False)
  embed.add_field(name="advertising", value="advertising in any way (yes, dms included) will result in a ban **unless the user ASKED for an invite**", inline=False)
  embed.add_field(name="Role begging", value="begging or asking for any role will be punished accordingly. all roles you can get without problems are in #react-for-roles", inline=False)
  embed.add_field(name="usernames", value="your username has to be mentionable. complaining about a change in username may result into further punishments", inline=False)
  embed.add_field(name="mentioning", value="no pinging staff manager or above for no reason. no mass pinging or ghostpinging.", inline=False)
  embed.add_field(name="channel pins / topics", value="read channel pins/topics for channel specific rules. failing to follow those will be punished even if claimed to be unaware.", inline=False)
  embed.add_field(name="Follow discord's TOS", value="failing to follow any part of discord's TOS may result in an instant ban.", inline=False)
  embed.add_field(name="loopholes", value="using any kind of loopholes to break the rules will be punished ", inline=False)
  embed.add_field(name="leaking / cracking", value="leaking any script will be punished accordingly. threatening to crack or cracking any script or trying to get people to crack or leak something will result in a ban.", inline=True)
  await ctx.send(embed=embed)

@bot.command(aliases=['staffapplication'])
async def apply(ctx):
  q_list = [
    "If a staff was abusing members and/or other staff, what would you do if the owner is inactive?",
    "if a member was spamming in ANY channel, how would you solve that?",
    "if a staff is in bad behavior, what would you do if the owner is inactive?",
    "why do you want to become staff?",
    "what would you do if people were to report a paa abuser to you?"
  ]
  a_list = []
  submit_channel = bot.get_channel(738021490552864803)
  channel = await ctx.author.create_dm()

  def check(m):
    return m.content is not None and m.channel == channel and m.author.id == ctx.author.id

  for question in q_list:
    sleep(.5)
    await channel.send(question)
    msg = await bot.wait_for('message', check=check)
    a_list.append(msg.content)

  submit_wait = True
  while submit_wait:
    await channel.send('End of questions - "submit" to finish')
    msg = await bot.wait_for('message', check=check)
    if "submit" in msg.content.lower():
      submit_wait = False
      answers = "\n".join(f'{a}. {b}' for a, b in enumerate(a_list, 1))
      submit_msg = f'Application from {msg.author} \nThe answers are:\n{answers}'
      await submit_channel.send(submit_msg)

bot.run('Nzg4NTEzOTMxMTAxOTk1MDQ4.X9km0w.SNgG2E8TDkMHDzFzmQEHxnBJcaw')