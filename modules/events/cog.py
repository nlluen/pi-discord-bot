import asyncio

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
            print('ignoring message')
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
        with open('pictures/deleted.jpg', 'rb') as f:
            image = discord.File(f)
            # Send the image to the channel
            await deleted_channel.send(file=image)
        await log_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Events(bot))