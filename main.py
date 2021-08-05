setupType = input("Select a setup type (simple / advanced): ")

if setupType == "simple":
    # Asking the user for the discord bot token
    discordBotToken = input("Please input your discord bot token here: ")
    botToken = str(discordBotToken)
    # Asking the user for the command prefix (why are you even reading this lmao)
    commandPrefix = input("Please enter the bot's prefix: ")

    #Creating executeMe.py
    with open("executeMe.py", "w") as f:
        f.write(f"""import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '{commandPrefix}')

@client.event
async def on_ready():
    print("I'm Online!")

@client.command()
async def hi(ctx):
    await ctx.send("Hello from the self made bot!")

client.run('{botToken}')""")

    # Closing the file
    f.close()

    # Success message and giving some info to the user.
    print("Done! The only command available as of right now, is 'hi'.")

elif setupType == "advanced":
    # Asking the user for the discord bot token
    discordBotToken = input("Please input your discord bot token here: ")
    botToken = str(discordBotToken)
    # Asking the user for the command prefix (why are you even reading this lmao)
    commandPrefix = input("Please enter the bot's prefix: ")
    # Asking user if the command prefix should be case insensitive
    isCaseSensitive = input("Should the Prefix be case insensitive? (yes or no) ")
    # Checking the input of the user
    if isCaseSensitive == "yes":
        case = True
    elif isCaseSensitive == "no":
        case = False
    else:
        print("Please only enter yes or no!")
    # Asking the user what to send back to the "hi" command
    whatToSayToHiCommand = input("Please enter what the bot should respond to the 'hi' command: ")

    #Creating executeMe.py
    with open("executeMe.py", "w") as f:
        f.write(f"""import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '{commandPrefix}', case_insensitive = {case})

@client.event
async def on_ready():
    print("I'm Online!")

@client.command()
async def hi(ctx):
    await ctx.send("{whatToSayToHiCommand}""" + f"""")

client.run('{botToken}')""")

    # Closing the file
    f.close()

    # Success message and giving some info to the user.
    print("Done! The only command available as of right now, is 'hi'.")

else:
    print("Please only enter simple OR advanced!")