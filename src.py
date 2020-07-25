'''
Developer: Leo Power
Discord: -{ Power1482 }-#0101
Support Discord Server: https://discord.gg/bQCZMDE/
Website: https://powerthecoder.xyz/
'''
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

'''
Name: Corrupt Network
Prefix: -
color=0xff0000

* Auto welcome msgs 
Blacklist words
Anti Link (unless in specific channel)
Music
Auto Messages
Ticket System
Suggest System
Giveaway System
Purge 
Softban (kick, delete all msgs, no ban)
Ban
Kick
Warn
Mute
Say
Mod Logs
'''

client = commands.Bot(command_prefix="-")
Token = 'NzI1OTQ1NzM1NjM5NTk3MTI3.XvWHsg.0oMmGpzb8wJcVJi6V4fLto2-8WU'
Version = '1.0'
client.remove_command("help")




#       BOT EVENTS       #


@client.event
async def on_ready():
    print(" ")
    print("-------------------------------")
    print("Bot Online")
    print('Logged In As: ',client.user.name)
    print('ID: ',client.user.id)
    print('Bot Version: ',Version)
    print('Discord Version: ',discord.__version__)
    print('-------------------------------')
    print(" ")
    print(" ")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Corrupt Factions Discord"))
    #await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Developing'))

