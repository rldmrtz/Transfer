import discord
client = discord.Client()


@client.event
async def on_ready():
    print("Ready")
    
    
token = "token"
client.run(token)
