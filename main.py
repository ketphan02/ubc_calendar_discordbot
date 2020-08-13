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
    # crawl_visualize.start()
    print("Finished crawling data")

@client.event
async def on_message(message):

    path = './'
    if message.author.bot:
        return

    if message.content.lower() == "/calendar":
        channel = message.channel
        await channel.send("What is your campus?\n1. Vancouver\n2. Okanagan")

        usr_data = await client.wait_for('message')
        msg = usr_data.content
        if msg == '2':
            path = path + 'okanagan/'
            directory = os.listdir(path)
            msg = "What is your Faculty?\n"
            for i in range(len(directory)):
                msg = msg + str(i + 1) + '. ' + directory[i] + '\n'
            await channel.send(msg)

            usr_data = await client.wait_for('message')
            msg = usr_data.content
            msg = int(msg) - 1
            path = path + directory[msg] + '/'
            directory = os.listdir(path)
            msg = "What is your Program?\n"
            for i in range(len(directory)):
                msg = msg + str(i + 1) + '. ' + directory[i] + '\n'
            await channel.send(msg)

            usr_data = await client.wait_for('message')
            msg = usr_data.content
            msg = int(msg) - 1
            path = path + directory[msg] + '/'
            directory = os.listdir(path)
            msg = "What is your Major?\n"
            for i in range(len(directory)):
                msg = msg + str(i + 1) + '. ' + directory[i].replace(".csv", "") + '\n'
            await channel.send(msg)
            
            usr_data = await client.wait_for('message')
            msg = usr_data.content
            msg = int(msg) - 1
            path = path + directory[msg]
            
            # col_names = ["INFO", "CREDIT"]
            data = pd.read_csv(path)
            await channel.send(data)
            print(data)


client.run(TOKEN)


"""
UPLOAD

git add .
git commit -m "update"
git push origin master

"""