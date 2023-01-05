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

@client.tree.command(description="This command sends a anon message to a user by his user ID")
@app_commands.describe(
    usuario='The Destination user ID',
    mensaje='The message you want to send',
)
async def send(interaction: discord.Interaction, usuario: str , mensaje: str):

    user = client.get_user(int(usuario))
    if user:
        await user.send('You have recibed the next anon message: ' + mensaje)
        await interaction.response.send_message('Your message has been delivered')
    else:
        await interaction.response.send_message("Sorry the message coul not be delivered, maybe I'am not in the same server as the destination user or he has server DMs blocked")

@client.tree.command(description="Some help with the bot usage")
@app_commands.describe()
async def help(interaction: discord.Interaction):
  await interaction.response.send_message("For using this bot you have to use the /send command indicating the User ID of the target user ( this is how to find his user id https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-) and the message you want to send")


client.run(token)