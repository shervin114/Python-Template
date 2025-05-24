import os
import discord
from discord.ext import commands

TOKEN = your token here

intents = discord.Intents.default() # intents here
intents.members = True
intents.message_content = True
intents.guilds = True
intents.voice_states = True
intents.emojis_and_stickers = True
intents.invites = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents) # you can change the cmd prefix

bot.run(TOKEN)
