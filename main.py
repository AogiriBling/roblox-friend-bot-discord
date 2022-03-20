import os
from discord.ext import commands 
import discord, requests, random, threading, asyncio
from webserver import keep_alive

my_secret = os.environ['token']
token = os.environ['token']

with open('cookies.txt', 'r') as cookies:
    cookies1 = cookies.read().splitlines()

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Bot is online!')

def add_user(cookie, userid):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
            session.post(f'https://friends.roblox.com/v1/users/{userid}/request-friendship')
    except:
        pass



@bot.command()
async def friends(ctx, userId):
    await ctx.send(f'<@{ctx.author.id}>, **Started Sending "1050" friend Requests..check your friends requests!** ```WARNING ONLY THOSE WHO HAVE USED ON THEMSELF ONCE IT WONT WORK ON THEM AGAIN TRY SOME OTHER ID!``` **Enjoy!** `Aogiri`  https://i.vgy.me/fQaC8I.png ')
    for x in cookies1:
        threading.Thread(target=add_user, args=(x, userId,)).start()
            
keep_alive()
bot.run(token)
