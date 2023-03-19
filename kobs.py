import os
import time
try:
    import discord
except:
    if os.name == "nt":
        os.system('pip install discord')
        import discord
    else:
        os.system('pip3 install discord')
        import discord
try:
    from colorama import Fore
except:
    if os.name == "nt":
        os.system('pip install colorama')
        from colorama import Fore
    else:
        os.system('pip3 install colorama')
        from colorama import Fore

from discord.ext import commands
from discord.ext.commands.errors import DisabledCommand

class data:
    admin_role = "784994511599829002" #admin role tag id
    Token = "OTQwNzQ5MzgyNjk1OTE1NTkw.GhXDV0.EK7tvoFdUGLBfFyGRUKDE6YE5tMzuSlcTt1lEU" #Bot token
    prefix = "!" #Bot prefix
    icon = "https://cdn.discordapp.com/avatars/784994511599829002/796670c38b30d02c29db237b5c621d11.png?size=1024" #Bot tumbnail icon
    colors = "#7F7F7F" # Bot tumbnail color

client = commands.Bot(command_prefix=data.prefix,intents=discord.Intents.all())  
client.remove_command("help")

@client.event
async def on_ready():
    print(f'{Fore.RED}[{Fore.RESET}Debug{Fore.RED}]{Fore.RESET} Bot Sucsses Fully Started')

@client.event
async def on_voice_state_update(member, before, after):
    if after.channel.id == 1044390624574574676: # channel id connecet to staff
        if member == client.user:
            return
        else:
            timenow = time.strftime("%H:%M")
            channel = client.get_channel(1044390733135757373) # channel id jaii k payam bede
            emb = discord.Embed(
                title = "**Quantum**",
                description = f"**New User in Connect To staff \n User : {member.mention} \n User ID : {member.id} \n User name : {member.name} \n Time : {timenow} **",
                color=discord.Color.blue()
            )
            member_emb = discord.Embed(
                title = "**Quantum**",
                description = f"{member.mention} \n **dadash Kheyli khosh omadi**",
                color=discord.Color.blue()
            )
          #  emb.set_thumbnail(url=member.author.avatar_url)
            member_emb.set_thumbnail(url=data.icon)
            member_emb.set_footer(text='Quantum',icon_url=data.icon)
            await member.send(embed=member_emb)
            await channel.send(f'|| <@&{data.admin_role}> ||')
            await channel.send(embed=emb)
            channel = client.get_channel(1044390624574574676)
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio("voice.mp3"), after=lambda e: print('done', e))
            await channel.disconnect()


def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

clear()
client.run(data.Token)