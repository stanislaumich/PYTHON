#pip install -U aiogram
#pip install pytube
from aiogram import *
import os
from pytube import YouTube


bot = Bot("5706031236:AAGoV6JWqK3jwNsE0EsS8keHXqCREpIYtAk")
dp = Dispatcher(bot)

def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'')
    return value;

@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
	chat_id = message.chat.id
	await bot.send_message(chat_id, "Привет, я могу скачать звук из видео\n отправь мне ссылку на YouTube")
	
@dp.message_handler()
async def text_message(message:types.Message):
	chat_id = message.chat.id
	url = message.text
	yt = YouTube(url)
	if message.text.startswith == 'https://youtu.be/' or 'https://youtube.com/':
		await bot.send_message(chat_id,f"*Начинаю загрузку видео* : *{yt.title}*\n *C канала *:[{yt.author}]({yt.channel_url})", parse_mode="Markdown")
		await download_youtube_video(url,message,bot)

async def download_youtube_video(url,message,bot):
	print("Загружаю ")
	yt = YouTube(url)
	s = yt.title
	#s = s.replace('|',' ')
	s = remove(s, '\/:*?"<>|')
	print(f"{s}")
	#print(yt.streams)
	#stream = yt.streams.filter(progressive=True, file_extension="mp4")
	stream = yt.streams.filter(only_audio=True)
	stream.first().download(f'{message.chat.id}', f'{s}.mp3')#get_highest_resolution
	file_stats = os.stat(f'{message.chat.id}/{s}.mp3')
	if file_stats.st_size<50000000:
		with open(f"{message.chat.id}/{s}.mp3", 'rb') as video:
			#await bot.send_video(message.chat.id, video, caption ="*Вот ваша панама*", parse_mode="Markdown")
			await bot.send_audio(message.chat.id, video, caption ="*Скачано ботом с Ютуба*", parse_mode="Markdown")
			#os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")
			print("Готово")
	else:
		await bot.send_message(message.chat.id,f"Размер : {file_stats.st_size} не могу отправить")
		print("Большой файл")


#--------------------------------------------
if __name__=='__main__':
	print("SOUND")
	executor.start_polling(dp)