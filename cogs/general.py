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
    

    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(title="Help Menu", description="Version 1.0 \nPrefix `-`\n<> are place holders")
        embed.add_field(name="`-ticket <reason>`", value="To make a ticket (`<reason>` not required)", inline=False)
        embed.add_field(name="`-close`", value="To close a ticket that you own", inline=False)
        embed.add_field(name="`-suggest <suggestion>`", value="To create a suggestion", inline=False)
        embed.add_field(name="`-help`", value="To open the help menu", inline=False)
        embed.add_field(name="`-adminhelp`", value="To open Staff help menu", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    @has_permissions(manage_messages=True)
    async def adminhelp(self, ctx):
        embed=discord.Embed(title="Help Menu", description="Version 1.0 \nPrefix `-`\n<> are place holders")
        embed.add_field(name="`-purge <amount>`", value="To clear chat in discord", inline=False)
        embed.add_field(name="`-warn @user <reason>`", value="To give a warning to a user", inline=False)
        embed.add_field(name="`-kick @user <reason>`", value="To kick the user", inline=False)
        embed.add_field(name="`-ban @user <reason>`", value="To ban the user", inline=False)
        embed.add_field(name="`-softban @user`", value="To kick a user without them knowing and deleting all msg they have", inline=False)
        embed.add_field(name="`-mute @user <reason>`", value="To mute a user", inline=False)
        embed.add_field(name="`-ticket <reason>`", value="To make a ticket (`<reason>` not required)", inline=False)
        embed.add_field(name="`-close`", value="To close a ticket that you own", inline=False)
        embed.add_field(name="`-close_s @user`", value="To close a ticket that you do **NOT** own", inline=False)
        embed.add_field(name="`-suggest <suggestion>`", value="To create a suggestion", inline=False)
        embed.add_field(name="`-giveaway <reward>`", value="To create a giveaway message", inline=False)
        embed.add_field(name="`-giveaway_tag <reward>`", value="To create a giveaway message **(WILL TAG EVERYONE)**", inline=False)
        embed.add_field(name="`-giveaway_winner <msg ID>`", value="To auto roll a winner from a giveaway", inline=False)
        embed.add_field(name="`-giveaway_role <role> <msg ID>", value="To select a winner based on a role", inline=False)
        embed.add_field(name="`-say <args>`", value="To make the bot text as you", inline=False)
        embed.add_field(name="`-say_f <args>`", value="To make the bot text in embeds as you", inline=False)
        embed.add_field(name="`-help`", value="To open the help menu", inline=False)
        embed.add_field(name="`-adminhelp`", value="To open Staff help menu", inline=False)
        embed.add_field(name="`-promote @user <rank>`", value="To promote someone", inline=False)
        embed.add_field(name="`-demote @user <rank>`", value="To demote someone", inline=False)
        embed.add_field(name="`-strike <faction> <reason>`", value="To give a strike to a faction", inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def snipe(self, ctx):
        with open("db_snipe.json", "r") as f:
            data = json.load(f)
        snipe = data["message"]
        embed=discord.Embed(title="Message Snipe", description=f"**Latest Deleted Message** \n\n{snipe}")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def about(self, ctx):
        author = ctx.message.author.name
        embed=discord.Embed(title="About", description="**Version:** 1.0 \n**Developer:** <@255876083918831616> \n**Owner:** <@226573983783321611>", color=0xff0000)
        embed.add_field(name="Website: ", value="https://powerthecoder.xyz", inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))
    