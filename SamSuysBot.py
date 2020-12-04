# bot.py
import os
from dotenv import load_dotenv

from datetime import datetime
import threading

import discord
from discord.ext import commands
import asyncio

load_dotenv()

client = commands.Bot(command_prefix='!')#discord.Client()

def checkTime():
    # This function runs periodically every 1 second
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    if(current_time == '21:55:30'):  # check if matches with the desired time
        print('sending message')


checkTime()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def send_anonymous_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(content) # send whatever in the content to the mentioned user.

client.run(os.environ['DISCORD_TOKEN'])
