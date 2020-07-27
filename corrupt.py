import os
import sys
import time
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.utils import find
from discord.utils import get
import asyncio
from datetime import datetime
import json

with open("token.json", "r") as f:
    data = json.load(f)

d_token = data['Token']

Token = str(d_token)



cogs = [
    'cogs.admin',
    'cogs.events',
    'cogs.general',
    'cogs.moderation',
    'cogs.ticket',
]

class client(commands.AutoShardedBot):
    def __init__(self):
        prefix_list = ('-')
        super().__init__(command_prefix=prefix_list, case_insensitive=True)
        self.red = 0xff0000
        self.devs = [
            255876083918831616 # leo
        ]
        self.Version = '1.0'

    async def on_ready(self):
        #await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Developing'))
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Corrupt Factions Discord"))


        print(" ")
        print("-------------------------------")
        print("Bot Online")
        print('Logged In As: ',client.user.name)
        print('ID: ',client.user.id)
        print('Bot Version: ',self.Version)
        print('Discord Version: ',discord.__version__)
        print('-------------------------------')
        print(" ")
        print(" ")

        for cog in cogs:
            try:
                client.load_extension(cog)
                print(f"Loaded {cog}")
            except Exception as e:
                print(f"Error on Loading {cog}. Error is {e}")

client = client()
client.remove_command('help')

StartTime = datetime.now()

@client.event
async def ad():
    await client.wait_until_ready()
    gen = client.get_channel(719720125485547590)
    while not client.is_closed():
        x = 0
        while x <= 4:
            await asyncio.sleep(21600)
            if(x == 0):
                x += 1
                await gen.send(">>> Join us on the server @ - play.corruptfacs.net")
            elif(x == 1):
                x += 1
                await gen.send(">>> Make sure to sign up for our website - https://www.corruptfactions.net/")
            elif(x == 2):
                x += 1
                await gen.send(">>> Hey Everyone don't forget to check out our store - http://store.corruptfacs.net/")
            elif(x == 3):
                x = 0


@client.command(aliases=['new'])
async def ticket(ctx, *,args=None):
    author = ctx.author.name
    author_id = ctx.author.id
    author_test = ctx.author
    author_dm = client.get_user(author_id)
    guild = ctx.guild

    def check_react(reaction, user):
        return str(reaction.emoji) in ["⚔️"] and user != client.user

    await ctx.channel.purge(limit=1)
    category_id = discord.utils.get(guild.categories, name="Tickets")

    channel = await category_id.create_text_channel(f'{author}')
    await channel.set_permissions(ctx.author, read_messages=True, send_messages=True, read_message_history=True, add_reactions=True)

    embed=discord.Embed(title=f"Support Ticket", description=f"Hey {author}, please wait patiently for a member on our staff \nteam to get back to you! While you are waiting please describe what you need help \nwith to the best of you're ability. \nFaction leader? Click :crossed_swords: \nto claim faction leader role")
    await channel.send(f"<@{author_id}>")
    msg = await channel.send(embed=embed)
    await msg.add_reaction("⚔️")
    reaction, user = await client.wait_for('reaction_add', timeout = 100, check=check_react)
    if(str(reaction.emoji) == "⚔️"):
        embed=discord.Embed(title="Faction Leader", description="You have been given Faction Leader role. \nIf you don't need anything else please do `-close`")
        role = discord.utils.get(author_test.guild.roles, name="Faction Leader")
        await Member.add_roles(author_test, role)
        await channel.send(f"<@{author_id}>")
        await channel.send(embed=embed)

@client.command()
async def close(ctx):
    author2 = ctx.author.name
    author_id = ctx.author.id
    guild = ctx.guild
    author = str(author2.lower())
    
    support_channel = discord.utils.get(guild.channels, name=author, type=discord.ChannelType.text)
    embed=discord.Embed(title=f"Ticket closing {author}", description=f"If you need any more help please do `-ticket` ", color=0xff0000)
    embed.set_author(name="Support Ticket")
    await ctx.send(f"<@{author_id}>")
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await support_channel.delete()
    
