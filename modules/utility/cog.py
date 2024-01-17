import discord
from discord.ext import commands
from discord import app_commands
import time
import asyncio
import random


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.has_any_role('Untitled', 'The Godfather')
    @commands.command(name='purge', help='purge x amount of message')
    async def purge(self, ctx, arg: int):
        if arg < 15:
            await ctx.channel.purge(limit=arg+1)
            await asyncio.sleep(3)

    @app_commands.command(name='poll', description='create a poll with up to 10 inputs',)
    @app_commands.guilds(752401958647890104)
    async def poll(self, interaction: discord.Interaction, title: str, option1: str, option2: str, option3: str=None, option4: str=None, option5: str=None, option6: str=None, option7: str=None, option8: str=None, option9: str=None, option10: str=None):
        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        options = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10]
        valid_options = [option for option in options if option is not None]
        embed = discord.Embed(title=title, color=discord.Color.dark_gold())

        for i, option in enumerate(valid_options):
            embed.add_field(name=f'{i+1}) {option}', value='', inline=False)

        await interaction.response.send_message(embed=embed)

        original_response = await interaction.original_response()

        for i in range(len(valid_options)):
            await original_response.add_reaction(number_emojis[i])

    @app_commands.command(name='flip', description='Flip a coin to make your basic life choices')
    @app_commands.guilds(752401958647890104)
    # @commands.cooldown(1, 1, commands.BucketType.user)
    # @commands.command(name='flip', help='Flip a coin to make your basic life choices and guess the outcome')
    async def flip(self, interaction: discord.Interaction, guess: str=None):
        HoT = random.randint(0, 1)


        if guess is not None:
            guess = guess.lower()
            if HoT:
                side = 'Heads'
            else:
                side = 'Tails'

            if guess == side.lower():
                await interaction.response.send_message(f"You were correct! It was {side}")
            else:
                await interaction.response.send_message(f"You were wrong! It was {side}")

        if HoT:
            await interaction.response.send_message("Heads!")
        else:
            await interaction.response.send_message("Tails!")

    @app_commands.command(name='addrole', description='Give yourself a role')
    @app_commands.guilds(752401958647890104)
    # @commands.cooldown(1, 1, commands.BucketType.user)
    # @commands.command(name='flip', help='Flip a coin to make your basic life choices and guess the outcome')
    async def addrole(self, interaction: discord.Interaction, role: discord.Role):
        roles = interaction.user.roles
        print(roles)
        print(role)
        restricted_roles = ["Men", "Untitled", "Champion Of Halloween", "The Godfather", "The Godmother", "The Godson", "ECE", "Hall Of Shame"]
        if role not in roles and role.name not in restricted_roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"You have been given the *{role}* role")
        elif role in roles:
            await interaction.response.send_message("You already have this role!")
        else:
            await interaction.response.send_message("Sorry but you cannot access that role!")

    @app_commands.command(name='removerole', description='Remove a role')
    @app_commands.guilds(752401958647890104)
    # @commands.cooldown(1, 1, commands.BucketType.user)
    # @commands.command(name='flip', help='Flip a coin to make your basic life choices and guess the outcome')
    async def removerole(self, interaction: discord.Interaction, role: discord.Role):
        roles = interaction.user.roles
        if role in roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Successfully removed the {role} role!")
        else:
            await interaction.response.send_message("You cannot remove a role you do not have!")


    #
    # @app_commands.command(name='flip2', description='Flip a coin and bet on which side it lands')
    # @app_commands.guilds(752401958647890104)
    # async def flip2(self, interaction: discord.Interaction):
    #     await interaction.response.send_message('Coin is flipping in the air! Call it!')
    #     time.sleep(3.0)
    #
    #     def check(m):
    #         return (m.content.lower() == 'heads' or m.content.lower() == 'tails') and m.author == ctx.author
    #     try:
    #         message = await self.bot.wait_for('message', timeout=0.5, check=check)
    #     except asyncio.TimeoutError:
    #         await ctx.send('There are only two sides to a coin ... and that is not one of them! Try again.')
    #     else:
    #         print(message.content)
    #         HoT = random.randint(0, 1)
    #         print(HoT)
    #         if HoT:
    #             side = 'HEADS'
    #         else:
    #             side = 'TAILS'
    #
    #         if side == message.content.upper():
    #             await ctx.send(f'landed on {side}! You were correct!')
    #         else:
    #             await ctx.send(f'landed on {side}! You were wrong!')


async def setup(bot):
    await bot.add_cog(Utility(bot))






