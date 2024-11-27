import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await ctx.send(f"Archivo guardado en ./{file_name }")
            await attachment.save(f"./{file_name}")
            try:
                clase = get_class("keras_model.h5","labels.txt",file_name)
                if clase[0] == "Gotico":
                    await ctx.send("el estilo gotico es caracterizado por tener un arte puntiagudo y detalles ornomentales")
                if clase[0] == "neoclasico":
                    await ctx.send("El arte neoclásico fue un movimiento artístico del siglo XVIII inspirado en la antigüedad grecorromana, que buscaba simplicidad, equilibrio y valores morales en contraste con los excesos del rococó. Caracterizado por su enfoque en la razón, la sobriedad y la simetría, destacó en arquitectura, pintura y escultura con temáticas históricas y heroicas, promoviendo ideales de virtud y civismo propios de la Ilustración.")
            except:
                await ctx.send("ocurrio un error")
    else:
        await ctx.send("Olvidaste subir una imagen) :(")
        




bot.run("tu token")