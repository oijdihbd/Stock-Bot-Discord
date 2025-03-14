import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)


async def load():
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.load_extension(f'commands.{filename[:-3]}')


@bot.event
async def on_message(message):
    if bot.user in message.mentions:
        prefix = "."  
        await message.channel.send(f"> My prefix is `{prefix}` \n Use `{prefix}help` for a list of commands.")

    await bot.process_commands(message)


async def main():
    await load(60s)
    await bot.start("MTM1MDEzMjU3NDMyODE5NzEzMQ.Gid_Oy.hgnQzRgGwLQY2Yft5Mm8WyC_-Vq8Q4hDBbhzb4")


asyncio.run(main())
