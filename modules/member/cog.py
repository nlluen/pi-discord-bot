from discord.ext import commands
import json
import discord
import re
from datetime import datetime


def embed_info(member_id, member):
    members = get_registered_members()

    if member_id in members:
        name = members[member_id]["Name"]
        birthday = members[member_id]["Birthday"]
        dabloons = members[member_id]["Dabloons"]
        pfp = member.display_avatar
        em = discord.Embed(title=f"{member.nick}'s Information", color=discord.Color.blue())
        em.add_field(name='Name', value=name, inline=True)
        em.add_field(name='Birthday', value=birthday, inline=True)
        em.add_field(name='Dabloons', value=dabloons, inline=False)
        em.add_field(name='Server Join Date', value=member.joined_at.strftime('%m/%d/%Y at %H:%M:%S'), inline=False)
        em.set_thumbnail(url=f'{pfp}')
        # em.set_footer(text="footer")
        return em


def get_registered_members():
    with open('members.json', 'r') as rf:
        members = json.load(rf)
    return members


def update_registered_members(members):
    with open('members.json', "w") as file:
        json.dump(members, file)


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='register', help='register your info', usage='<argument1> [optional_argument2]')
    async def register(self, ctx, *args):
        name = args[0]
        birthday = args[1]
        user_id = ctx.author.id

        try:
            birthday_date = datetime.strptime(birthday, '%m/%d')
            formatted_birthday = f"{birthday_date.month}/{birthday_date.day}"
        except ValueError:
            await ctx.send("Please input a valid calendar in the mm/dd format.")
            return

        dic = {
            "Name": name,
            "Birthday": formatted_birthday,
            "User_ID": user_id,
            "Dabloons": 0,
        }

        members = get_registered_members()

        if str(user_id) in members:
            await ctx.send(f'<@{user_id}> You have already registered.')
        else:
            await ctx.send(f'<@{user_id}> Thank you for registering!')
            members[user_id] = dic
            update_registered_members(members)

    @commands.command(name='unregister', help='unregister your info')
    async def unregister(self, ctx):
        members = get_registered_members()
        user_id = str(ctx.author.id)
        if user_id in members:
            del members[user_id]
            await ctx.send("You have successfully unregistered.")
            update_registered_members(members)
        else:
            await ctx.send("Try registering first.")

    @commands.command(name='info', help="display your info", usage='<user>')
    async def info(self, ctx, user: discord.User = None):
        server_id = 752401958647890104
        if user is None:
            member_id = str(ctx.author.id)
            member = ctx.author
        else:
            member_id = str(user.id)
            member = self.bot.get_guild(server_id).get_member(int(member_id))

        em = embed_info(member_id, member)
        await ctx.send(embed=em)

    @commands.command(name='av', help="display your profile picture")
    async def av(self, ctx, user: discord.User = None):
        server_id = 752401958647890104
        if user is None:
            member = ctx.message.author
            pfp = ctx.message.author.display_avatar
        else:
            pfp = user.display_avatar
            member = self.bot.get_guild(server_id).get_member(user.id)
        em = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.blue())
        em.set_image(url=f'{pfp}')
        await ctx.send(embed=em)

    @commands.command(name='birthdays', help='list of birthdays')
    async def birthdays(self, ctx):
        members = get_registered_members()

        if not members:
            await ctx.send("There are no members registered")
            return

        date_format = "%m/%d"
        sorted_birthdays = dict(sorted(members.items(), key=lambda x: datetime.strptime(x[1]["Birthday"], date_format)))
        embed = discord.Embed(title=f"List of Birthdays - {len(sorted_birthdays)}", color=discord.Color.blue())
        for user_id, member_data in sorted_birthdays.items():
            birthday = member_data.get('Birthday')
            name = member_data.get("Name")
            if birthday and name:
                embed.add_field(name=name, value=birthday, inline=False)
        await ctx.send(embed=embed)




async def setup(bot):
    await bot.add_cog(Member(bot))
