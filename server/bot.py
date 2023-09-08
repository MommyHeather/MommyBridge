import aiofiles
import discord
from discord.ext import commands
import asyncio

## EDIT THESE VALUES TO MATCH YOUR NEEDS
bot_prefix = ">"
with open("TOKEN") as f:
    bot_token = f.read()
cogs = ["cogs.chatbridge", 'jishaku'] #all cogs to load - these are bot cogs, not related to server>## END VALUES

bot = commands.Bot(command_prefix=commands.when_mentioned_or(bot_prefix), allowed_mentions=discord.AllowedMentions.users())