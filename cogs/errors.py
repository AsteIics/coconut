import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from discord.ext.commands import MissingRequiredArgument

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print ('Cog loaded: errors.py')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embedVar = discord.Embed(title='**DEVELOPER**', description='Error occured:\n commands.MissingRequiredArgument', color=7419530)
        embedVar.add_field(name='**NOT PARSED**', value='Input all arguments.')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=embedVar)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embedVar = discord.Embed(title='**DEVELOPER**', description='Error occured:\n commands.CommandNotFound', color=7419530)
        embedVar.add_field(name='**NOT PARSED**', value='Could not find command.')

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(embed=embedVar)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        embedVar = discord.Embed(title='**DEVELOPER**', description='Error occured:\n commands.MissingPermissions', color=7419530)
        embedVar.add_field(name='**NOT PARSED**', value='Missing required permissions.')

        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=embedVar)



def setup(client):
    client.add_cog(Errors(client))
