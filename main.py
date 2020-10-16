import discord # All I know is pain
from discord.ext import commands, tasks
client = commands.Bot(
    command_prefix="^",  # Don't make it a closed diamond bracket
    description="the tutorial girl is hot >:D",  # Actual comment on our video game
    owner_id=212949132577341440,  # Hi, I'm Keiron!
    case_insensitive=True)

# here are all the events im gonna make this thing
# I actually dont think i have enough algorithms to fill a single page
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(client.command_prefix + 'hello'):
        await message.channel.send('Subscribe to keirontravis on Twitch')
    if message.content.startswith(client.command_prefix + 'test'):
        await message.channel.send(message)  # (I brute forced it, yay)
@client.command
async def command(ctx):
  await ctx.send("Lunara")

# ok now that's all setup we just have to run the damn thing
client.run(
    'NzE4MDQ3MDM5NDE3NDgzMzI2.XtjMTA.2zZFZRPwhjjEfkx8g0thAKvDA8Y',
    bot=True,
    reconnect=True)
# Shoutout to the programmer from gov.uk who wrote "Thanks Martha" as the last line of the html file. That line lives in my mind free of charge, and now i write funny comments in my source codes. Anyway, subscribe to keirontravis on Twitch!