import discord


client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$uff'):
        await message.channel.send('uff uff!')
