import os
import shutil

import discord
from dotenv import load_dotenv
import crawl_visualize

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # crawl_visualize.pre_pre_prework()
    print("Finished crawling data")

@client.event
async def on_message(message):
    if message.content.lower() == "calendar" and not message.author.bot:
        channel = message.channel
        await channel.send("calendar")

client.run(TOKEN)
