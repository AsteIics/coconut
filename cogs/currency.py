import discord
import json
import os
from random import randrange, randint
from discord.ext import commands

os.chdir("C:\\Users\\astel\\Documents\\Repositories\\JetBrains\\discord")

class Currency(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cog loaded: currency.py')

    @commands.command(aliases=['bal'])
    async def balance(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()
        user = ctx.author
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        embedVar = discord.Embed(name=f"**{ctx.author.name}'s Balance**", color=3066993)
        embedVar.set_thumbnail(url=author.avatar_url)
        embedVar.add_field(name="**Wallet balance**", value=wallet_amt)
        embedVar.add_field(name="**Bank balance**", value=bank_amt)
        embedVar.set_footer(text=f"Requested by {ctx.message.author}")
        await ctx.send(embed=embedVar)

    @commands.command()
    async def beg(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]

        earnings = random.randrange(501)
        chance = random.randint(0, 100)

        if chance > 50:
            wallet_amt += earnings
            await ctx.send(f"You sat on the street for 5 hours, {random.randint(0,60)} people stopped because you're so hot.")
        elif chance < 50:
            await ctx.semd("You sat on the street for 5 hours, no one stopped because you look ugly.")

        with open("mainbank.json", "w") as f:
            json.dump(users, f)

    async def open_account(self, user):
        users = await get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 500

        with open("mainbank.json", "w") as f:
            json.dump(users, f)
        return True

    async def get_bank_data(self):
        with open("mainbank.json", "r") as f:
            users = json.load(f)

        return users

def setup(client):
    client.add_cog(Currency(client))
