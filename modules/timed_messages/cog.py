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


    def get_work_message(self):
        message = "Happy 5 PM everyone"
        return message
        #message_list = ["Happy 5 PM everyone!"]

    def get_morning_messages(self):
            message_list = ["Good morning everyone! Have a great day :)", "Rise and grind everyone!"]
            num = random.randint(0, 1)
            message = message_list[num]
            return message

    #@commands.cooldown(1, 1, commands.BucketType.user)
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
                await gen_channel.send(morning_message)
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
                gen_channel_id = 752401958647890108
                gen_channel = self.bot.get_channel(gen_channel_id)
                if gen_channel:
                    await gen_channel.send(f"Today is <@{member_id}>'s birthday! Everyone wish them a HBD")









async def setup(bot):
    await bot.add_cog(Timed_Messages(bot))
