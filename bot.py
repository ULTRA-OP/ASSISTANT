

from telethon import TelegramClient
import os
"""
owner = os.environ.get("OWNER_ID", None)
token = os.environ.get("TOKEN")
api_id = os.environ.get("API_ID", None)
api_hash = os.environ.get("API_HASH", None)
"""
api_id = "2654773"
api_hash = "d53a77f2db19fcdb81ff2b2170e93c96"
token = "1789892375:AAFEsATJh7EHwhFtsRNWJkjpPiyae4TW_cY"
bot = TelegramClient ("legendx", api_id, api_hash).start(bot_token=token)
devs = set(int(x) for x in os.environ.get("DEV_USERS", "1694874284", "1503668700").split())
# kanger aaya bhaago bc
photo = "https://telegra.ph/file/4678add619696c235a42a.jpg"
from telethon import events, Button, custom
import asyncio
import logging
import os
from datetime import datetime
try:
  import requests
except:
  os.system("pip install requests")
try:
  import LEGENDX
except:
  os.system("pip install LEGENDX")
from requests import exceptions, get, post
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
import re, sys, os

PERU = [[Button.url("Repo", "https://github.com/HACKERBOTTELEGRAM/HACKERBOTOP"), Button.url("Channel", "https://t.me/DARKLONXOP")]]
PERU += [[Button.url("Spam", "https://t.me/DARKLON_OT"), Button.url("Support", "https://t.me/DARKLON_USERBOT_SUPPORT")]]
PERU += [[custom.Button.inline("Rules", data="rules")]]

HMM= [[custom.Button.inline("Rules", data="rules")]]

hmm = [[custom.Button.inline("Back", data="back")]]

alain = [[Button.url("Support", "V"), Button.url("Chat", "https://t.me/DARKLON_USERBOT_SUPPORT")]]

import logging
import os
from datetime import datetime
from telethon import events
import requests
from requests import exceptions, get
from telethon.errors.rpcerrorlist import YouBlockedUserError

@bot.on(events.ChatAction)
async def handler(event):
  if event.user_joined:
    pro = await event.get_user()
    boy = pro.first_name
    if event.chat_id == -1001427249400:
      await bot.send_file(event.chat_id, photo, caption=f"**Hello {boy} welcome to UltraX Chat\nMake sure that you read the group rules...**", buttons=HMM)
    elif pro.id == 1082238780:
      await bot.send_message(event.chat.id, f"**Oh no!\nBe alert a shitty kanger {boy} has just joined chat.\nLet me inform @admins**")
    else:
      await bot.send_message(event.chat.id, f"**Hello mate\nI am UltraX Assistant, Sorry to say that i only work in UltraX network.**", buttons=alain)
      

@bot.on(events.NewMessage(pattern="/start|/START|DARKLON"))
async def assistant (event):
  if event.chat_id == -1001420616907:
    await bot.send_message(event.chat_id,"**Hello I am DARKLON assitant.\nA simple group manager bot to manage DARKLON network**", buttons=PERU)
  else:
    await bot.send_message(event.chat.id, f"**Hello mate\nI am DARKLON Assistant, Sorry to say that i only work in DARKLON network.**", buttons=alain)
    
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"help")))
async def help (event):
  await event.edit("Feature coming soon")
  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"rules")))
async def help (event):
  await event.edit(f"**Here are the rules for DARKLON USERBOT SUPPORT:**\n\n-`Don't use other userbots here.`\n-`Send the full logs if your bot crashes.`\n `No pm to devs, results in ban.`\n-`No phonographic content here.`\n-`Dont spam through bot commands.`", buttons=hmm)

  
@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back")))
async def back(event):
  global LEGEND

  await event.edit("**Hello I am UltraX assitant.\nA simple group manager bot to manage UltraX network**", buttons=PERU)
  
@bot.on(events.NewMessage(pattern="/rules|/RULES"))
async def assistant (event):
  if event.chat_id == -1001420616907:
     await bot.send_message(event.chat.id, "**Click below to check group rules**",buttons=hmm)
  else:
     await bot.send_message(event.chat.id, f"**Hello mate\nI am DARKLON Assistant, Sorry to say that i only work in DARKLON network.**", buttons=alain)


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

if __name__ ==  '__main__':
  bot.run_until_disconnected()
