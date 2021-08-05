import os
import random

#import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client = discord.Client()

bot = commands.Bot(command_prefix = '!')

'''
@client.event
async def on_message(message):
	if message.author == client.user:
		return
'''

@bot.event
async def on_ready():
	print('My name is Connor. I’m the android sent by CyberLife to simp for Haruka.')

@bot.command(name = 'Connor', intro = 'Intro')
async def connorIntro(ctx):
	response = 'My name is Connor. I’m the android sent by CyberLife to simp for Haruka.'
	await ctx.send(response)
	#if message.content == 'HEY CONNOR!':
		
		

bot.run(TOKEN)

#Everything below this point was the original code to try and get this to work
#Simply put, NONE OF THIS WORKED

'''
import os
import discord
import random

import Config

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

Token = Config.TOKEN

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
			@bot.command(name=commandname) 
'''
