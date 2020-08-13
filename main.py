import os
import shutil

import discord
from dotenv import load_dotenv
import crawl_visualize
import pandas as pd

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    crawl_visualize.start() # This takes too much time
    print("Finished crawling data")

@client.event
async def on_message(message):

    path = './courses/'
    if message.author.bot:
        return

    if message.content.lower() == "/calendar":
        channel = message.channel
        await channel.send("What is your campus?\n1. Vancouver\n2. Okanagan")
        directory = os.listdir(path)
        
        await template("What is your Faculty?", client, path, directory, channel)

        await template("What is your Program?", client, path, directory, channel)

        await template("What is your Major?", client, path, directory, channel)
        
        usr_data = await client.wait_for('message')
        msg = usr_data.content
        msg = int(msg) - 1
        path = path + directory[msg]
        
        # col_names = ["INFO", "CREDIT"]
        data = pd.read_csv(path)
        await channel.send(data)
        print(data)


async def template(question, client, path, directory, channel):
    usr_data = await client.wait_for('message')
    msg = usr_data.content
    msg = int(msg) - 1
    path = path + directory[msg] + '/'
    directory = os.listdir(path)
    msg = question + '\n'
    for i in range(len(directory)):
        msg = msg + str(i + 1) + '. ' + directory[i] + '\n'
    await channel.send(msg)

client.run(TOKEN)


"""
UPLOAD

git add .
git commit -m "update"
git push origin master

"""