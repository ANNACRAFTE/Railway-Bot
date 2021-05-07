import discord
from discord.ext import commands
from discord import Game
from discord.ext.commands import Bot
from pip._vendor import requests
import datetime
import json
import mysql.connector
import asyncio
# Bots token
token = 'BOT TOKEN'

# Bots prefix (add one by default its !)
bot = commands.Bot(command_prefix=('PREFIX'))

# Request to add a train
@bot.command()
async def requestadd(ctx,  **args):
    await ctx.message.delete()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )
    mycursor = mydb.cursor()
    sql = f""
    mycursor.execute(sql)
    mydb.commit()
    replymessage = discord.Embed(title="", color=0x00FF00,
                                     description="")
    await ctx.send(embed=replymessage)


# Request to remove a train
@bot.command()
async def requestremove(ctx, **args):
    await ctx.message.delete()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )
    mycursor = mydb.cursor()
    sql = f""
    mycursor.execute(sql)
    mydb.commit()
    replymessage = discord.Embed(title="", color=0x00FF00,
                                     description="")
    await ctx.send(embed=replymessage)

# Request to remove a train
@bot.command()
async def requestedit(ctx, **args):        
    await ctx.message.delete()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=""
    )
    mycursor = mydb.cursor()
    sql = f""
    mycursor.execute(sql)
    mydb.commit()
    replymessage = discord.Embed(title="", color=0x00FF00,
                                     description="")
    await ctx.send(embed=replymessage)

# notes: 
# just a template. 
    
    
# run the bot
bot.run(token, bot=True)
