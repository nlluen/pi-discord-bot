import asyncio
import json
import time
import random

import discord
import re
from discord.ext import commands


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gamble', help='gamble ur life savings away')
    async def gamble(self, ctx):
        res1 = random.randint(0, 10)
        res2 = random.randint(0, 10)
        res3 = random.randint(0, 10)
        if int < 10:
            await ctx.send('X')
            time.sleep(1.0)
        else:
            await ctx.send('O')


    @commands.command(name='balance', help='lists the dabloons you have')
    async def balance(self, ctx):
        h = self.bot.get_cog('Fish')
        users = await h.get_fish_data()
        if str(ctx.message.author.id) in users:
            dabloon_amt = users[str(ctx.message.author.id)]['Dabloons']
            pfp = ctx.message.author.display_avatar
            em = discord.Embed(title=f"{ctx.author.name}'s Balance", color=discord.Color.blue())
            em.add_field(name='Dabloons', value=dabloon_amt)
            em.set_thumbnail(url=f'{pfp}')
            await ctx.send(embed=em)

    @commands.command(name='b', help='lists the dabloons you have')
    async def b(self, ctx, arg):
        id = re.sub(r'[<@>]', '', arg)
        x = self.bot.get_cog('Fish')
        users = await x.get_fish_data()
        h = self.bot.get_cog('Start')
        member_list = await h.active_members()
        for member in member_list:
            # print(member.id)
            # print(f'this is id: {id}')
            if id == str(member.id):
                person = member

        if str(id) in users:
            dabloon_amt = users[str(id)]['Dabloons']
            pfp = person.display_avatar
            em = discord.Embed(title=f"{person.name}'s Balance", color=discord.Color.blue())
            em.add_field(name='Dabloons', value=dabloon_amt)
            em.set_thumbnail(url=f'{pfp}')
            await ctx.send(embed=em)

    @commands.command(name='give', help='give your dabloons')
    async def give(self, ctx, arg):
        id = re.sub(r'[<@>]', '', arg)
        await ctx.send('How much do you wish to trade?')
        def check(m):
            print('i go here')
            return m.author == ctx.author
        try:
            print('i here')
            message = await self.bot.wait_for('message', timeout=3, check=check)
            dabloon_amt = int(message.content)
        except asyncio.TimeoutError:
            await ctx.send('This is not a valid dabloon value!')
        else:
            if (dabloon_amt <= 0):

                return

            print('in here!')
            x = self.bot.get_cog('Fish')
            users = await x.get_fish_data()
            user_dabloon = users[str(ctx.message.author.id)]['Dabloons']
            print(user_dabloon)
            print(dabloon_amt)
            if user_dabloon >= dabloon_amt:
                await ctx.send(f'You have given {dabloon_amt} dabloons to {arg}')
                users[str(ctx.message.author.id)]['Dabloons'] -= dabloon_amt
                users[str(id)]['Dabloons'] += dabloon_amt
            else:
                await ctx.send("You do not have enough dabloons to make this trade!")

            with open('fishdata.json', 'w') as wf:
                json.dump(users, wf)


async def setup(bot):
    await bot.add_cog(Economy(bot))
