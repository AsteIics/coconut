import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$', intents = discord.Intents.all())
member_count = sum([len([m for m in g.members if not m.bot]) for g in client.guilds])

@client.command()
async def load(ctx, extension):
    embedVar = discord.Embed(title="**DEVELOPER**", description="client.load_extension(f'cogs.{extension}'", color=7419530)
    embedVar.add_field(name="**PARSED**", value=f"Loaded cog {extension}")
    embedVar1 = discord.Embed(title='**DEVELOPER**', description='Error occured:\n commands.MissingPermissions', color=7419530)
    embedVar1.add_field(name='**NOT PARSED**', value='Missing required permissions.')

    if ctx.message.author.id == 445271451159887889:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(embed=embedVar)
    else:
        await ctx.send(embed=embedVar1)

@client.command()
async def unload(ctx, extension):
    embedVar = discord.Embed(title="**DEVELOPER**", description="client.unload_extension(f'cogs.{extension}'", color=7419530)
    embedVar.add_field(name="**PARSED**", value=f"Unloaded cog {extension}")
    embedVar1 = discord.Embed(title='**DEVELOPER**', description='Error occured:\n commands.MissingPermissions', color=7419530)
    embedVar1.add_field(name='**NOT PARSED**', value='Missing required permissions.')

    if ctx.message.author.id == 445271451159887889:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(embed=embedVar)
    else:
        await ctx.send(embed=embedVar1)

@client.command()
async def reload(ctx, extension):
    embedVar = discord.Embed(title="**DEVELOPER**", description="client.unload_extension(f'cogs.{extension}'\nclient.load_extension(f'cogs.{extension}'", color=7419530)
    embedVar.add_field(name="**PARSED**", value=f"Reloaded cog {extension}")
    embedVar1 = discord.Embed(title='**DEVELOPER**', description='Error occured:\n commands.MissingPermissions', color=7419530)
    embedVar1.add_field(name='**NOT PARSED**', value='Missing required permissions.')

    if ctx.message.author.id == 445271451159887889:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        await ctx.send(embed=embedVar)
    else:
        await ctx.send(embed=embedVar1)

for filename in os.listdir('./venv/cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='WIP | $help', url='https://twitch.tv/astelics'))
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

client.run('put your token here')
