import discord
import os
from discord.ext import commands
import discord_token

client = commands.Bot(command_prefix='.')
intents = discord.Intents.all()

@client.command(brief="-Cogs: clock, moderation, music")
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Loaded')

@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Unloaded')

@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        pass
#        client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == "__main__":
    client.run(discord_token.TOKEN)