import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from typing import Optional
load_dotenv()

token = os.environ['DISCORD_TOKEN']
guild_id = os.environ['DISCORD_GUILD_ID']
my_guild = discord.Object(id= guild_id )  # replace with your guild id


class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents().all())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=my_guild)
        await self.tree.sync(guild=my_guild)

client = MyClient()


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

@client.tree.command()
@app_commands.describe(
    usuario='La ID del usuario destinatario',
    mensaje='El mensaje que quiere enviar',
)
async def enviar(interaction: discord.Interaction, usuario: str , mensaje: str):

    user = client.get_user(int(usuario))
    if user:
        await user.send('Has recibido un mensaje anónimo: ' + mensaje)
        await interaction.response.send_message('Tu mensaje ya ha sido enviado')
    else:
        await interaction.response.send_message('No se ha encontrado ningún usuario con esa ID o no puedo enviarle mensajes porque no estamos en el mismo servidor o lo tiene bloqueado')

client.run(token)