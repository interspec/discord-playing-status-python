import discord
from discord.ext import commands
from requests import get
from random import choice
import pystyle
from concurrent.futures import ThreadPoolExecutor







print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, """
██████╗ ██╗      █████╗ ██╗   ██╗██╗███╗   ██╗ ██████╗      ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██║████╗  ██║██╔════╝     ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ ██╔════╝██╔══██╗
██████╔╝██║     ███████║ ╚████╔╝ ██║██╔██╗ ██║██║  ███╗    ██║     ███████║███████║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝
██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██║██║╚██╗██║██║   ██║    ██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗
██║     ███████╗██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                                                                    
~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~  

                                         ~{ Discord "Playing" Changer  }~
                                  ~{ Made with <3 by interspec (improve#0001) }~

~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ ### ~~~ 

            
""", 2))





print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, """
Enter your token (remove the "")
""", 2))

settoken = input(' ~ ')


token = settoken

print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, """
What would you like to set your Playing status to?
""", 2))
bot = commands.Bot(command_prefix = "notneeded")




status = input(' ~ ')

@bot.event
async def on_connect():
    play = discord.Game(
        name = status,
        
    )


    print('Your status is now: Playing ' + status)
    await bot.change_presence(activity=play)

bot.run(token, bot=False)    
