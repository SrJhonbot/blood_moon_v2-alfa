
import discord

import datetime
import time
import random
import os 

from datetime import datetime
from discord.ext import commands
from colorama import Fore, Style
from discord import Webhook

token = input("Token | ")

q_self = input("Modo self-bot on? (Y/N) : ")

if q_self == "Y" and "y":
    q_self = True
elif q_self == "N" and "n":
    q_self = False



client = commands.Bot(command_prefix=f"?",self_bot=q_self,help_command=None)

dt = datetime.now()
dt_format = dt.strftime("%H:%M")


__usuario__ = f"a"
__criadores__ = "Nux#8340 | Space.py#7528 | sr.master#6679"
__versao__ = "V2"

msgs = ["||@everyone|| Fracos, vocês sucumbiram perante o poder do blood moon","||@everyone|| HAHAHAHA! A LUA DE SANGUE CHEGOU E COM ELA VEIO O CAOS!","||@everyone|| ISSO É BLOOD MOON REQUIEM","||@everyone|| BLOOD MOON!","||@everyone|| FODIDOS PELA NORUEGA!"]
ch = {"NORUEGA DOMINA!","NORUEGA QUE MANDA AQUI!","NOSSO SERVIDOR","NORUEGA PASSOU E DOMINOU AQUI!","NORUEGA É DONA DAQUI!"}
time.sleep(3)
os.system(command="cls")
print(Fore.LIGHTBLACK_EX + "Loading...")
time.sleep(4)
os.system(command="cls")
time.sleep(3)
print(Fore.LIGHTWHITE_EX + f"""
        ██████╗██╗     ██████╗ ██████╗██████╗     ███╗   ███╗██████╗ ██████╗███╗   ██╗    ██╗   ████████╗ 
        ██╔══████║    ██╔═██████╔═██████╔══██╗    ████╗ ██████╔═══████╔═══██████╗  ██║    ██║   ██╚════██╗
        ██████╔██║    ██║██╔████║██╔████║  ██║    ██╔████╔████║   ████║   ████╔██╗ ██║    ██║   ██║█████╔╝
        ██╔══████║    ████╔╝██████╔╝████║  ██║    ██║╚██╔╝████║   ████║   ████║╚██╗██║    ╚██╗ ██╔██╔═══╝ 
        ██████╔███████╚██████╔╚██████╔██████╔╝    ██║ ╚═╝ ██╚██████╔╚██████╔██║ ╚████║     ╚████╔╝███████╗
        ╚═════╝╚══════╝╚═════╝ ╚═════╝╚═════╝     ╚═╝     ╚═╝╚═════╝ ╚═════╝╚═╝  ╚═══╝      ╚═══╝ ╚══════╝

                                {Fore.RESET}{Fore.LIGHTBLACK_EX}            user | {__usuario__}
                                            ═══════════════════════════════════════════════════════
                                            creators | {__criadores__}
                                            ═══════════════════════════════════════════════════════
                                            version  | {__versao__}
                                            ═══════════════════════════════════════════════════════
                                            Executed | {dt_format} 
                                {Fore.RESET}       
""")

os.system(command="pause")



#comandos
lista = [
    'kall',
    'kick',
    'ball',
    'ban',
    'nuke',
    'emoji',
    'server',
    'div_dm',
    'rename',
    'roles',
]



@client.command()
async def kick(member: discord.Member):
   await member.kick(reason="fuck u")
    
@client.command()
async def ban(member: discord.Member):
   await member.ban(reason="fuck u")
    
@client.event
async def on_channel_create(ctx):
    while True:
        await ctx.send(random.choices(msgs))
@client.command()
async def nuke(ctx):
    guild = ctx.message.guild
     




client.run(f"{token}",bot={q_self])