import discord
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='poll', help='create a poll with up to 10 inputs')
    async def poll(self, ctx, *args):
        if len(args) > 10:
            await ctx.send('Too many inputs...')
            return

        number_emojis = [1186851978760945715, 1186852036646551552]

        em = discord.Embed(title=f'{args[0]}', color=discord.Color.dark_gold())
        # em.add_field(name='1', value=playlists['1'])
        print(args[1])
        for i in range(1, len(args)):
            em.add_field(name=f'{i}) {args[i]}', value='', inline=False)

        message = await ctx.send(embed=em)

        for i in range(0, len(args) - 1):
            emote = ctx.guild.get_emoji(1186854497469861898)
            if not emote:
                print("zzz")

            await message.add_reaction(emote)


async def setup(bot):
    await bot.add_cog(Example(bot))






