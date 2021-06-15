import discord
import random
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog loaded: fun.py')

    @commands.command()
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
                "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
                "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
                "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
                "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]
        embedVar = discord.Embed(title="**QUESTION**", description=f"{question}", color=7506394)
        embedVar.add_field(name="**ANSWER**", value=f"{random.choice(responses)}", inline=False)
        await ctx.send(embed=embedVar)

    @commands.command()
    async def ship(self, ctx, user1 : discord.Member, user2 : discord.Member):
        embedVar = discord.Embed(title='**LOVE CALCULATOR**', description=f'{user1} and {user2} have a:', color=10181046)
        embedVar.set_thumbnail(url=ctx.author.avatar_url)
        embedVar.add_field(name=f'**{random.randint(0, 100 + 1)}%**', value='chance at true love!')
        embedCoc = discord.Embed(title='**LOVE CALCULATOR**', description=f'{user1} and {user2} have a:', color=10181046)
        embedCoc.set_author(name=ctx.author, url='https://twitch.tv/cooocnut', icon_url=ctx.author.avatar_url)
        embedCoc.add_field(name='**100%**', value='chance at true love!')
        if user1.id == 783028422057918494:
            if user2.id == 445271451159887889:
                await ctx.send(embed=embedCoc)
            else:
                await ctx.send(embed=embedVar)

    @commands.command()
    async def simp(self, ctx, user : discord.Member):
        embedVar = discord.Embed(title='**SIMP CALCULATOR**', description=f'{user} has a simp score of:', color=10181046)
        embedVar.set_author(name=ctx.author, url='https://twitch.tv/astelics', icon_url=ctx.author.avatar_url)
        embedVar.add_field(name=f'**{random.randint(0, 100 + 1)}%**', value='What a simp!')
        embedSimps = discord.Embed(title='**SIMP CALCULATOR**', description=f'{user} has a simp score of:', color=10181046)
        embedSimps.set_author(name=ctx.author, url='https://twitch.tv/astelics', icon_url=ctx.author.avatar_url)
        embedSimps.add_field(name=f'**100%**', value='What a simp!')
        if user.id == 783028422057918494 or user.id == 652856571252047872:
            await ctx.send(embed=embedSimps)
        else:
            await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Fun(client))
