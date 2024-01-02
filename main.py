import asyncio
import os
import discord
from discord.ext import commands


class CustomHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()

    async def send_command_help(self, command):
        ctx = self.context
        embed = discord.Embed(
            title=f"{command.name}",
            description=command.help or "No help available.",
            color=discord.Color.blue()
        )

        # Add usage information
        usage = self.get_command_signature(command)
        embed.add_field(name="Usage", value=f"`{usage}`", inline=False)
        await ctx.send(embed=embed)


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents, help_command=CustomHelpCommand())
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
