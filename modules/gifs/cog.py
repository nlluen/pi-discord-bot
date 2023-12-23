from discord.ext import commands
ignore_message_delete = False

class Gifs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_ignore_message(self):
        global ignore_message_delete
        return ignore_message_delete

    def set_ignore_message(self, ignore_message: bool):
        global ignore_message_delete
        ignore_message_delete = ignore_message

    @commands.command(name='squidward', help='Sends the squidward glass shatter gif')
    async def squidward(self, ctx):
        self.set_ignore_message(True)
        try:
            await ctx.message.delete()
            await ctx.send('https://tenor.com/view/squidward-tonight-glass-break-kinemaster-gif-22142436')
        finally:
            self.set_ignore_message(False)

    @commands.command(name='nerd', help='Sends a nerd gif')
    async def nerd(self, ctx):
        self.set_ignore_message(True)
        try:
            await ctx.message.delete()
            await ctx.send('https://tenor.com/view/nerd-emoji-nerd-emoji-avalon-play-avalon-gif-24241051')
        finally:
            self.set_ignore_message(False)

    @commands.command(name='grind', help='the grind starts')
    async def grind(self, ctx):
        self.set_ignore_message(True)
        try:
            await ctx.message.delete()
            await ctx.send('https://cdn.discordapp.com/attachments/752401958647890108/1079994924906324089/Screenshot_20220713-163149_YouTube.jpg')
        finally:
            self.set_ignore_message(False)


async def setup(bot):
    await bot.add_cog(Gifs(bot))