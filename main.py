import discord
import asyncio
from pystyle import Colors, Colorate, Center
import requests
from discord import SyncWebhook
import os
import time

banner = """

                    _____   _______________________  _____________________ __
                    ___  | / /__  ____/_  __ \__  / / /_  __ \_  __ \__  //_/
                    __   |/ /__  __/  _  / / /_  /_/ /_  / / /  / / /_  ,<   
                    _  /|  / _  /___  / /_/ /_  __  / / /_/ // /_/ /_  /| |  
                    /_/ |_/  /_____/  \____/ /_/ /_/  \____/ \____/ /_/ |_|  
                                                         
                                                                                                  
                                [Tool Developed by Vains]
                          [! https://www.youtube.com/@Vainsx47 !] 
                                  < Control any webhook >  
        


"""

options = """
                \033[31m1 : \033[0m Send message                  \033[31m4 : \033[0m Spam message 
                \033[31m2 : \033[0m Delete webhook                \033[31m5 : \033[0m Discord 
                \033[31m3 : \033[0m Rename webhook                \033[31m6 : \033[0m Exit


"""



while True:
    logo = Center.XCenter(banner)

    def printbanner():
        print(Colorate.Horizontal(Colors.red_to_white, banner, 1))

    printbanner()
    print(options)

    chc = int(input("[\033[31m/\033[0m] Choice: "))
    if chc == 1:        
        webhook = input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@Webhook URL~$ "))
        msg = input(Colorate.Horizontal(Colors.red_to_white, "[/] Choice:~/@Webhook URL~/@Message: "))

        webhook = SyncWebhook.from_url(webhook)
        webhook.send(msg)
        print(Colorate.Horizontal(Colors.red_to_white, f"[VAINS] | [SUCESS] | [+] Message sent: {msg}", 1))

    elif chc == 2:

        webhook = input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@Webhook URL~$ "))
        response = requests.delete(webhook)

        print(Colorate.Horizontal(Colors.red_to_white, "[VAINS] | [+] Webhook sucessfuly deleted.", 1))

    elif chc == 3:
        webhook = input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@Webhook URL~$ "))
        NewName = input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@NewName~$ "))

        webhook = SyncWebhook.from_url(webhook)

        async def edit():
            webhook.edit(name=f"{NewName}")
        asyncio.run(edit())
        print(Colorate.Horizontal(Colors.red_to_white, f"[VAINS] | [SUCESS] | [+] Renamed webhook: {NewName}", 1))

    elif chc == 4:
        webhook = input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@Webhook URL~$ "))
        msg = input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@Webhook URL~/@Message~$ "))
        amount = int(input(Colorate.Horizontal(Colors.red_to_white,"[/] Choice:~/@Webhook URL~/@Amount~$ ")))

        msgt = {
            "content": f"{msg}"
        }

        for i in range(amount):
           async def send():
                res = requests.post(webhook, json=msgt)

                if res.status_code == 204:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[VAINS] | [SUCESS] | [+] Message sent: {msg}.", 1))
                else:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[VAINS] | [ERROR] | [-] Error while sending {msg} | Status code: {res.status_code}", 1))
           asyncio.run(send())

    elif chc == 5:
        print(Colorate.Horizontal(Colors.red_to_white, f"[VAINS] | [DISCORD SERVER] | > https://discord.gg/dUUBrkRX5Y", 1))
        os.system("PAUSE")

    elif chc == 6:
        exit()
    time.sleep(0.7)
    os.system('cls')