@client.command()
@has_permissions(manage_channels=True)
async def close_s(ctx, user_name:discord.Member):
    author = ctx.author.name
    author_id = ctx.author.id
    author_DM = client.get_user(author_id)
    guild = ctx.guild

    channel_id = discord.utils.get(guild.channels, name=user_name)
    channel = client.get_channel(channel_id)
    embed=discord.Embed(title=f"{user_name} Deleting Ticket", description=f"If you need any more assistance please do `-ticket`", color=0xff0000)
    embed.set_author(name="Support Ticket")
    await ctx.send(f"@{user_name}")
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.channel.delete()


@client.command(aliases=['report', 'Sticket', 'Report'])
@has_permissions(manage_messages=True)
async def sticket(ctx, *,args=None):
    author = ctx.author.name
    author_id = ctx.author.id
    author_DM = client.get_user(author_id)
    author_discord = ctx.author
    guild = ctx.guild

    await ctx.channel.purge(limit=1)
    category_id = discord.utils.get(guild.categories, name="Report Forms")

    channel_test = await category_id.create_text_channel(f'{author}')
    await channel_test.set_permissions(ctx.author, read_messages=True, send_messages=True, read_message_history=True, add_reactions=True)


    def check(m):
        return m.channel.id == channel_test.id and m.author.id == ctx.author.id

    embed=discord.Embed(title="Punishment Reports", description="Discord user or Minecraft user:")
    await channel_test.send(f"<@{author_id}>")
    msg = await channel_test.send(embed=embed)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed2=discord.Embed(title="Punishment Reports", description="You're IGN or discord name?")
    await channel_test.send(embed=embed2)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed3=discord.Embed(title="Punishment Reports", description="Punishment?")
    await channel_test.send(embed=embed3)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed4=discord.Embed(title="Punishment Reports", description="How long does the punishment last?")
    await channel_test.send(embed=embed4)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed5=discord.Embed(title="Punishment Reports", description="What were they doing?")
    await channel_test.send(embed=embed5)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed6=discord.Embed(title="Punishment Reports", description="Did you issue a warning first?")
    await channel_test.send(embed=embed6)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed7=discord.Embed(title="Punishment Reports", description="Was anyone else involved?")
    await channel_test.send(embed=embed7)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed8=discord.Embed(title="Punishment Reports", description="Anything else we should know?")
    await channel_test.send(embed=embed8)
    question1 = await client.wait_for('message', timeout = 604800, check=check)

    embed9=discord.Embed(title="Punishment Reports", description="Your report has been submited")
    await channel_test.send(embed=embed9)

    asyncio.sleep(10)
    await channel_test.set_permissions(author_discord, read_messages=False, send_messages=False, read_message_history=False, add_reactions=False)
    notify_msg = await channel_test.send("@everyone")
    asyncio.sleep(5)
    await notify_msg.delete()


@client.command(pass_context=True)
async def reload(ctx, cog=None):
    if not ctx.author.id in client.devs:
        return
    if not cog:
        return
    try:
        client.reload_extension(cog)
        await ctx.message.add_reaction('✅')
        msg = await ctx.send(f"Reloading **{cog}**")
        await asyncio.sleep(20)
        await msg.delete()
    except Exception as e:
        await ctx.message.add_reaction('❌')
        msg = await ctx.send(f"<@255876083918831616> umm... **{cog}**!\n```{e}```")
        dev_logs = client.get_channel(665553350355582986)
        mod_logs = client.get_channel(477356858051526656)
        await asyncio.sleep(20)
        await msg.delete()
        await dev_logs.send(f"<@255876083918831616> umm... **{cog}**!\n```{e}```")
        await mod_logs.send(f"<@255876083918831616> umm... **{cog}**!\n```{e}```")





client.loop.create_task(ad())            
client.run(Token)
