import discord
import asyncio
import os
from discord.ext import commands

class Ultrahelp(commands.Cog):

     def __init__(self, client):
           self.client = client

     @commands.command(aliases=["commands", "help"])
     async def _commands1(self, ctx):

         author = ctx.message.author

         embed = discord.Embed(colour=0x0000ff)

         embed.set_author(name="ultra.py's Commands Pg. 1")
         embed.add_field(name="u!google", value="Google anything you desire", inline=False)
         embed.add_field(name="u!8ball", value="Use the all mighty magical 8ball", inline=False)
         embed.add_field(name="u!ping", value="Checks your latency", inline=False)
         embed.add_field(name="u!say", value="Gives you the power to make the bot say whatever you want", inline=False)
         embed.set_footer(text="For page 2 of the commands type 'u!commands2 \ help2'")

         await ctx.send(author, embed=embed)

     @commands.command(aliases=["commands2", "help2"])
     async def _commands2(self, ctx):

         author = ctx.message.author

         embed = discord.Embed(colour=0x0000ff)

         embed.set_author(name="ultra.py's Commands Pg. 2")
         embed.add_field(name="uhh", value="Nothings in here until more commands come out.")

         await ctx.send(author, embed=embed)

def setup(client):
     client.add_cog(Ultrahelp(client))
     print('NOW USING ULTRAHELP SYSTEM. made by anthony :)')