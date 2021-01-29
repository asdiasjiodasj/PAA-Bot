import discord
from discord.ext import commands
from discord.utils import get
import os

class Reactionroles(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    bot = self.bot
    if payload.guild_id == 738013984757645333:
      sever = bot.get_guild(738013984757645333)
      member = sever.get_member(payload.user_id)
      if payload.message_id == 777095378704138261:
        role = sever.get_role(769980203865866250)
        await payload.member.add_roles(role,reason="Reaction Role")
      elif payload.message_id == 777095640605523998:
        role = sever.get_role(775737426530140171)
        await payload.member.add_roles(role, reason="Reaction Roles")
      elif payload.message_id == 765132572593750046:
        role = sever.get_role(765132572593750046)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096287920193566:
        role = sever.get_role(756855960911216660)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096842004398082:
        role = sever.get_role(759107100482863104)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096867195650048:
        role = sever.get_role(759104722455363615)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096901518426183:
        role = sever.get_role(772804255328632832)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096925202743326:
        role = sever.get_role(759107107819094056)
        await payload.member.add_roles(role, reason = "Reacton Roles")
      elif payload.message_id == 777096953993232396:
        role = sever.get_role(759107103838830672)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096978433310760:
        role = sever.get_role(759105494022619199)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097123735797760:
        role = sever.get_role(759105221909020702)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097143437623296:
        role = sever.get_role(759104953612107806)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097232704602132:
        role = sever.get_role(759107487491424306)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097244326494228:
        role = sever.get_role(759104836854874173)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097258964746240:
        role = sever.get_role(759107595675238462)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097272730714132:
        role = sever.get_role(759104560328998923)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097288648097832:
        role = sever.get_role(759107694153302066)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097301130608661:
        role = sever.get_role(759107784804401162)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097320104984606:
        role = sever.get_role(759107900521185281)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097334684516373:
        role = sever.get_role(759107988983250994)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097345749876736:
        role = sever.get_role(759108239694102539)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097361289510912:
        role = sever.get_role(759108378923761765)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097376292667393:
        role = sever.get_role(759108442265747505)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097388111822909:
        role = sever.get_role(759108691802194000)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097401948700692:
        role = sever.get_role(759108848693936129)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097452414042132:
        role = sever.get_role(759108917015347281)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801466034368413757:
        role = sever.get_role(801464789469495296)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801466107592179753:
        role = sever.get_role(801465448574746634)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801467145061400636:
        role = sever.get_role(801466341554913301)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801468316774301726:
        role = sever.get_role(794999839707758640)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801468385321287750:
        role = sever.get_role(794999029879668777)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801468502926032956:
        role = sever.get_role(801467623794540545)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801469493359673416:
        role = sever.get_role(801468991616974899)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801470478081458206:
        role = sever.get_role(801469105600200755)
        await payload.member.add_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801470536827797566:
        role = sever.get_role(801469588516372520)
        await payload.member.add_roles(role, reason = "Reaction Roles")
  
  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    bot = self.bot
    if payload.guild_id == 738013984757645333:
      sever = bot.get_guild(738013984757645333)
      member = sever.get_member(payload.user_id)
      if payload.message_id == 777095378704138261:
        role = sever.get_role(769980203865866250)
        await member.remove_roles(role,reason="Reaction Role")
      elif payload.message_id == 777095640605523998:
        role = sever.get_role(775737426530140171)
        await member.remove_roles(role, reason="Reaction Role")
      elif payload.message_id == 765132572593750046:
        role = sever.get_role(765132572593750046)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096287920193566:
        role = sever.get_role(756855960911216660)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096842004398082:
        role = sever.get_role(759107100482863104)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096867195650048:
        role = sever.get_role(759104722455363615)
        await member.remove_roles(role, reason = "reaction Roles")
      elif payload.message_id == 777096901518426183:
        role = sever.get_role(772804255328632832)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096925202743326:
        role = sever.get_role(759107107819094056)
        await member.remove_roles(role, reason = "Reacton Roles")
      elif payload.message_id == 777096953993232396:
        role = sever.get_role(759107103838830672)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777096978433310760:
        role = sever.get_role(759105494022619199)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097123735797760:
        role = sever.get_role(759105221909020702)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097143437623296:
        role = sever.get_role(759104953612107806)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097232704602132:
        role = sever.get_role(759107487491424306)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097244326494228:
        role = sever.get_role(759104836854874173)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097258964746240:
        role = sever.get_role(759107595675238462)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097272730714132:
        role = sever.get_role(759104560328998923)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097288648097832:
        role = sever.get_role(759107694153302066)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097301130608661:
        role = sever.get_role(759107784804401162)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097320104984606:
        role = sever.get_role(759107900521185281)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097334684516373:
        role = sever.get_role(759107988983250994)
        await member.remove_roles(role,reason = "Reaction Roles")
      elif payload.message_id == 777097345749876736:
        role = sever.get_role(759108239694102539)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097361289510912:
        role = sever.get_role(759108378923761765)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097376292667393:
        role = sever.get_role(759108442265747505)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097388111822909:
        role = sever.get_role(759108691802194000)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097401948700692:
        role = sever.get_role(759108848693936129)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 777097452414042132:
        role = sever.get_role(759108917015347281)
        await member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801466034368413757:
        role = sever.get_role(801464789469495296)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801466107592179753:
        role = sever.get_role(801465448574746634)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801467145061400636:
        role = sever.get_role(801466341554913301)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801468316774301726:
        role = sever.get_role(794999839707758640)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801468385321287750:
        role = sever.get_role(794999029879668777)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801468502926032956:
        role = sever.get_role(801467623794540545)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801469493359673416:
        role = sever.get_role(801468991616974899)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801470478081458206:
        role = sever.get_role(801469105600200755)
        await payload.member.remove_roles(role, reason = "Reaction Roles")
      elif payload.message_id == 801470536827797566:
        role = sever.get_role(801469588516372520)
        await payload.member.remove_roles(role, reason = "Reaction Roles")

def setup(bot):
  bot.add_cog(Reactionroles(bot))