@client.event
async def on_member_join(member):
    welcome_channel = client.get_channel(536770707384696832)
    x = random.randint(1,5)
    if(int(x) == 1):
        embed=discord.Embed(title="Player just arrived. Seems OP - please nerf", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
        await welcome_channel.send(embed=embed)
    elif(int(x) == 2):
        embed=discord.Embed(title="Player just slid into the server.", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
        await welcome_channel.send(embed=embed)
    elif(int(x) == 3):
        embed=discord.Embed(title="Player Has joined the chat. We hope you brought pizza.", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
        await welcome_channel.send(embed=embed)
    elif(int(x) == 4):
        embed=discord.Embed(title="Welcome Player We were expecting you ( ͡° ͜ʖ ͡°)", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
        await welcome_channel.send(embed=embed)
    elif(int(x) == 5):
        embed=discord.Embed(title="Oh no! Player has entered the chat Hide your bananas.", description=f"Please Welcome **{member}** to Corrupt Factions \nCheck out #rules")
        await welcome_channel.send(embed=embed)

@client.event
async def on_message(message):
    # Make sure spam loops dont happen
    if("https://discord.gg/" in message.content.lower()) and (message.channel.id != 704929553289838683):
        await message.delete()
    elif("http://discord.gg/" in message.content.lower()) and (message.channel.id != 704929553289838683):
        await message.delete()
    elif("/discord.gg/" in message.content.lower()) and (message.channel.id != 704929553289838683):
        await message.delete()
    elif("discord.gg" in message.content.lower()) and (message.channel.id != 704929553289838683):
        await message.delete()
    elif(".gg/" in message.content.lower()) and (message.channel.id != 704929553289838683):
        await message.delete()
    elif("nigger" in message.content.lower()):
        await message.delete()
    elif("nigga" in message.content.lower()):
        await message.delete()
    elif("faggot" in message.content.lower()):
        await message.delete()
    elif("fagot" in message.content.lower()):
        await message.delete()
    await client.process_commands(message)

@client.event
async def on_message_delete(message):
    # Message = message.content
    # Author = message.author.mention
    with open("corrupt_snipe.json", "r") as f:
        data = json.load(f)
    msg = message.content
    authr = message.author.mention
    data['message'] = f"**Message**: {msg} \n**Author:** {authr}"
    with open("corrupt_snipe.json", "w") as f:
        json.dump(data, f)


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


#       COMMANDS        #

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help Menu", description="Version 1.0 \nPrefix `-`\n<> are place holders")
    embed.add_field(name="`-ticket <reason>`", value="To make a ticket (`<reason>` not required)", inline=False)
    embed.add_field(name="`-close`", value="To close a ticket that you own", inline=False)
    embed.add_field(name="`-suggest <suggestion>`", value="To create a suggestion", inline=False)
    embed.add_field(name="`-help`", value="To open the help menu", inline=False)
    embed.add_field(name="`-adminhelp`", value="To open Staff help menu", inline=False)
    await ctx.send(embed=embed)

@client.command()
@has_permissions(manage_messages=True)
async def adminhelp(ctx):
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


@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def purge(ctx, arg):            
    author = ctx.message.author.name                                                                            
    embed=discord.Embed(title=f"Clearing...", description=f"Clearing {arg}", color=0xff0000)
    await ctx.send(embed=embed)
    amount1 = int(arg)
    time.sleep(1)
    await ctx.channel.purge(limit=amount1+2)

@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def warn(ctx, user_name:discord.Member, *,args=None):
    author = ctx.message.author.name

    # Get Information
    user_id = user_name.id
    userid = str(user_id)

    with open("corrupt_ticket.json", "r") as f:
        users = json.load(f)
    target = userid
    if not f'{target}' in users:
        users[f'{target}'] = {}
        users[f'{target}'] = 1
        embed=discord.Embed(title="Warning", description=f"**Warned:** {user_name} \n**Reason:** {args} \n**Total Warns:** 1 \n**Warned By:** {author}", color=0xff0000)
        await ctx.send(f"<@{userid}>")
        await ctx.send(embed=embed)
    else:
        warnam = int(users[f'{target}'])
        warnam += 1
        users[f'{target}'] = warnam
        embed=discord.Embed(title="Warning", description=f"**Warned:** {user_name} \n**Reason:** {args} \n**Total Warns:** {warnam} \n**Warned By:** {author}", color=0xff0000)
        await ctx.send(f"<@{userid}>")
        await ctx.send(embed=embed)
    with open("corrupt_ticket.json", "w") as f:
        json.dump(users, f)

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def kick(ctx, user_name:discord.Member, *,args=None):
    author = ctx.author.name
    embed=discord.Embed(title="Player Kicked", description=f"**Player:** {user_name} \n**Reason:** {args} \n**Kicked By:** {author}", color=0xff0000)
    await user_name.kick(reason=args)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@has_permissions(ban_members=True)
async def ban(ctx, user_name:discord.Member, *,args=None):
    author = ctx.author.name
    embed=discord.Embed(title="Player Banned", description=f"**Player:** {user_name} \n**Reason:** {args} \n**Banned By:** {author}", color=0xff0000)
    await user_name.ban(reason=args)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@has_permissions(ban_members=True)
async def softban(ctx, user_name:discord.Member, *,args=None):
    await user_name.ban(reason=None)
    await asyncio.sleep(5)
    await user_name.unban(reason=None)

@client.command(pass_context=True)
@has_permissions(kick_members=True)
async def mute(ctx, user_name:discord.Member, args=None):
    # 683197335429316644
    author = ctx.author.name
    role = discord.utils.get(user_name.guild.roles, name="Muted")
    await Member.add_roles(user_name, role)
    embed=discord.Embed(title="Player Muted", description=f"**Player:** {user_name} \n**Reason:** {args} \n**Muted By:** {author}", color=0xff0000)
    await ctx.send(embed=embed)

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

@client.command()
async def suggest(ctx, *,args=None):
    author = ctx.author.name
    if(str(args.lower()) == None):
        embed=discord.Embed(title="Suggestion", description="Please enter your suggestion after the command")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
    else:
        suggestion_channel = client.get_channel(705326373992005674)
        test_channel = client.get_channel(704929553289838683)
        '''
        Developer: Leo Power

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
        INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
        PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL LEO POWER AND DEVELOPERS OR POWERTHECODER BE LIABLE 
        FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
        ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

        '''
        embed=discord.Embed(title="Suggestion", description=f"**Suggested By:** {author} \n**Suggestion:**\n {args}")
        msg = await suggestion_channel.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def giveaway(ctx, *,args):
    author = ctx.message.author.name
    embed=discord.Embed(title=args, description="React with 🎉 to enter!", color=0xff0000)
    embed.set_author(name="🎉 GIVEAWAY 🎉")
    giveaway_channel = client.get_channel(719442620513779793)
    message = await giveaway_channel.send(embed=embed)
    await message.add_reaction('🎉')

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def giveaway_tag(ctx, *,args):
    author = ctx.message.author.name
    embed=discord.Embed(title=args, description="React with 🎉 to enter!", color=0xff0000)
    embed.set_author(name="🎉 GIVEAWAY 🎉")
    giveaway_channel = client.get_channel(719442620513779793)
    await giveaway_channel.send("@everyone")
    message = await giveaway_channel.send(embed=embed)
    await message.add_reaction('🎉')

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def giveaway_winner(ctx, arg1):
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

    embed=discord.Embed(title="Giveaway Winner", description=f"**Users:** {', '.join(user.name for user in users)}  \n**Winner:** {random.choice(user_list)}", color=0xff0000)
    embed.set_author(name="🎉 GIVEAWAY WINNER 🎉")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def giveaway_winner_role(ctx, arg1, arg2):
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
            

@client.command(pass_context=True)
async def say(ctx, *,args):
    author = ctx.message.author.name
    author_id = ctx.message.author.id
    if(author_id == 255876083918831616) or (author_id == 226573983783321611):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"{args}")
    else:
        pass

@client.command(pass_context=True)
async def say_f(ctx, *,args):
    author = ctx.message.author.name
    author_id = ctx.message.author.id
    if(author_id == 255876083918831616) or (author_id == 226573983783321611):
        await ctx.channel.purge(limit=1)
        embed=discord.Embed(title="\u200b", description=f"{args}")
        await ctx.send(embed=embed)
    else:
        pass

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def promote(ctx, user_name:discord.Member, *,args=None):
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
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Helper \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Helper)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "jr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Jr Moderator \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Moderator \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "sr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Sr Moderator \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "admin"):
        await ctx.channel.purge(limit=1)
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Admin \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await Member.add_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
    if(str(rank.lower()) == "trial sr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Trial Sr Moderator \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "trial mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Trial Moderator \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "trial jr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Promotion", description=f"Congratulations {user_name}\n\n**New Rank:** Trial Jr Moderator \n**Promotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Trial_Jr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        
        
    else:
        embed=discord.Embed(title="Promotion/Demotion Help Menu", description="Command is `-promote/demote @user <rank>` \n\n\nhelper \njr mod \nmod \nsr mod \nadmin \ntrial sr mod \ntrial mod \ntrial jr mod")
        await ctx.send(embed=embed)
    
@client.command(pass_context=True)
@has_permissions(administrator=True)
async def demote(ctx, user_name:discord.Member, *,args=None):
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
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Helper \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Helper)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "jr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Jr Moderator \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Moderator \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "sr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Sr Moderator \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "admin"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Administrator  \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "trial sr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Trial Sr Moderator \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "trial mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Trial Moderator \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        await Member.remove_roles(user_name, Trial_Jr_Moderator)
        
        
    if(str(rank.lower()) == "trial jr mod"):
        promotion_channel = client.get_channel(725645441357840406)
        embed=discord.Embed(title="Demotion", description=f"Demoted {user_name}\n\n**New Rank:** Trial Jr Moderator \n**Demotor:** {author}")
        await promotion_channel.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await Member.add_roles(user_name, Trial_Jr_Moderator)
        await Member.remove_roles(user_name, Helper)
        await Member.remove_roles(user_name, Moderator)
        await Member.remove_roles(user_name, Sr_Moderator)
        await Member.remove_roles(user_name, Administrator)
        await Member.remove_roles(user_name, Trial_Sr_Moderator)
        await Member.remove_roles(user_name, Trial_Moderator)
        await Member.remove_roles(user_name, Jr_Moderator)
        
        
    else:
        embed=discord.Embed(title="Promotion/Demotion Help Menu", description="Command is `-promote/demote @user <rank>` \n\n\nhelper \njr mod \nmod \nsr mod \nadmin \ntrial sr mod \ntrial mod \ntrial jr mod")
        await ctx.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def strike(ctx, faction, *,args):
    author = ctx.message.author.name
    author_id = ctx.message.author.id
    strike_channel = client.get_channel(727435494555910265)

    with open("corrupt_faction.json", "r") as f:
        factions = json.load(f)
    target = str(faction)
    if not f'{target}' in factions:
        factions[f'{target}'] = {}
        factions[f'{target}'] = 1
        embed=discord.Embed(title="Faction Strike", description=f"**Striked:** {faction} \n**Reason:** {args} \n**Total Strikes:** 1 \n**Strike By:** {author}", color=0xff0000)
        await strike_channel.send(embed=embed)
    else:
        warnam = int(factions[f'{target}'])
        warnam += 1
        factions[f'{target}'] = warnam
        embed=discord.Embed(title="Faction Strike", description=f"**Striked:** {faction} \n**Reason:** {args} \n**Total Strikes:** {warnam} \n**Strike By:** {author}", color=0xff0000)
        await strike_channel.send(embed=embed)
    with open("corrupt_faction.json", "w") as f:
        json.dump(factions, f)

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

@client.command()
async def snipe(ctx):
    with open("corrupt_snipe.json", "r") as f:
        data = json.load(f)
    snipe = data["message"]
    embed=discord.Embed(title="Message Snipe", description=f"**Latest Deleted Message** \n\n{snipe}")
    await ctx.send(embed=embed)



client.loop.create_task(ad())
client.run(Token)