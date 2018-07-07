import discord
from discord.ext import commands
from twilio.rest import Client

bot = commands.Bot(command_prefix='!')

#Twilio creds
account_sid = "ACc6af640dd8dff28b9959ada7bc7d53ed"
# Your Auth Token from twilio.com/console
auth_token  = "a65f6d085d0c94cb0204c3db32341a6a"
client = Client(account_sid, auth_token)
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
    #os.system("twilbot.py " + arg1 + ' ' + arg2)
    await ctx.send('Sending an SMS message to {} to play Overwatch right now!'.format(arg1))


bot.run('NDY0OTA5ODk2ODUzNDg3NjE4.DiGAfA.orkfIFgUA3cqCcXTbZPMVFaTiik')