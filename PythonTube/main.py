#pip install -U aiogram
#pip install pytube
from aiogram import *
import os
from pytube import YouTube


bot = Bot("5746153528:AAEe7LThBESKsgCqJlkBY0SrLMakLlZVrsY")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
	chat_id = message.chat.id
	await bot.send_message(chat_id, "Привет, я могу скачать видео\n отправь мне ссылку")
	
@dp.message_handler()
async def text_message(message:types.Message):
	chat_id = message.chat.id
	url = message.text
	yt = YouTube(url)
	if message.text.startswith == 'https://youtu.be/' or 'https://youtube.com/':
		await bot.send_message(chat_id,f"*Начинаю загрузку видео* : *{yt.title}*\n *C канала *:[{yt.author}]({yt.channel_url})", parse_mode="Markdown")
		await download_youtube_video(url,message,bot)

async def download_youtube_video(url,message,bot):
	yt = YouTube(url)
	s = yt.title
	s = s.replace('|',' ')
	s = s.replace('/',' ')
	s = s.replace('?',' ')
	s = s.replace(':',' ')
	stream = yt.streams.filter(progressive=True, file_extension="mp4")
	stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{s}.mp4')
	file_stats = os.stat(f'{message.chat.id}/{message.chat.id}_{s}.mp4')
	if file_stats.st_size<50000000:
		with open(f"{message.chat.id}/{message.chat.id}_{s}.mp4", 'rb') as video:
			await bot.send_video(message.chat.id, video, caption ="*Вот ваше видео*", parse_mode="Markdown")
			#os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")
	else:
		await bot.send_message(message.chat.id,f"Размер : {file_stats.st_size} не могу отправить")



#--------------------------------------------
if __name__=='__main__':
	print("VIDEO")
	executor.start_polling(dp)