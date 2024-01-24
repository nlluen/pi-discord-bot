import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import json


def embed_info(member_id, member):
    members = get_registered_members()
    if member_id in members:
        name = members[member_id]["Name"]
        birthday = members[member_id]["Birthday"]
        dabloons = members[member_id]["Dabloons"]
        pfp = member.display_avatar
        em = discord.Embed(title=f"{member.display_name}'s Information", color=discord.Color.blue())
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

    @app_commands.command(name='register', description='register your info')
    @app_commands.guilds(752401958647890104)
    async def register(self, interaction: discord.Interaction, name: str, birthday: str):
        user_name = name.title().strip()
        user_birthday = birthday
        user_id = interaction.user.id
        #print(user_id)
        try:
            birthday_date = datetime.strptime(user_birthday, '%m/%d')
            formatted_birthday = f"{birthday_date.month}/{birthday_date.day}"
            #print(formatted_birthday)
        except ValueError:
            await interaction.response.send_message("Please input a valid calendar in the mm/dd format.")
            return

        dic = {
            "Name": user_name,
            "Birthday": formatted_birthday,
            "User_ID": user_id,
            "Dabloons": 0,
        }

        members = get_registered_members()

        if str(user_id) in members:
            await interaction.response.send_message(f'<@{user_id}> You have already registered.')
        else:
            await interaction.response.send_message(f'<@{user_id}> Thank you for registering!')
            members[user_id] = dic
            update_registered_members(members)

    @app_commands.command(name='unregister', description='unregister your info')
    @app_commands.guilds(752401958647890104)
    async def unregister(self, interaction: discord.Interaction):
        members = get_registered_members()
        user_id = str(interaction.user.id)
        if user_id in members:
            del members[user_id]
            await interaction.response.send_message(f"<@{user_id}> You have successfully unregistered.")
            update_registered_members(members)
        else:
            await interaction.response.send_message(f"<@{user_id}> Try registering first.")

    @app_commands.command(name='info', description='display your info')
    @app_commands.guilds(752401958647890104)
    async def info(self, interaction: discord.Interaction, user: discord.User = None):
        if user is None:
            member_id = str(interaction.user.id)
            member = interaction.user
        else:
            member_id = str(user.id)
            member = user
        em = embed_info(member_id, member)
        await interaction.response.send_message(embed=em)

    @app_commands.command(name='av', description="display your or someone else's profile picture")
    @app_commands.guilds(752401958647890104)
    async def av(self, interaction: discord.Interaction, user: discord.User = None):
        if user is None:
            member = interaction.user
        else:
            member = user
        pfp = member.display_avatar
        em = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.blue())
        em.set_image(url=f'{pfp}')
        await interaction.response.send_message(embed=em)

    @app_commands.command(name='birthdays', description="display all the member's birthdays or someone specific")
    @app_commands.guilds(752401958647890104)
    async def birthdays(self, interaction: discord.Interaction, user: discord.User = None):
        members = get_registered_members()

        if not members:
            await interaction.response.send_message("There are no members registered")
            return

        if user and str(user.id) in members:
            birthday = members[str(user.id)].get('Birthday')
            embed = discord.Embed(title=f"{user.display_name}'s Birthday", color=discord.Color.blue())
            embed.description = f"{birthday}"
            embed.set_thumbnail(url=f'{user.display_avatar}')
        else:
            date_format = "%m/%d"
            sorted_birthdays = dict(
                sorted(members.items(), key=lambda x: datetime.strptime(x[1]["Birthday"], date_format)))
            embed = discord.Embed(title=f"List of Birthdays - {len(sorted_birthdays)}", color=discord.Color.blue())
            for user_id, member_data in sorted_birthdays.items():
                birthday = member_data.get('Birthday')
                name = member_data.get("Name")
                if birthday and name:
                    embed.add_field(name=name, value=birthday, inline=False)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Member(bot))
