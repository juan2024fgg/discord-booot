import model
import discord,os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token=os.getenv("dt")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='-', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(model.getclass(modelpath="./keras_model.h5",
                                          labelspath="labels.txt",
                                          imagepath=f"./{attachment.filename}"))
    else:
        await ctx.send("Olvidaste subir la imagen :(")



bot.run(token)