import discord
from discord.ext import commands
from datetime import datetime
import time as ti

class Timer(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="Timer", brief="-Creates a countdown and replies to the user when it finishes.", aliases=["timer", "countdown", "tmr", "ctd"])
    async def timer(self, ctx, arg):
        testt = await ctx.message.channel.send("‎‏‏‎‎")
        countdown = int(arg)
        while countdown >= 0:
            mins, secs = divmod(countdown, 60)
            tmr = '{:02d}:{:02d}'.format(mins, secs)
            await testt.edit(content=tmr)
            print(tmr, end="\r")
            ti.sleep(1)
            countdown -= 1
            
        await ctx.channel.purge(limit=1)
        await ctx.message.reply('Its time', mention_author=True)

def setup(client):
    client.add_cog(Timer(client))