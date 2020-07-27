import os
import os
import sys
import time
import random
from random import randrange
import dbl
import discord
from discord.ext import commands
from discord.ext import tasks
from discord import Member
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.utils import find
from discord.utils import get
import asyncio
import youtube_dl
import requests
from requests import get
import logging
from datetime import datetime
from twilio.rest import Client
import matplotlib
import json
from discord.ext import menus
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
import pyppdf.patch_pyppeteer
import lavalink
from discord import Embed

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['new'])
    async def ticket(self, ctx, *,args=None):
        author = ctx.author.name
        author_id = ctx.author.id
        author_test = ctx.author
        author_dm = self.client.get_user(author_id)
        guild = ctx.guild

        def check_react(reaction, user):
            return str(reaction.emoji) in ["⚔️"] and user != self.client.user

        await ctx.channel.purge(limit=1)
        category_id = discord.utils.get(guild.categories, name="Tickets")

        channel = await category_id.create_text_channel(f'{author}')
        await channel.set_permissions(ctx.author, read_messages=True, send_messages=True, read_message_history=True, add_reactions=True)

        embed=discord.Embed(title=f"Support Ticket", description=f"Hey {author}, please wait patiently for a member on our staff \nteam to get back to you! While you are waiting please describe what you need help \nwith to the best of you're ability. \nFaction leader? Click :crossed_swords: \nto claim faction leader role")
        await channel.send(f"<@{author_id}>")
        msg = await channel.send(embed=embed)
        await msg.add_reaction("⚔️")
        reaction, user = await self.client.wait_for('reaction_add', timeout = 100, check=check_react)
        if(str(reaction.emoji) == "⚔️"):
            embed=discord.Embed(title="Faction Leader", description="You have been given Faction Leader role. \nIf you don't need anything else please do `-close`")
            role = discord.utils.get(author_test.guild.roles, name="Faction Leader")
            await Member.add_roles(author_test, role)
            await channel.send(f"<@{author_id}>")
            await channel.send(embed=embed)

    @commands.command()
    async def close(self, ctx):
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
        
    @commands.command()
    @has_permissions(manage_channels=True)
    async def close_s(self, ctx, user_name:discord.Member):
        author = ctx.author.name
        author_id = ctx.author.id
        author_DM = self.client.get_user(author_id)
        guild = ctx.guild

        channel_id = discord.utils.get(guild.channels, name=user_name)
        channel = self.client.get_channel(channel_id)
        embed=discord.Embed(title=f"{user_name} Deleting Ticket", description=f"If you need any more assistance please do `-ticket`", color=0xff0000)
        embed.set_author(name="Support Ticket")
        await ctx.send(f"@{user_name}")
        await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.channel.delete()


    @commands.command(aliases=['report'])
    @has_permissions(manage_messages=True)
    async def sticket(self, ctx, *,args=None):
        author = ctx.author.name
        author_id = ctx.author.id
        author_DM = self.client.get_user(author_id)
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
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed2=discord.Embed(title="Punishment Reports", description="You're IGN or discord name?")
        await channel_test.send(embed=embed2)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed3=discord.Embed(title="Punishment Reports", description="Punishment?")
        await channel_test.send(embed=embed3)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed4=discord.Embed(title="Punishment Reports", description="How long does the punishment last?")
        await channel_test.send(embed=embed4)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed5=discord.Embed(title="Punishment Reports", description="What were they doing?")
        await channel_test.send(embed=embed5)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed6=discord.Embed(title="Punishment Reports", description="Did you issue a warning first?")
        await channel_test.send(embed=embed6)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed7=discord.Embed(title="Punishment Reports", description="Was anyone else involved?")
        await channel_test.send(embed=embed7)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed8=discord.Embed(title="Punishment Reports", description="Anything else we should know?")
        await channel_test.send(embed=embed8)
        question1 = await self.client.wait_for('message', timeout = 604800, check=check)

        embed9=discord.Embed(title="Punishment Reports", description="Your report has been submited")
        await channel_test.send(embed=embed9)

        asyncio.sleep(10)
        await channel_test.set_permissions(author_discord, read_messages=False, send_messages=False, read_message_history=False, add_reactions=False)
        notify_msg = await channel_test.send("@everyone")
        asyncio.sleep(5)
        await notify_msg.delete()



def setup(client):
    client.add_cog(Main(client))
    