import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command(brief="-Pings the bot, also shows latency")
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    @commands.command(brief="-Kicks a user, can include a reason")
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command(brief="-Bans a user, @the user in the command, can include a reason")
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command(brief="-Unbans a user, type out name and numbers")
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discrim = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discrim):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command(brief="-Clears chat, no more than 100 messages at a time")
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, arg):
        await ctx.channel.purge(limit=int(arg)+1)

def setup(client):
    client.add_cog(Moderation(client))