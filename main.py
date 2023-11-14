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

#
# @bot.event
# async def on_message_delete(message):
#     # Check that the message was not sent by a bot to avoid logging bot actions
#     if message.author == bot.user:
#         return
#
#     channel_id = message.channel.id
#     mod_log_id = 762824517654937631
#     log_channel = bot.get_channel(mod_log_id)
#     deleted_channel = bot.get_channel(channel_id)
#     # Log the deleted message to a file or database
#     embed = discord.Embed(title=f"{message.author.name}#{message.author.discriminator}",  color=0xff0000)
#     embed.add_field(name=f'Message was deleted in {message.channel.mention}', value=message.content)
#     with open('pictures/deleted.jpg', 'rb') as f:
#         image = discord.File(f)
#         # Send the image to the channel
#         await deleted_channel.send(file=image)
#     await log_channel.send(embed=embed)


@bot.command(name='ping', help='Sends jotchua :)')
async def ping(ctx):
    await ctx.send('<:jotchua:992580804188319824>')


@bot.command(name='stop', help='stops bot')
async def stop(ctx):
    await bot.get_channel(1045937547597053982).send("I am getting very sleepy...why is it all turning black...")
    await bot.close()


# async def load():
#     for folder in os.listdir('modules'):
#         if os.path.exists(os.path.join('modules', folder, 'cog.py')):
#             await bot.load_extension(f'modules.{folder}.cog')


async def main():
    #await load()
    await bot.start(os.environ['TOKEN'])
    #await bot.start('')
asyncio.run(main())