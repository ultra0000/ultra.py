import discord
import random
import urllib
import requests
import bs4
from discord.ext import commands

client = commands.Bot(command_prefix = 'u!')

@client.event
async def on_ready():
  print('Running!')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! Latency is {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
  await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['search'])
async def google(ctx, *, query):
  searchInput = "https://google.com/search?q="+urllib.parse.quote(query)
  res = requests.get(searchInput)
  res.raise_for_status()
  soup = bs4.BeautifulSoup(res.text, "html.parser")
  linkElements = soup.select('div#main > div > div > div > a')
  if len(linkElements) == 0:
    await ctx.send("Couldn't find any results...")
  else:
    link = linkElements[0].get("href")
    i = 0
    while link[0:4] != "/url" or link[14:20] == "google":
      i += 1
      link = linkElements[i].get("href")
  await ctx.send("Result: \nhttp://google.com"+link)

@client.command()
async def say(ctx, *, text):
  text_components = text.split()
  if "@everyone" in text_components or "@here" in text_components:
      await ctx.send("You cannot have \"everyone\" or \"here\" in your message!")
      return
  await ctx.message.delete()
  await ctx.send(text)


client.run(TOKEN)