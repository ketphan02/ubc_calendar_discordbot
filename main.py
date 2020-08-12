import os

import discord
from dotenv import load_dotenv
import crawl_visualize

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    crawl_visualize.pre_pre_prework()

@client.event
async def on_message(message):
    if message.content.lower() == "calender":
        channel = message.channel
        await channel.send("I'm working on it...")

client.run(TOKEN)
