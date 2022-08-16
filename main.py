import discord
from discord.ext import commands
from webserver import keep_alive
import os

client = commands.Bot(command_prefix='c.', help_command=None)

@client.event
async def on_ready():
    print("i am online")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers"))


@client.event
async def on_command_error(ctx, error):

  
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='Error', description='You missed one or more arguments', color=discord.Color.red())
        embed.set_footer(text='Calculator')
        embed.timestamp = ctx.message.created_at
        await ctx.send(embed=embed)



@client.command(name='calculate', aliases=['calc'])
async def calculate(ctx, num1, operation, num2):

    if operation == '+':
       action = int(num1) + int(num2)
    elif operation == '-':
       action = int(num1) - int(num2)
    elif operation == '*':
       action = int(num1) * int(num2)
    elif operation == '/':
       action = int(num1) / int(num2)
        
      
      
    embed=discord.Embed(
        title='Result',
        description = f'{action}',
        color=discord.Color.teal()
    )
    embed.set_footer(text='Calculator')
    embed.timestamp = ctx.message.created_at

    if operation == '+':
        print(f'{num1, operation, num2} = {int(num1) + int(num2)}')
    elif operation == '*':
        print(f'{num1, operation, num2} = {int(num1) * int(num2)}')
    elif operation == '-':
        print(f'{num1, operation, num2} = {int(num1) - int(num2)}')
    elif operation == '/':
        print(f'{num1, operation, num2} = {int(num1) / int(num2)}')

    await ctx.send(embed=embed)
      
      

@client.command(name='links', aliases=['l', 'invite', 'supportserver', 'vote'])
async def links(ctx):
    embed=discord.Embed(title='Calculator - Links', color=discord.Color.dark_grey())
    embed.add_field(name='Invite Link', value='[Calculator - Bot Invite](https://discord.com/oauth2/authorize?client_id=996796279038418995&permissions=8&scope=bot)', inline=False)
    embed.add_field(name='Support Server', value='[Calculator - Support Server](https://shorturl.at/almQW)', inline=False)
    embed.add_field(name='Vote Us', value='[Calculator - Vote](https://top.gg/bot/996796279038418995/vote)', inline=False)
    embed.set_footer(text='Calculator')
    embed.timestamp = ctx.message.created_at

    await ctx.send(embed=embed)

@client.command(name='operations', aliases=['actions', 'o'])
async def operations(ctx):
    embed=discord.Embed(title='Calculator - Operations', color=discord.Color.purple())
    embed.add_field(name='**+**', value='This operation do addition', inline=False)
    embed.add_field(name='**-**', value='This operation do subtraction', inline=False)
    embed.add_field(name='*****', value='This operation do multiplication', inline=False)
    embed.add_field(name='**/**', value='This operation do division', inline=False)
    embed.set_footer(text='Calculator')
    embed.timestamp = ctx.message.created_at

    await ctx.send(embed=embed)
  

@client.command()
async def info(ctx):
  embed = discord.Embed(color=discord.Color.dark_green())
  embed.add_field(name='Author', value='The author of this bot is yoav.#8309', inline=False)
  embed.add_field(name='Hosting', value='This bot using "Replit" for 24/7 hosting',  inline=False)
  embed.add_field(name='Coding Language', value='This bot coded with "Python" and using the package "discord.py"')
  embed.set_footer(text='Calculator')
  embed.timestamp = ctx.message.created_at
  await ctx.send(embed=embed)
      
@client.command(name='help', aliases=['h', 'commands', 'command'])
async def help(ctx):
    embed=discord.Embed(title='Calculator - Commands', color=discord.Color.blurple())
    embed.add_field(name='c.calculate <exercise>', value='Calculate an math exercise', inline=False)
    embed.add_field(name='c.links', value='Send all of my links', inline=False)
    embed.add_field(name='c.operations', value='Give information about the operations', inline=False)
    embed.add_field(name='c.info', value='Send intersting information about the bot', inline=False)
    embed.add_field(name='Support Server', value='[Calculator - Support Server](https://shorturl.at/almQW)', inline=False)
    embed.set_footer(text='Calculator')
    embed.timestamp = ctx.message.created_at


    await ctx.send(embed=embed)


keep_alive()

TOKEN = os.environ.get("OTk2Nzk2Mjc5MDM4NDE4OTk1.GvoEIi.tU89Zw6P2rKzPYlkGmmrHQZR7tE-kAEsh2-f10")


client.run(TOKEN)