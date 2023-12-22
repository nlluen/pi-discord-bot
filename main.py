import asyncio
import os
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)
client = discord.Client(intents=intents)


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="The Degenerates of this Server")
    await bot.change_presence(activity=activity)
    #await bot.change_presence(activity=discord.Game("League Of Legends"))
    #await bot.get_channel(1045937547597053982).send("I'm back and capable of being awake 24/7.");
    print("Bot is ready")


@bot.command(name='ping', help='Sends jotchua :)')
async def ping(ctx):
    await ctx.send('<:jotchua:992580804188319824>')


@bot.command(name='stop', help='stops bot')
async def stop(ctx):
    allowed_role = discord.utils.get(ctx.guild.roles, name="The Godfather")
    if allowed_role in ctx.author.roles:
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
