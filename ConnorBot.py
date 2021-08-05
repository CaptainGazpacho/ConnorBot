#Author: Captain Gazpacho
#Date Completed: Aug XX 2021
#Special Thanks: Phantom Cultist Ryuk, Darth Yog, High Inquisitor

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

@bot.command(name = 'ConnorHelp', help = 'Gives help for all commands')
async def ConnorHelp(ctx):
	response = 'Here is a list of the available commands:\n\n!ConnorHelp - Gives help for all commands\n!ConnorIntro - Makes the bot introduce itself\n!ConnorSimp - Makes Connor simp for Haruka\n!ConnorGif - Plays a random Connor Gif\n!ConnorQuote - Shows a random Connor quote'
	await ctx.send(response)

@bot.command(name = 'ConnorIntro', help = 'Makes the bot introduce itself')
async def ConnorIntro(ctx):
	response = 'My name is Connor. I’m the android sent by CyberLife to simp for Haruka.'
	await ctx.send(response)
	
@bot.command(name = 'ConnorSimp', help = 'Makes Connor simp for Haruka')
async def ConnorSimp(ctx):
	response = 'Haruka, I find your antlers to be most, beautiful my lady'
	await ctx.send(response)
	
@bot.command(name = 'ConnorGif', help = 'Plays a random Connor Gif')
async def ConnorGif(ctx):
	Connor_Gifs = ['https://tenor.com/view/connor-bryan-dechart-detroit-become-human-dbh-gif-14745350', 'https://tenor.com/view/connor-hank-detroit-become-human-gif-12327020', 'https://tenor.com/view/connor-detroit-detroit-become-human-gif-15593015', 'https://tenor.com/view/wink-connor-detroit-become-human-video-game-gif-17810333', 'https://tenor.com/view/connor-detroit-become-human-dbh-excited-shoulder-wiggle-gif-12020038'
	]
	response = random.choice(Connor_Gifs)
	await ctx.send(response)

@bot.command(name = 'ConnorQuote', help = 'Shows a random Connor quote')
async def ConnorQuote(ctx):
	Connor_Quotes = ['28 stab wounds. You didn\'t want to leave him a chance, huh?', 'I like dogs.', 'I\'m not programmed to say things like this, but... I really appreciated working with you. With a little more time, who knows... We might\'ve even become friends...'
	]
	response = random.choice(Connor_Quotes)
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
