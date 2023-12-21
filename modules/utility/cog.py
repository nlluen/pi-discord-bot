import asyncio

import discord
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='purge', help='purge x amount of message')
    async def purge(self, ctx, arg: int):
        if arg < 15:
            await ctx.channel.purge(limit=arg+1)
            await asyncio.sleep(3)

    @commands.command(name='poll', help='create a poll with up to 10 inputs')
    async def poll(self, ctx, *args):
        if len(args) > 10:
            await ctx.send('Too many inputs...')
            return

        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

        em = discord.Embed(title=f'{args[0]}', color=discord.Color.dark_gold())
        # em.add_field(name='1', value=playlists['1'])
        print(args[1])
        for i in range(1, len(args)):
            em.add_field(name=f'{i}) {args[i]}', value='', inline=False)

        message = await ctx.send(embed=em)

        for i in range(0, len(args) - 1):
            await message.add_reaction(number_emojis[i])


async def setup(bot):
    await bot.add_cog(Utility(bot))






