import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send(f'Hola, soy un bot {client.user}!')

    elif message.content.startswith('$help'):
        help_text = (
            "Lista de comandos disponibles:"
            "$hello saluda"
            "$heh repite 'heh' n veces"
            "$ppt <piedra/papel/tijera>` juega piedra papel o tijera"
            "$pass <largo> genera una contraseña"
            "$coin lanza una moneda"
            "$roll <lados> tira un dado"
            "$joke cuenta un chiste"
            "$help muestra este mensaje"
        )
        await message.channel.send(help_text)

    elif message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)

    elif message.content.startswith('$ppt'):
        opciones = ["piedra", "papel", "tijera"]
        user_choice = message.content[5:].lower()

        if user_choice not in opciones:
            await message.channel.send("Elige: piedra, papel o tijera.")
            return

        bot_choice = random.choice(opciones)

        if user_choice == bot_choice:
            resultado = "Empate."
        elif (user_choice == "piedra" and bot_choice == "tijera") or \
             (user_choice == "papel" and bot_choice == "piedra") or \
             (user_choice == "tijera" and bot_choice == "papel"):
            resultado = "Ganaste!"
        else:
            resultado = "Perdiste!"

        await message.channel.send(f"Tú: {user_choice}\nBot: {bot_choice}\n{resultado}")

    elif message.content.startswith('$pass'):
        try:
            length = int(message.content[6:])
        except:
            length = 8

        elements = "+-/*!&$#?=@<>"
        password = "".join(random.choice(elements) for _ in range(length))

        await message.channel.send(f"Tu contraseña: `{password}`")

    elif message.content.startswith('$coin'):
        flip = random.choice(["HEADS", "TAILS"])
        await message.channel.send(f"La moneda cayó en: **{flip}**")

    elif message.content.startswith('$roll'):
        try:
            sides = int(message.content[6:])
            if sides < 2:
                await message.channel.send("Elige un número de lados mayor a 1.")
                return
        except:
            sides = 6  

        result = random.randint(1, sides)
        await message.channel.send(f"🎲 Resultado: **{result}** de {sides}")

    elif message.content.startswith('$joke'):
        jokes = [
            "Error 404: chiste no encontrado.",
            "Mi código funciona. No sé por qué, pero funciona.",
            "Cual es el colmo de Aladin, tener mal genio"
        ]
        await message.channel.send(random.choice(jokes))
    
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

    
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)

client.run("MTQzNDYzNTgzNzA5NzY0NDA0Mg.Gk_HV9.Uq2Uf324UaBm0lBuwAyXj5ZCIQd1ARMOpXtVsM")
