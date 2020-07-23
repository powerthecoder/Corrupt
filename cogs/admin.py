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
        self.promotion_channel = client.get_channel(725645441357840406)
        self.giveaway_channel = client.get_channel(719442620513779793)
    
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def giveaway(self, ctx, *,args):
        author = ctx.message.author.name
        embed=discord.Embed(title=args, description="React with 🎉 to enter!", color=0xffbb1c)
        embed.set_author(name="🎉 GIVEAWAY 🎉")
        message = await self.giveaway_channel.send(embed=embed)
        await message.add_reaction('🎉')

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def giveaway_tag(self, ctx, *,args):
        author = ctx.message.author.name
        embed=discord.Embed(title=args, description="React with 🎉 to enter!", color=0xffbb1c)
        embed.set_author(name="🎉 GIVEAWAY 🎉")
        await self.giveaway_channel.send("@everyone")
        message = await self.giveaway_channel.send(embed=embed)
        await message.add_reaction('🎉')

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def giveaway_winner(self, ctx, arg1):
        author = ctx.message.author.name
        # arg1 = message id
        # arg2 = channel id

        message = await ctx.fetch_message(int(arg1))
        users = set()
        for reaction in message.reactions:
            async for user in reaction.users():
                users.add(user)

        user_list = [user.name for user in users]
        #await ctx.send(f"users: {', '.join(user.name for user in users)}")
        #await ctx.send(f"Winner: **{random.choice(user_list)}**")

        embed=discord.Embed(title="Giveaway Winner", description=f"**Users:** {', '.join(user.name for user in users)}  \n**Winner:** {random.choice(user_list)}", color=0xffbb1c)
        embed.set_author(name="🎉 GIVEAWAY WINNER 🎉")
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def giveaway_winner_role(self, ctx, arg1, arg2):
        author = ctx.message.author.name
        # arg1 = Role
        # arg2 = ID

        role = discord.utils.find(lambda r: r.name == arg1)
        message = await ctx.fetch_message(int(arg2))
        users = set()
        for reaction in message.reactions:
            async for user in reaction.users():
                if(user.has_role(role)):
                    users.add(user)
                else:
                    pass
                

    @commands.command(pass_context=True)
    async def say(self, ctx, *,args):
        author = ctx.message.author.name
        author_id = ctx.message.author.id
        if(author_id == 255876083918831616) or (author_id == 226573983783321611):
            await ctx.channel.purge(limit=1)
            await ctx.send(f"{args}")
        else:
            pass

    @commands.command(pass_context=True)
    async def say_f(self, ctx, *,args):
        author = ctx.message.author.name
        author_id = ctx.message.author.id
        if(author_id == 255876083918831616) or (author_id == 226573983783321611):
            await ctx.channel.purge(limit=1)
            embed=discord.Embed(title="\u200b", description=f"{args}")
            await ctx.send(embed=embed)
        else:
            pass

    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def promote(self, ctx, user_name:discord.Member, *,args=None):
        rank = str(args)
        Helper = discord.utils.get(user_name.guild.roles, id=718156336755638294)
        Jr_Moderator = discord.utils.get(user_name.guild.roles, id=718156747914608650)
        Moderator = discord.utils.get(user_name.guild.roles, id=718156937497411637)
        Sr_Moderator = discord.utils.get(user_name.guild.roles, id=718157086516576366)
        Administrator = discord.utils.get(user_name.guild.roles, id=706641328854794332)
        Trial_Sr_Moderator = discord.utils.get(user_name.guild.roles, id=726662950940704808)
        Trial_Moderator = discord.utils.get(user_name.guild.roles, id=726662859446157352)
        Trial_Jr_Moderator = discord.utils.get(user_name.guild.roles, id=726662599726333990)

        author = ctx.author.name
        author_id = ctx.author.id

        if(str(rank.lower()) == "helper"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Helper)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Helper \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "jr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Jr Moderator \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Moderator \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "sr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Sr Moderator \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "admin"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Admin \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "trial sr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Trial Sr Moderator \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "trial mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Trial Moderator \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "trial jr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Trial_Jr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            
            embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Trial Jr Moderator \n**Promotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Promotion/Demotion Help Menu", description="Command is `-promote/demote @user <rank>` \n\n\nhelper \njr mod \nmod \nsr mod \nadmin \ntrial sr mod \ntrial mod \ntrial jr mod")
            await ctx.send(embed=embed)
        
    @commands.command(pass_context=True)
    @has_permissions(administrator=True)
    async def demote(self, ctx, user_name:discord.Member, *,args=None):
        rank = str(args)
        Helper = discord.utils.get(user_name.guild.roles, id=718156336755638294)
        Jr_Moderator = discord.utils.get(user_name.guild.roles, id=718156747914608650)
        Moderator = discord.utils.get(user_name.guild.roles, id=718156937497411637)
        Sr_Moderator = discord.utils.get(user_name.guild.roles, id=718157086516576366)
        Administrator = discord.utils.get(user_name.guild.roles, id=706641328854794332)
        Trial_Sr_Moderator = discord.utils.get(user_name.guild.roles, id=726662950940704808)
        Trial_Moderator = discord.utils.get(user_name.guild.roles, id=726662859446157352)
        Trial_Jr_Moderator = discord.utils.get(user_name.guild.roles, id=726662599726333990)

        author = ctx.author.name
        author_id = ctx.author.id

        if(str(rank.lower()) == "helper"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Helper)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Helper \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "jr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Jr Moderator \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Moderator \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "sr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Sr Moderator \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "admin"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Administrator  \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "trial sr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Trial Sr Moderator \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "trial mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            await Member.remove_roles(user_name, Trial_Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Trial Moderator \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        if(str(rank.lower()) == "trial jr mod"):
            await ctx.channel.purge(limit=1)
            await Member.add_roles(user_name, Trial_Jr_Moderator)
            await Member.remove_roles(user_name, Helper)
            await Member.remove_roles(user_name, Moderator)
            await Member.remove_roles(user_name, Sr_Moderator)
            await Member.remove_roles(user_name, Administrator)
            await Member.remove_roles(user_name, Trial_Sr_Moderator)
            await Member.remove_roles(user_name, Trial_Moderator)
            await Member.remove_roles(user_name, Jr_Moderator)
            
            embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Trial Jr Moderator \n**Demotor:** {author}")
            await self.promotion_channel.send(embed=embed)
        else:
            embed=discord.Embed(title="Promotion/Demotion Help Menu", description="Command is `-promote/demote @user <rank>` \n\n\nhelper \njr mod \nmod \nsr mod \nadmin \ntrial sr mod \ntrial mod \ntrial jr mod")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Main(client))
    