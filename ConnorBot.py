import discord
import random

TOKEN = 'ODcxMTY4NTU0MDk4MTMwOTU0.YQXY8A.mneWhS8wxZuHw4IsDH0_kDAMJjM'

client = discord.Client()

@client.event
async def on_ready():
	print('My name is Connor. I’m the android sent by CyberLife to simp for Haruka.'.format(client))
	

@client.event
async def on_message(message):
	username = str(message.author).split('#')[0]
	user_message = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {user_message} ({channel})')

client.run(TOKEN)