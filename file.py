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

def get_dog_image_url():    
    url = 'https://dog.ceo/api/breeds/image/random'
    res = requests.get(url)
    data = res.json()
    return data['message']

@bot.command('dog')
async def dog(ctx):
    '''Una volta chiamato il comando dog, il programma richiama la funzione get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)


@bot.command()
async def pokedex(ctx, pokemon_name):
    # Costruisci l'URL per ottenere informazioni sul Pokémon specificato
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    
    # Fai una richiesta all'API per ottenere dati sul Pokémon
    response = requests.get(url)
    
    # Controlla se la richiesta ha avuto successo (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Estrai le informazioni desiderate dal JSON della risposta
        pokemon_id = data['id']
        pokemon_types = [t['type']['name'] for t in data['types']]
        pokemon_image_url = data['sprites']['front_default']
        
        # Costruisci un messaggio con le informazioni di base del Pokémon
        embed = discord.Embed(title=f"**Informazioni su {pokemon_name.capitalize()}**", color=0xffd700)
        embed.add_field(name="ID", value=pokemon_id, inline=True)
        embed.add_field(name="Tipo/i", value=", ".join(pokemon_types), inline=True)
        embed.set_image(url=pokemon_image_url)
        
        # Aggiungi ulteriori campi per gli attacchi e la loro efficacia
        embed = await add_attack_info(embed, data)
        
        # Invia il messaggio al canale
        await ctx.send(embed=embed)
    else:
        # Se la richiesta fallisce, invia un messaggio di errore
        await ctx.send(f"Errore nell'ottenere informazioni su {pokemon_name.capitalize()}.")

async def add_attack_info(embed, pokemon_data):
    # Estrai informazioni sugli attacchi
    abilities = []
    for ability in pokemon_data['abilities']:
        abilities.append(ability['ability']['name'])

    # Aggiungi informazioni sugli attacchi all'embed
    embed.add_field(name="Abilità", value=", ".join(abilities), inline=False)
    
    return embed


bot.run("MTE5OTM5MzA4NDgwMzM4MzM0Ng.GRAa4I.SNm3Ze6CPHhjlwsBK-_UyedFOonuegVY5-Rocw")
