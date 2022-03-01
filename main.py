import discord, requests, json
from discord.ext import commands
from config import settings
bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command()
async def rat(ctx):
    author = ctx.message.author
    response = requests.get('https://raw.githubusercontent.com/thisisignitedoreo/thisisignitedoreo.github.io/main/rat.json')
    json_data = json.loads(response.text)
    await ctx.send(f'{author.mention}, последняя версия RatLauncher: {json_data["ver"]}.\nСкачать ты его можешь сдесь: {json_data["link"]}')
@bot.command()
async def randcat(ctx):
	response = requests.get('https://aws.random.cat/meow')
	json_data = json.loads(response.text)
	embed = discord.Embed(color = 0x20B2AA, title = 'Рандомный котик') # Создание Embed'a
	embed.set_image(url = json_data['file'])
	await ctx.send(embed = embed) # Отправляем Embed
@bot.command()
async def randfox(ctx):
	response = requests.get('https://randomfox.ca/floof/')
	json_data = json.loads(response.text)
	embed = discord.Embed(color = 0xFF4500, title = 'Рандомная лиса') # Создание Embed'a
	embed.set_image(url = json_data['image'])
	await ctx.send(embed = embed) # Отправляем Embed
@bot.command()
async def randdog(ctx):
	response = requests.get('https://random.dog/woof.json')
	json_data = json.loads(response.text)
	embed = discord.Embed(color = 0x8B4513, title = 'Рандомная собака') # Создание Embed'a
	embed.set_image(url = json_data['url'])
	await ctx.send(embed = embed) # Отправляем Embed
bot.run(settings['token'])
