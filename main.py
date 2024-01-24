import discord
from discord.ext import commands
from discord import Interaction
import asyncio
import os

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="The Degenerates of this Server")
    await bot.change_presence(activity=activity)
    synced = await bot.tree.sync(guild=discord.Object(id=752401958647890104))
    print("Bot is ready")
    print(len(synced))


@bot.tree.command(name='ping', description='Sends jotchua!', guild=discord.Object(id=752401958647890104))
async def ping(interaction: Interaction):
    await interaction.response.send_message("<:jotchua:992580804188319824>")


@bot.tree.command(name='example', description='g', guild=discord.Object(id=752401958647890104))
async def example(interaction: Interaction, message1: str) -> None:
    await interaction.response.send_message(message1)


@bot.command(name='stop', help='stops bot')
async def stop(ctx):
    allowed_role1 = discord.utils.get(ctx.guild.roles, name="The Godfather")
    allowed_role2 = discord.utils.get(ctx.guild.roles, name="Untitled")
    if allowed_role1 or allowed_role2 in ctx.author.roles:
        await bot.get_channel(1045937547597053982).send("I am getting very sleepy...why is it all turning black...")
        await bot.close()


async def load():
    for folder in os.listdir('modules'):
        if os.path.exists(os.path.join('modules', folder, 'cog.py')):
            await bot.load_extension(f'modules.{folder}.cog')


async def main():
    await load()
    await bot.start(os.environ['TOKEN'])
asyncio.run(main())
