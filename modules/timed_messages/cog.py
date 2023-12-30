import discord
from discord.ext import commands, tasks
import datetime
import random
import json

class Timed_Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_messages.start()
        self.birthday_messages.start()
        self.water_reminder.start()

    def get_work_message(self):
        message = "Happy 5 PM everyone"
        return message
        # message_list = ["Happy 5 PM everyone!"]

    def get_morning_messages(self):
        message_list = ["Good morning everyone! Have a great day :)", "Rise and grind everyone!"]
        num = random.randint(0, 1)
        message = message_list[num]
        return message

    # @commands.cooldown(1, 1, commands.BucketType.user)
    @tasks.loop(seconds=60)
    async def daily_messages(self):
        date = datetime.datetime.now()
        gen_channel_id = 752401958647890108
        gen_channel = self.bot.get_channel(gen_channel_id)
        if gen_channel:
            # print("I work :)")
            hour = date.hour
            minute = date.minute
            if hour == 8 and minute == 00:
                morning_message = self.get_morning_messages()
                await gen_channel.send(date.strftime(f"{morning_message} Today is %B %d, %Y"))
            if hour == 16 and minute == 20:
                await gen_channel.send("420")
            if hour == 17 and minute == 00:
                work_message = self.get_work_message()
                await gen_channel.send(work_message)
            if hour == 23 and minute == 11:
                await gen_channel.send("11:11 make a wish")
            if hour == 23 and minute == 30:
                await gen_channel.send("Getting sleepy... Goodnight everyone see you all tomorrow. Sweet dreams :)")
        else:
            print('no work')

    @tasks.loop(seconds=60)
    async def birthday_messages(self):
        date = datetime.datetime.now()
        todays_month = date.month
        todays_day = date.day
        with open('members.json', 'r') as rf:
            members = json.load(rf)
        for member_id in members:
            birthday_month, birthday_day = map(int, members[member_id]["birthday"].split('/'))
            if todays_month == birthday_month and todays_day == birthday_day:
                if date.hour == 00 and date.minute == 10:
                    gen_channel_id = 752401958647890108
                    gen_channel = self.bot.get_channel(gen_channel_id)
                    if gen_channel:
                        server_id = 752401958647890104
                        member = self.bot.get_guild(server_id).get_member(members[member_id]["user_id"])
                        print(member)
                        em = discord.Embed(title="Happy Birthday", color=discord.Color.blue())
                        em.description = f"Today is <@{member_id}>'s birthday! Everyone wish them a a happy birthday :D"
                        # em.add_field(f"Today is <@{member_id}>'s birthday! Everyone wish them a happy birthday :D")
                        pfp = member.display_avatar
                        em.set_thumbnail(url=f'{pfp}')
                        await gen_channel.send(embed=em)

    # pooja's water reminder
    @tasks.loop(minutes=60)
    async def water_reminder(self):
        print('i work')
        # water_messages = ["It's time to dink your oiter! Remember to stay hydrated :)",
        #                   "You must be parched, dink some oiter!",
        #                   "Water you waiting for? Dink up some oiter!",
        #                   "Pour decisions are the ones without oiter. Hydrate wisely!",
        #                   "Sip, sip, hooray! It's oiter time!",
        #                   "You shore could use a dink right now! What about some oiter?",
        #                   "Hydrate to feel great!",
        #                   "DINK MORE OITER NOW!",
        #                   "Oiter is the solution to so many problems, dink some!",
        #                   "You're mostly made of oiter so dink some!",
        #                   "Stay hydrated and dink some oiter right now!",
        #                   "Dink oiter for clear skin and a better gut :D"]
        # server_id = 752401958647890104
        # date = datetime.datetime.now()
        # if 10 <= date.hour <= 23:
        #     server = self.bot.get_guild(server_id)
        #     if not server:
        #         return
        #     user = server.get_member(1184993798875512894)
        #     num = random.randint(0, 11)
        #     await user.send(water_messages[num])

    @birthday_messages.before_loop
    @daily_messages.before_loop
    @water_reminder.before_loop
    async def before_water_reminder(self):
        await self.bot.wait_until_ready()


async def setup(bot):
    await bot.add_cog(Timed_Messages(bot))
