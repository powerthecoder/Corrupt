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
