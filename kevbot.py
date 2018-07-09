import discord
from discord.ext import commands
from twilio.rest import Client
from kevbotconfig import *  



bot = commands.Bot(command_prefix='!')

#client = Client(account_sid, auth_token)
users = {"Kevin": "+18056987435"}

person = ""
content = ""


def SendMessage(person, content):
    message = client.messages.create(
        to=users.get(person), 
        from_="+18055002584",
        body=content)
    print(message.sid)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def alert(ctx, arg1):
    SendMessage(arg1, "Get on Overwatch!")
    await ctx.send('Sending an SMS message to {} to play Overwatch right now!'.format(arg1))

@bot.event
async def on_member_update(before, after):
    print(after.game)
    SendMessage(Kevin,'test')



bot.run(discordToken)