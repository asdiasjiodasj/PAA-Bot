import typing
from discord.ext import commands
from discord import User, errors


class Purge(commands.Cog, name='Purge'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name='purge',
        hidden=True,
    )
    async def purge(
        self, ctx,
        num_messages: int,
    ):
        channel = ctx.message.channel
        await ctx.message.delete()
        await channel.purge(limit=num_messages, check=None, before=None)
        return True

    @commands.command(
        name='purge_until',
        hidden=True,
    )
    async def purge_until(
        self, ctx,
        message_id: int,
    ):
        channel = ctx.message.channel
        try:
            message = await channel.fetch_message(message_id)
        except errors.NotFound:
            await ctx.send("Message could not be found in this channel")
            return

        await ctx.message.delete()
        await channel.purge(after=message)
        return True

    @commands.command(
        name='purge_user',
        hidden=True,
        aliases=['purgeu', 'purgeuser'],
    )
    async def purge_user(
        self, ctx,
        user: User,
        num_messages: typing.Optional[int] = 100,
    ):
        channel = ctx.message.channel

        def check(msg):
            return msg.author.id == user.id

        await ctx.message.delete()
        await channel.purge(limit=num_messages, check=check, before=None)


def setup(bot):
    bot.add_cog(Purge(bot))