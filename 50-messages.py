import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
client = commands.Bot(
    command_prefix="$",
    help_command=None,
    intents=intents
)

#---------------------------------------------------------------------------------------------------
# Start vom Bot
#--------------------------------------------------------------------------------------------------
@client.event
async def on_connect():
    print("[Ich habe mich eingeloggt]...")
    await client.wait_until_ready()
    channel = client.get_channel()#channel_id
    for x in range(50,0,-1):
        await channel.send(x)
        
client.run("Bot-Token")
