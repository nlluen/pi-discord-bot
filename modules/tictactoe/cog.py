import discord
from discord.ext import commands
from discord import app_commands
import time
import asyncio
import random


class TictactoeButtons(discord.ui.View):
    def __init__(self, player1, player2: discord.Member, current_player: discord.Member):
        super().__init__()
        self.player1 = player1
        self.player2 = player2
        self.current_player = current_player
        self.board = ["-" for _ in range(9)]

    def make_move(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user == self.current_player:
            if interaction.user == self.player1:
                button.label = "X"
                button.style = discord.ButtonStyle.red
                self.current_player = self.player2
            else:
                button.label = "O"
                button.style = discord.ButtonStyle.blurple
                self.current_player = self.player1
            button.disabled = True

    def check_winner(self):
        winning_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]  # diagonal
        ]

        for positions in winning_positions:
            if self.board[positions[0]] == self.board[positions[1]] == self.board[positions[2]] == "X":
                return self.player1
            elif self.board[positions[0]] == self.board[positions[1]] == self.board[positions[2]] == "O":
                return self.player2
        return None

    async def winner_confirmed(self, interaction: discord.Interaction):
        winner = self.check_winner()
        if winner is None:
            return
        for child in self.children:
            child.disabled = True
        await interaction.channel.send(f"{winner.mention} wins!")

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=1, custom_id="1")
    async def button1_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[0] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=1)
    async def button1_2(self, interaction: discord.Interaction, button: discord.ui.Button,):
        self.make_move(interaction, button)
        self.board[1] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=1)
    async def button1_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[2] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=2)
    async def button2_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[3] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=2)
    async def button2_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[4] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=2)
    async def button2_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[5] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=3)
    async def button3_1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[6] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=3)
    async def button3_2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[7] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='-', style=discord.ButtonStyle.grey, row=3)
    async def button3_3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.make_move(interaction, button)
        self.board[8] = button.label
        await self.winner_confirmed(interaction)
        await interaction.response.edit_message(view=self)


class Tictactoe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='tictactoe', description='initiate a tic tac toe battle!')
    @app_commands.guilds(752401958647890104)
    async def tictactoe(self, interaction: discord.Interaction, player2: discord.Member):
        player1 = interaction.user
        rand = random.randint(0, 1)
        if rand:
            current_player = player1
        else:
            current_player = player2
        await interaction.response.send_message(f"{player2.mention} do you accept the challenge?")
        original_response = await interaction.original_response()
        await original_response.add_reaction("⚔")

        def player2_accept_check(reaction, user):
            return user == player2 and str(reaction.emoji) == "⚔"

        try:
            reaction, _ = await self.bot.wait_for("reaction_add", timeout=60, check=player2_accept_check)
            await interaction.channel.send(f"Let us begin! {current_player.mention} you are first!")
            view = TictactoeButtons(player1=player1, player2=player2, current_player=current_player)
            await interaction.channel.send(content=f"Tic Tac Toe Battle: {player1.display_name} VS {player2.display_name}", view=view)
        except asyncio.TimeoutError:
            await interaction.channel.send(f"Guess {player2.mention} was not feeling it today!")


async def setup(bot):
    await bot.add_cog(Tictactoe(bot))






