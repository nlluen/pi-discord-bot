from discord.ext import commands
import json
import discord
import re
from datetime import datetime


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='register', help='register your info')
    async def register(self, ctx, *args):

        fname = args[0]
        birthday = args[1]
        month, day = map(int, args[1].split('/'))
        user_id = ctx.author.id

        if month > 12 and day > 31:
            return

        dic = {
            "fname": fname,
            "birthday": birthday,
            "user_id": user_id,
            "dabloons": 0,
        }

        with open('members.json', 'r') as rf:
            print('in here')
            members = json.load(rf)

        if str(user_id) in members:
            await ctx.send(f'<@{user_id}> You have already registered.')
        else:
            await ctx.send(f'<@{user_id}> Thank you for registering!')
            members[user_id] = dic
            with open('members.json', "w") as file:
                json.dump(members, file)

    def display_info(self, member_id, member):
        with open('members.json', 'r') as rf:
            members = json.load(rf)

        if member_id in members:
            fname = members[member_id]["fname"]
            birthday = members[member_id]["birthday"]
            dabloons = members[member_id]["dabloons"]
            pfp = member.display_avatar
            em = discord.Embed(title=f"{member.name}'s Information", color=discord.Color.blue())
            em.add_field(name='Name', value= fname)
            em.add_field(name='Birthday', value=birthday)
            em.add_field(name='Dabloons', value=dabloons)
            em.set_thumbnail(url=f'{pfp}')
            return em

    @commands.command(name='info', help="display your info")
    async def info(self, ctx):
        member_id = str(ctx.author.id)
        member = await self.bot.fetch_user(member_id)
        em = self.display_info(member_id, member)
        await ctx.send(embed=em)

    @commands.command(name='getinfo', help="display another person's info")
    async def getinfo(self, ctx, arg):
        member_id = re.sub(r'[<@>]', '', arg)
        member = await self.bot.fetch_user(member_id)
        em = self.display_info(member_id, member)
        await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(Member(bot))
