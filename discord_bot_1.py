import discord

client = discord.Client()
#token = open("token.txt","r").read()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.content}")
    if "ciao" in message.content.lower():
        await message.channel.send(f"Buongiorno, {message.author}")

client.run("NTEwMTE4NjA5ODY4MjkyMTQ2.DsXvkA.s0vsT8fdRVeBmaea7FVRFTTnx2Y")
