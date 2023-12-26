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
            members = json.load(rf)

        if str(user_id) in members:
            await ctx.send(f'<@{user_id}> You have already registered.')
        else:
            await ctx.send(f'<@{user_id}> Thank you for registering!')
            members[user_id] = dic
            with open('members.json', "w") as file:
                json.dump(members, file)

    def embed_info(self, member_id, member):
        with open('members.json', 'r') as rf:
            members = json.load(rf)

        if member_id in members:

            fname = members[member_id]["fname"]
            birthday = members[member_id]["birthday"]
            dabloons = members[member_id]["dabloons"]
            pfp = member.display_avatar
            em = discord.Embed(title=f"{member.nick}'s Information", color=discord.Color.blue())
            print('here')
            em.add_field(name='Name', value=fname, inline=True)
            em.add_field(name='Birthday', value=birthday, inline=True)
            em.add_field(name='Dabloons', value=dabloons, inline=False)
            em.add_field(name='Server Join Date', value=member.joined_at.strftime('%m/%d/%Y at %H:%M:%S'), inline=False)
            em.set_thumbnail(url=f'{pfp}')
            #em.set_footer(text="footer")
            return em

    @commands.command(name='info', help="display your info")
    async def info(self, ctx, user: discord.User = None):
        server_id = 752401958647890104
        if user is None:
            member_id = str(ctx.author.id)
            member = ctx.author
        else:
            member_id = str(user.id)
            member = self.bot.get_guild(server_id).get_member(int(member_id))
            print(member_id)
            print(member)

        em = self.embed_info(member_id, member)
        await ctx.send(embed=em)

    # @commands.command(name='getinfo', help="display another person's info")
    # async def getinfo(self, ctx, arg):
    #     member_id = re.sub(r'[<@>]', '', arg)
    #     server_id = 752401958647890104
    #     member = self.bot.get_guild(server_id).get_member(int (member_id))
    #     em = self.embed_info(member_id, member)
    #     await ctx.send(embed=em)

    @commands.command(name='av', help="display your profile picture")
    async def av(self, ctx, user: discord.User = None):
        server_id = 752401958647890104
        if user is None:
            member = ctx.message.author
            pfp = ctx.message.author.display_avatar
        else:
            pfp = user.display_avatar
            member = self.bot.get_guild(server_id).get_member(user.id)
        em = discord.Embed(title=f"{member.nick}'s Avatar", color=discord.Color.blue())
        em.set_image(url=f'{pfp}')
        await ctx.send(embed=em)


async def setup(bot):
    await bot.add_cog(Member(bot))
