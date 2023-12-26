import asyncio
import random
import discord
from discord.ext import commands
import time


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role('Untitled', 'The Godfather')
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

    @commands.cooldown(1, 1, commands.BucketType.user)
    @commands.command(name='flip', help='Flip a coin to make your basic life choices')
    async def flip(self, ctx):
        HoT = random.randint(0, 1)
        if HoT:
            await ctx.send(f'<@{ctx.message.author.id}> Heads!')
        else:
            await ctx.send(f'<@{ctx.message.author.id}> Tails!')

    @commands.command(name='flip2', help='Flip a coin and bet on which side it lands')
    async def flip2(self, ctx):
        await ctx.send('Coin is flipping in the air! Call it!')
        time.sleep(3.0)

        def check(m):
            return (m.content.lower() == 'heads' or m.content.lower() == 'tails') and m.author == ctx.author
        try:
            message = await self.bot.wait_for('message', timeout=0.5, check=check)
        except asyncio.TimeoutError:
            await ctx.send('There are only two sides to a coin ... and that is not one of them! Try again.')
        else:
            print(message.content)
            HoT = random.randint(0, 1)
            print(HoT)
            if HoT:
                side = 'HEADS'
            else:
                side = 'TAILS'

            if side == message.content.upper():
                await ctx.send(f'landed on {side}! You were correct!')
            else:
                await ctx.send(f'landed on {side}! You were wrong!')


async def setup(bot):
    await bot.add_cog(Utility(bot))






