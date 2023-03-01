from pyrogram import Client, filters
from pyrogram.types import *
from pytube import YouTube
import os

#api_id = 11855414
#api_hash = "71449899c824b5bc9a91d8a52b20c5f3"

app = Client(
"Downloader",
api_id = 11855414,
api_hash = "71449899c824b5bc9a91d8a52b20c5f3",
bot_token ="5769907387:AAEJSjo2cu7dsw5h1xbyPi568TijI4rp4-Q"
)

@app.on_message()
async def down(client, message):
	await message.reply("Wait...")
	yt = YouTube(message.text)
	video = yt.streams.filter(res="720p", progressive = False, file_extension="mp4").first()
	file = await app.download_media(video)
	with open(file, "rb") as vid:
		print(vid)
		await app.send_video(message.chat.id, vid)
  
print("Successful") 
app.run()
