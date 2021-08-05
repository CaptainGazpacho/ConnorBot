import discord
import random

TOKEN = 'ODcxMTY4NTU0MDk4MTMwOTU0.YQXY8A.1_doJi4Xdq4opgNIuQu8EqVL-Fc'

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
	
	#if message.author == 'ConnorBot#8331':
		#return
		
	if message.author != 'ConnorBot#8331':
		if user_message.lower() == '!Connor':
			print('My name is Connor. I’m the android sent by CyberLife to simp for Haruka.')
			await message.channel.send('My name is Connor. I’m the android sent by CyberLife to simp for Haruka.')
			return

client.run(TOKEN)