import os
import time
import ctypes
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("Discord Bot Maker | Supelion")

print("\n\n" + "-" * 10 + " Welcome to the Discord Bot Maker! " + "-" * 10)
time.sleep(2)
setupType = input("\n\nSelect a setup type (simple / advanced): ")

if setupType.lower() == "simple":
    # Asking the user for the discord bot token
    botToken = input("\nPlease input your discord bot token here: ")
    # Asking the user for the command prefix (why are you even reading this lmao)
    commandPrefix = input("\nPlease enter the bot's prefix: ")

    #Creating executeMe.py
    with open("executeMe.py", "w") as f:
        f.write(f"""import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix = '{commandPrefix}')

@bot.event
async def on_ready():
    print("I'm Online!")

@bot.command()
async def hi(ctx):
    await ctx.send("Hello from the self made bot!")

@bot.command()
async def ping(ctx):
    
    ping = round(bot.latency * 1000)
    
    pingembed = discord.Embed(color = 0x2f3136)
    
    pingembed.add_field(name = "Pong!", value = f'""" + "{ping}" + f""" ms')
    
    await ctx.reply(embed=pingembed, mention_author=False)
""" + """
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
""" + f"""

bot.run('{botToken}')""")

    # Success message and giving some info to the user.
    print("\n\nDone!")

elif setupType.lower() == "advanced":
    # Asking the user for the discord bot token
    botToken = input("\nPlease input your discord bot token here: ")
    # Asking the user for the command prefix (why are you even reading this lmao)
    commandPrefix = input("\nPlease enter the bot's prefix: ")
    # Asking user if the command prefix should be case insensitive
    case = input("\nShould the Prefix be case insensitive? (yes or no) ")
    # Checking the input of the user
    if case.lower() == "yes":
        case = True
    elif case.lower() == "no":
        case = False
    else:
        print("Please only enter yes or no!")
    # Asking the user what to send back to the "hi" command
    whatToSayToHiCommand = input("\nPlease enter what the bot should respond to the 'hi' command: ")

    #Creating executeMe.py
    with open("executeMe.py", "w") as f:
        f.write(f"""import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix = '{commandPrefix}', case_insensitive = {case})

@bot.event
async def on_ready():
    print("I'm Online!")

@bot.command()
async def hi(ctx):
    await ctx.send("{whatToSayToHiCommand}""" + f"""")

@bot.command()
async def ping(ctx):
    
    ping = round(bot.latency * 1000)
    
    pingembed = discord.Embed(color = 0x2f3136)
    
    pingembed.add_field(name = "Pong!", value = f'""" + "{ping}" + f""" ms')
    
    await ctx.reply(embed=pingembed, mention_author=False)
""" + """
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)
""" + f"""

bot.run('{botToken}')""")

    # Success message and giving some info to the user.
    print("\n\nDone!")

else:
    print("Please only enter simple OR advanced!")
