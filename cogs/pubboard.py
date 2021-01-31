import discord
import asyncio
import json
import os
from discord.ext import commands, tasks
from datetime import datetime, timedelta
from pytz import timezone

##oh god here we fucking go
##this is prob gonna end up in a shitshow
##lets hope not ~~Anthonyjrvill

##btw for timezones to work put in 'pip install pytz'

class Publicboard(commands.Cog):

     def __init__(self, client):
         self.client = client

     @commands.command()
     async def addmessage(self, ctx, *, message):
         timestamp = str(datetime.now(timezone('US/Central')))
         emoji = '✔️'
         author = str(ctx.message.author)
         pfp = str(ctx.message.author.avatar_url)
         save = {
            'date': timestamp,
            'message': f'{message}',
            'user': author,
            'pfp': pfp
         }

         with open('public.json', 'w') as f:
             json.dump(save, f, indent=4)

         await ctx.message.add_reaction(emoji)

     @commands.command(aliases=["pubboard", "publicboard", "messageboard"])
     async def board(self, ctx):
         
         with open('public.json', 'r') as f:
                   save = json.load(f)

         author = ctx.message.author

         self.save = save

         date = self.save['date']
         avatar = self.save['pfp']

         embed = discord.Embed(colour=0xff7b00)
         embed.set_author(name="Public Board", icon_url=avatar)
         embed.add_field(name="Made by", value=f"{self.save['user']}", inline=True)
         embed.add_field(name="Sent at", value=f"{self.save['date']} CST", inline=True)
         embed.add_field(name="Message:", value=f"{self.save['message']}", inline=False)
         embed.set_footer(text="To add your own text use 'u!addmessage (message)'")

         await ctx.send(author, embed=embed)

def setup(client):
     client.add_cog(Publicboard(client))
     print('NOW USING PUBLICBOARD')