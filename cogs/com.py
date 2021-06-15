import discord
import random
import asyncio
import datetime
from discord.ext import commands

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Event
    @commands.Cog.listener()
    async def on_ready(self):
        print ('Cog loaded: com.py')

    #Command
    @commands.command()
    async def ping(self, ctx):
        embedVar = discord.Embed(title="**PING**", description=f"Ping: {round(client.latency * 1000)}ms", color=7506394)
        await ctx.send(embed=embedVar)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        embedVar = discord.Embed(title="**PURGED MESSAGES**", description=f"Messages has been removed!", color=7506394)
        embedVar.add_field(name="**MESSAGES**", value=f"{amount}")
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(embed=embedVar, delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        embedVar1 = discord.Embed(title="**KICKED USER**", description=f"{member}", color=7506394)
        embedVar1.add_field(name="**REASON**", value=f"{reason}", inline=False)
        embedVar1.add_field(name="**PUNISHER**", value=f"{ctx.author}", inline=False)

        embedVar2 = discord.Embed(title="**KICK**", description=f"You have been kicked from {ctx.message.guild.name}", color=7506394)
        embedVar2.add_field(name="**REASON**", value=f"{reason}", inline=False)
        embedVar2.add_field(name="**PUNISHER**", value=f"{ctx.author}", inline=False)

        channel = await member.create_dm()
        await ctx.send(embed=embedVar1)
        await channel.send(embed=embedVar2)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        embedVar1 = discord.Embed(title="**BANNED USER**", description=f"{member}", color=7506394)
        embedVar1.add_field(name="**REASON**", value=f"{reason}", inline=False)
        embedVar1.add_field(name="**BANNED BY**", value=f"{ctx.author}")

        embedVar2 = discord.Embed(title="**BAN**", description=f"You have been banned from {ctx.message.guild.name}", color=7506394)
        embedVar2.add_field(name="**REASON**", value=f"{reason}", inline=False)
        embedVar2.add_field(name="**BANNED BY**", value=f"{ctx.author}", inline=False)

        channel = await member.create_dm()
        await ctx.send(embed=embedVar1)
        await channel.send(embed=embedVar2)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        embedVar = discord.Embed(title="**UNBANNED USER**", description=f"{member}", color=7506394)
        embedVar.add_field(name="**UNBANNED BY**", value=f"{ctx.author}", inline=False)

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(embed=embedVar)
                return

    @commands.command(aliases=["ui", "whois"])
    async def userinfo(self, ctx, user : discord.Member):
        roles=[role for role in user.roles]
        roles.pop(0)

        embedVar=discord.Embed(title=f"User Info - {user}", description=" ", color=7506394)
        embedVar.set_thumbnail(url=user.avatar_url)
        embedVar.add_field(name="ID:", value=user.id)
        embedVar.add_field(name="Nick Name", value=user.nick, inline=False)
        embedVar.add_field(name="Created at", value=user.created_at.strftime("%a, %b %#d, %Y, %I:%M %p UTC"))
        embedVar.add_field(name="Joined server at", value=user.joined_at.strftime("%a, %b %#d, %Y, %I:%M %p UTC"))
        embedVar.add_field(name="Is the user a bot?", value=val, inline=False)
        embedVar.add_field(name="Top Role", value=user.top_role.mention)
        embedVar.add_field(name=f"Roles ({len(roles)})", value="   ".join([role.mention for role in roles]), inline=False)
        embedVar.set_footer(text=f"Requested by {ctx.message.author}")
        embedVar.timestamp = datetime.datetime.utcnow()

        if user.bot:
            val = "Yes"
        elif not user.bot:
            val = "No"
        await ctx.send(embed=embedVar)

def setup(client):
    client.add_cog(Commands(client))
