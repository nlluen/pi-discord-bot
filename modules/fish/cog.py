import asyncio
import json
import time
import random
import re


import discord
from discord.ext import commands

spawn = 0
start_time = 0
end_time = 0
fished = False
class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.set_fish_data()
        print("on ready in fish")

    # async def spawn(self):
    #     global spawn
    #     global start_time
    #     global fished
    #     fished = False
    #     start_time = time.time()
    #     spawn = random.randint(1, 50)
    #     return spawn
    #
    # @commands.cooldown(1, 1.5, commands.BucketType.user)
    # @commands.group(name='fish', help='spawn in a fish', invoke_without_command=True)
    # async def fish(self, ctx):
    #     spawn = await self.spawn()
    #
    #     if spawn == 50:
    #         await ctx.send("Legendary Fish")
    #         await ctx.send(':whale:')
    #     elif 47 < spawn < 50:
    #         await ctx.send("Epic Fish")
    #         await ctx.send(':seal:')
    #     elif 43 < spawn <= 47:
    #         await ctx.send("Very Rare Fish")
    #         await ctx.send(':shark:')
    #     elif 36 < spawn <= 43:
    #         await ctx.send("Rare Fish")
    #         await ctx.send(':tropical_fish:')
    #     else:
    #         await ctx.send("Common Fish")
    #         await ctx.send(':fish:')
    #
    # @commands.cooldown(1, 1.5, commands.BucketType.guild)
    # @fish.command(name='c', help='attempt to catch the fish')
    # async def c(self, ctx):
    #     global fished
    #     global end_time
    #     end_time = time.time()
    #     total_time = end_time - start_time
    #     if total_time > 10:
    #         await ctx.send('You took too long! The fish is gone. Try again.')
    #         return
    #     if fished:
    #         await ctx.send('Fish has already been caught!')
    #         return
    #
    #     await ctx.send('You throw your rod...')
    #     time.sleep(1)
    #     chance = random.randint(0, 1)
    #     if chance:
    #         if spawn == 50:
    #             await ctx.send(f"{ctx.author.name} caught the Legendary Fish! They've earned 50 dabloons!")
    #             await self.update_fish(ctx.author.id, 50)
    #         elif 47 < spawn < 50:
    #             await ctx.send(f"{ctx.author.name} caught the Epic Fish! They've earned 15 dabloons!")
    #             await self.update_fish(ctx.author.id, 15)
    #         elif 43 < spawn <= 47:
    #             await ctx.send(f"{ctx.author.name} caught a Very Rare Fish! They've earned 10 dabloons!")
    #             await self.update_fish(ctx.author.id, 10)
    #         elif 36 < spawn <= 43:
    #             await ctx.send(f"{ctx.author.name} caught a Rare Fish! They've earned 5 dabloons!")
    #             await self.update_fish(ctx.author.id, 5)
    #         else:
    #             await ctx.send(f"{ctx.author.name} caught a Common Fish! They've earned 1 dabloon!")
    #             await self.update_fish(ctx.author.id, 1)
    #         fished = True
    #     else:
    #         await ctx.send("The fish swam away! Better luck next time :o")
    #

    #
    # async def get_fish_data(self):
    #     with open('fishdata.json', 'r') as rf:
    #         users = json.load(rf)
    #     return users
    #
    # async def set_fish_data(self):
    #     h = self.bot.get_cog('Start')
    #     member_list = await h.active_members()
    #
    #     for member in member_list:
    #         users = await self.get_fish_data()
    #         if str(member.id) not in users:
    #             users[str(member.id)] = {}
    #             users[str(member.id)]['Dabloons'] = 0
    #
    #         with open('fishdata.json', 'w') as wf:
    #             json.dump(users, wf)
    #
    # async def update_fish(self, member, amount):
    #     print('updating fish')
    #     dabloon_amt = amount
    #     users = await self.get_fish_data()
    #     users[str(member)]['Dabloons'] += dabloon_amt
    #
    #     with open('fishdata.json', 'w') as wf:
    #         json.dump(users, wf)


async def setup(bot):
    await bot.add_cog(Fish(bot))
