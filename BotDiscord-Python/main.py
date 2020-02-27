import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from discord.ext.commands.cooldowns import BucketType
from random import randint
token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
Client=discord.Client()
client=commands.Bot(command_prefix="didac!")

@client.event
async def on_ready():
    print("Bot lancé !")

@client.command(pass_context=True)
async def roll(ctx, nb_max:int):
    embed=discord.Embed(
        title="Lancé de {}".format(ctx.message.author.name),
        description="Résultat : {}".format(randint(1,nb_max))

    )
    embed.add_field(
        name="Tu veux toi aussi lancer un dé ?",
        value="Alors fait didac!roll <nombre maximum>",
        inline=True
    )
    await client.send_message(ctx.message.author,embed=embed)
    pass


client.run(token)
