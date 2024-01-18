import asyncio
import datetime

import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        gifs = self.bot.get_cog("Gifs")
        ignore_message = gifs.get_ignore_message()

        if ignore_message:
            return

        if message.author == self.bot.user:
            return

        channel_id = message.channel.id
        mod_log_id = 762824517654937631
        log_channel = self.bot.get_channel(mod_log_id)
        deleted_channel = self.bot.get_channel(channel_id)
        # Log the deleted message to a file or database
        embed = discord.Embed(title=f"{message.author.name}", color=0xff0000)
        embed.add_field(name=f'Message was deleted in {message.channel.mention}', value=f'*{message.content}*')
        embed.set_footer(text=message.created_at.strftime('%m/%d/%Y at %I:%M:%S %p')) #I is for Hour on 12 hour clock and %p is for AM/PM
        # with open('pictures/deleted.jpg', 'rb') as f:
        #     image = discord.File(f)
        #     # Send the image to the channel
        #     await deleted_channel.send(file=image)
        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel_id = before.channel.id
        mod_log_id = 762824517654937631
        log_channel = self.bot.get_channel(mod_log_id)
        deleted_channel = self.bot.get_channel(channel_id)
        embed = discord.Embed(title=f"{before.author.name}", color=0xff0000)
        embed.add_field(name=f'Message was edited in {before.channel.mention}', value=f'\n[Jump to Message]({before.jump_url})', inline=False)
        embed.add_field(name='Before', value=f'*{before.content}*', inline=False)
        embed.add_field(name='After', value=f'*{after.content}*', inline=False)
        embed.set_footer(text=after.created_at.strftime('%m/%d/%Y at %I:%M:%S %p'))  # I is for Hour on 12 hour clock and %p is for AM/PM
        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel_id = 752414419358711849
        welcome_channel = self.bot.get_channel(welcome_channel_id)

        if welcome_channel:
            await welcome_channel.send(f"Welcome to the Degenerates of RU'23, {member.mention}. Have fun, be nice, and be a degenerate")

    @commands.Cog.listener()
    async def on_voice_state_update(self, user, before, after):
        current_time = datetime.datetime.now().strftime('%m/%d/%Y at %I:%M:%S %p')
        mod_log_id = 762824517654937631
        log_channel = self.bot.get_channel(mod_log_id)

        embed = discord.Embed(title=user, color=discord.Color.dark_gold())
        embed.set_footer(text=current_time)
        # embed.set_image(url=f'{user.display_avatar}')
        if before.channel is None and after.channel is not None:
            embed.description = f'{user.display_name} joined {after.channel.name}'

            await log_channel.send(embed=embed)
            print(f'{user.display_name} joined {after.channel.name}')
            # Add your custom logic here

            # Check if the user left a voice channel
        elif before.channel is not None and after.channel is None:
            embed.description = f'{user.display_name} left {before.channel.name}'
            await log_channel.send(embed=embed)
            print(f'{user.display_name} left {before.channel.name}')
            # Add your custom logic here

            # Check if the user switched voice channels
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            embed.description = f'{user.display_name} switched from {before.channel.name} to {after.channel.name}'
            await log_channel.send(embed=embed)
            print(f'{user.display_name} switched from {before.channel.name} to {after.channel.name}')


async def setup(bot):
    await bot.add_cog(Events(bot))