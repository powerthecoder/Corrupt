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
import json


class Main(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.welcome_channel = client.get_channel(536770707384696832)
        self.facrec = 704929553289838683
        self.gen = client.get_channel(719720125485547590)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        x = random.randint(1,5)
        if(int(x) == 1):
            embed=discord.Embed(title="Player just arrived. Seems OP - please nerf", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
            await self.welcome_channel.send(embed=embed)
        elif(int(x) == 2):
            embed=discord.Embed(title="Player just slid into the server.", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
            await self.welcome_channel.send(embed=embed)
        elif(int(x) == 3):
            embed=discord.Embed(title="Player Has joined the chat. We hope you brought pizza.", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
            await self.welcome_channel.send(embed=embed)
        elif(int(x) == 4):
            embed=discord.Embed(title="Welcome Player We were expecting you ( ͡° ͜ʖ ͡°)", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
            await self.welcome_channel.send(embed=embed)
        elif(int(x) == 5):
            embed=discord.Embed(title="Oh no! Player has entered the chat Hide your bananas.", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
            await self.welcome_channel.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message):
        # Make sure spam loops dont happen
        if("https://discord.gg/" in message.content.lower()) and (message.channel.id != self.facrec):
            await message.delete()
        elif("http://discord.gg/" in message.content.lower()) and (message.channel.id != self.facrec):
            await message.delete()
        elif("/discord.gg/" in message.content.lower()) and (message.channel.id != self.facrec):
            await message.delete()
        elif("discord.gg" in message.content.lower()) and (message.channel.id != self.facrec):
            await message.delete()
        elif(".gg/" in message.content.lower()) and (message.channel.id != self.facrec):
            await message.delete()
        elif("nigger" in message.content.lower()):
            await message.delete()
        elif("nigga" in message.content.lower()):
            await message.delete()
        elif("faggot" in message.content.lower()):
            await message.delete()
        elif("fagot" in message.content.lower()):
            await message.delete()
        await self.client.process_commands(message)


    @commands.Cog.listener()
    async def on_message_delete(self, message):
        # Message = message.content
        # Author = message.author.mention
        with open("db_snipe.json", "r") as f:
            data = json.load(f)
        msg = message.content
        authr = message.author.mention
        data['message'] = f"**Message**: {msg} \n**Author:** {authr}"
        with open("db_snipe.json", "w") as f:
            json.dump(data, f)


def setup(client):
    client.add_cog(Main(client))
    