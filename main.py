from ast import alias
from unicodedata import name
import random
import discord
from discord.ext.commands import *
from googleapiclient.discovery import build
import json


api_key="AIzaSyCrirDLATf_s1YloBRGMV6AaqeUfq2cI2g"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = Bot(command_prefix=".", intents=intents);
token = "" #Token here

@bot.event
async def on_ready():
    print("ready for using discord bot!");
    

@bot.command(aliases = ['hi','chào','chao','yo'])
async def hello(ctx):
    member = ctx.author
    await ctx.send(f"{member.mention} quen không mà gọi nhau ?");

@bot.command(name = "random",aliases = ['rd'])
async def _random(ctx, min, max):
    member = ctx.author
    embed=discord.Embed(title="Anh Tom đỏ đen", description="Gánh nặng luôn đặt lên đôi vai ta", color=0x5cb85c)
    embed.add_field(name="Con số định mệnh:", value=f"```{random.randint(int(min),int(max))}```", inline=True)
    embed.set_footer(text=f"{member}")
    await ctx.send(embed=embed)

@bot.command(aliases = ['avt'])
async def avatar(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed=discord.Embed(title=f"Avatar of {member.name}", color=0x5cb85c)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=ctx.message.created_at)
    await ctx.send(embed=embed)
    
@bot.command(aliases = ['s'])
async def search(ctx, *,search):
    temp = search
    randomlist = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="9d5a2b9a4430a335f", searchType="image"
    ).execute()
    url = result["items"][randomlist]["link"]
    embed = discord.Embed(title=f"Ảnh {temp}")
    embed.set_image(url=url)
    await ctx.send(embed=embed)
bot.run(token)

