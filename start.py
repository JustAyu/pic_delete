import asyncio
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from pyrogram.types import Message

API_ID = 
ALI_HASH = ""
app = Client("babe",api_id=API_ID,api_hash=API_HASH)

ASKING = int(input("How many dps you wanna delete?\n"))


async def sux():
  try:
    photos = [p async for p in app.get_chat_photos("me")]
    print("Deleting All Photos...")
    await app.delete_profile_photos([p.file_id for p in photos[1:ASKING]])
    print("Deleted All Photos!")
  except:
    print("Something Is Wrong\nERROR!")


app.run(sux())
