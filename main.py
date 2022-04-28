import Keep_Alive
import discord
from discord.ext import commands
import os

client_key = os.getenv("key")

intents = discord.Intents.default()
intents.members = True

testing = False

client = commands.Bot(command_prefix = "c!", case_insensitive = True, intents=intents)

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Músicas do Youtube"))
    print('Entramos como {0.user}'.format(client))



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

Keep_Alive.keep_alive()

client.run(client_key)