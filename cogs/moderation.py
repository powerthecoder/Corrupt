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
    
    
    @commands.command(pass_context=True)
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, arg):            
        author = ctx.message.author.name                                                                            
        embed=discord.Embed(title=f"Clearing...", description=f"Clearing {arg}", color=0xf20000)
        await ctx.send(embed=embed)
        amount1 = int(arg)
        time.sleep(1)
        await ctx.channel.purge(limit=amount1+2)


    @commands.command(pass_context=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx, user_name:discord.Member, *,args=None):
        author = ctx.author.name
        embed=discord.Embed(title="Player Kicked", description=f"**Player:** {user_name} \n**Reason:** {args} \n**Kicked By:** {author}", color=0xf20000)
        await user_name.kick(reason=args)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, user_name:discord.Member, *,args=None):
        author = ctx.author.name
        embed=discord.Embed(title="Player Banned", description=f"**Player:** {user_name} \n**Reason:** {args} \n**Banned By:** {author}", color=0xf20000)
        await user_name.ban(reason=args)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @has_permissions(ban_members=True)
    async def softban(self, ctx, user_name:discord.Member, *,args=None):
        await user_name.ban(reason=None)
        await asyncio.sleep(5)
        await user_name.unban(reason=None)


    @commands.command(pass_context=True)
    @has_permissions(kick_members=True)
    async def mute(self, ctx, user_name:discord.Member, args=None):
        # 683197335429316644
        author = ctx.author.name
        role = discord.utils.get(user_name.guild.roles, name="Muted")
        await Member.add_roles(user_name, role)
        embed=discord.Embed(title="Player Muted", description=f"**Player:** {user_name} \n**Reason:** {args} \n**Muted By:** {author}", color=0xf20000)
        await ctx.send(embed=embed)


    @commands.command()
    @has_permissions(administrator=True)
    async def strike(self, ctx, faction, *,args):
        author = ctx.message.author.name
        author_id = ctx.message.author.id
        strike_channel = self.client.get_channel(727435494555910265)

        with open("/root/DiscordGit/Corrupt/cogs/db_faction.json", "r") as f:
            factions = json.load(f)
        target = str(faction)
        if not f'{target}' in factions:
            factions[f'{target}'] = {}
            factions[f'{target}'] = 1
            embed=discord.Embed(title="Faction Strike", description=f"**Striked:** {faction} \n**Reason:** {args} \n**Total Strikes:** 1 \n**Strike By:** {author}", color=0xf20000)
            await strike_channel.send(embed=embed)
        else:
            warnam = int(factions[f'{target}'])
            warnam += 1
            factions[f'{target}'] = warnam
            embed=discord.Embed(title="Faction Strike", description=f"**Striked:** {faction} \n**Reason:** {args} \n**Total Strikes:** {warnam} \n**Strike By:** {author}", color=0xf20000)
            await strike_channel.send(embed=embed)
        with open("db_faction.json", "w") as f:
            json.dump(factions, f)
    
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def fire(self, ctx, user_name:discord.Member, *,args=None):
        for i in user_name.guild.roles:
            try:
                role = discord.utils.get(user_name.guild.roles, name=str(i))
                await Member.remove_roles(user_name, role)
            except:
                pass
            pass
        member_role = discord.utils.get(user_name.guild.roles, name="Member")
        await Member.add_roles(user_name, member_role)
        await user_name.edit(nick=None)
        embed=discord.Embed(title=f"Fired {user_name}", description=f"{user_name} has been striped of all roles")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Main(client))
    