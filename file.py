import discord
from discord.ext import commands
import random  # Aggiungi questa importazione per utilizzare la funzione random.choice
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()  # Aggiungi questo decoratore per trasformare la funzione in un sotto-comando
async def meme(ctx):
    cringe_memes = ['images/cringe_meme1.png', 'images/cringe_meme2.png', 'images/cringe_meme3.png', 'images/cringe_meme4.png', 'images/cringe_meme5.png', 'images/cringe_meme6.png', 'images/cringe_meme7.png', 'images/cringe_meme8.png', 'images/cringe_meme9.png', ]
    random_meme = random.choice(cringe_memes)
    
    with open(random_meme, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def cat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()
    
    cat_image_url = data[0]['url']

    embed = discord.Embed()
    embed.set_image(url=cat_image_url)

    await ctx.send(embed=embed)

bot.run("MTE5OTM5MzA4NDgwMzM4MzM0Ng.GJfbfq.M-09RZEdnv9Wlw1ljhmRzdk-AK9Dl0KzCAZyKc")
