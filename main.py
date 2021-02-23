import discord
from discord import DMChannel
from replit import db
from discord.ext import commands
from keep_alive import keep_alive

import custom_math as cm

intents = discord.Intents.all()
client = commands.Bot(command_prefix="gd!", case_insensitive=True, intents_members=True)
intents = discord.Intents(messages=True, guilds=True)
c_name = "Gapla Dollars"

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('gd!help'))
  print("Bank of Gapla Bot is ready. \n")

@client.command(pass_context = True,help="Gives a person a starting balance")
async def sbal(ctx, args, *, args1):
    user = str(ctx.author.send)
    if user == "wyatt400":
      db[args] = float(args1)
      db[args1] = args
      await ctx.send("set " + args + " to " + args1 + f" {c_name}")

@client.command(help="Creates an account for you")
async def acc(ctx):
    user = str(ctx.author.name)
    db[user] = 0
    db[0] = user
    await ctx.send("Created " + user + "'s account!")

@client.command(pass_context = True, help=f"Gives {c_name} from the Federal Reserve to the user"
                )
async def add(ctx, args1, *, member):
    user = str(ctx.author.name)
    if user == "wyatt400":
        oldcur = db[member]
        db[member] = oldcur + float(args1)
        db[args1] = member
        currency = db[member]
        await ctx.send(member + " now has " + str(currency) + f" {c_name}!")
    else:
        await ctx.send("You do not have permission to use this command.")

@client.command(pass_context = True,help="See your balance")
async def bal(ctx):
    user = str(ctx.author.name)
    currency = db[user]
    embed = discord.Embed(
    title=user + "'s Balance",
    color=discord.Color.blue()
    )
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="User: ", value=user, inline=True)
    embed.add_field(name="Amount: ", value=str(currency) + f" {c_name}!", inline=True)
    await ctx.send(embed=embed)

@client.command(
    help="See other people's balances (use gd!bal \"username\", no ping or nick)"
)
async def obal(ctx, *, args):
    currency = db[args]
    embed = discord.Embed(
    title=args + "'s Balance",
    color=discord.Color.blue()
    )
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="User: ", value=args, inline=True)
    embed.add_field(name="Amount: ", value=str(currency) + f" {c_name}!", inline=True)
    await ctx.send(embed=embed)

@client.command(help="Deletes your account")
async def delete(ctx):
    user = str(ctx.author.name)
    val = db[user]
    if val < 0 or val > 0:
        await ctx.send(
            "You cannot delete your account because it has a balance or a debt."
        )
    else:
        del db[user]
        embed = discord.Embed(
        title="Account Deleted!",
        color=discord.Color.blue()
    )
        await ctx.send(embed=embed)

@client.command(help=f"The ability to gift people {c_name}!")
async def gift(ctx, args1, *, member):
    user = str(ctx.author.name)
    oldcur = db[user]
    db[user] = oldcur - int(args1)
    if db[user] < 0:
        db[user] = oldcur
        await ctx.send("You have an insufficent balance.")
    elif "-" in args1:
      await ctx.send(f"You cannot send negative amounts of {c_name}.")
    else:
      new = db[user]
      db[new] = user
      oldcur = db[member]
      db[member] = oldcur + int(args1)
      db[args1] = member
      embed = discord.Embed(
      title="Gift!",
      color=discord.Color.blue()
    )
      embed.set_thumbnail(url="https://www.brianhe.com/images/portfolio/thumb/6.jpg")
      embed.add_field(name="Gifter", value=user, inline=False)
      embed.add_field(name="Reciver", value=member, inline=False)
      embed.add_field(name=f"Amount Gifted {c_name}", value=args1, inline=True)
      await ctx.send(embed=embed)

@client.command(help = "Send BRUHisbackbois ideas and other stuff!", pass_context = True)
async def ask(ctx, *, value):
  user_ = str(ctx.author.name)
  user = await client.fetch_user("769007255700897822")
  embed = discord.Embed(
      title="[--Note--]",
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.add_field(name="User: ", value=user_, inline=True)
  embed.add_field(name="Description", value=value, inline=True)
  await DMChannel.send(user, embed=embed)
  
@client.command(help = "Version and copyright info for the Bank of Gapla bot.")
async def info(ctx):
    embed = discord.Embed(
    title="Info",
    color=discord.Color.blue()
    )
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="Info: ", value="Bank of Gapla Bot v2.5 STABLE. Created by BRUHisbackbois for the Government of the Federated States of Gapla. Ask for source code using gd!ask.", inline=True)
    embed.add_field(name="How to contact: ", value="gd!ask '<question>' ", inline=True)
    await ctx.send(embed=embed)

@client.command(help = "Does stuff.")
async def stuff(ctx):
  await ctx.author.send("Click this link for more projects by BRUHisbackbois: https://machinelearningbasics.codeninja135.repl.co")

keep_alive()

#This is the line where the token usually goes, but we're not putting it here for security reasons.
