# -*- coding: utf-8 -*-
# https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter10.html
import config
import telebot
import sqlite3
from datetime import datetime, date, time
import time
from telebot import types

bot = telebot.TeleBot(config.token)
#GROUP_ID = -273237249  # Ваш ID группы
GROUP_ID = -1001117386138

conn = sqlite3.connect('Bot_messages.sqlite', check_same_thread=False)
conn1 = sqlite3.connect('comm.sqlite', check_same_thread=False)
#cursor = conn.cursor()
# Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
#cursor.execute("create table mess (id integer not null primary key AUTOINCREMENT, uid text, mess text, dop text,ts DATETIME DEFAULT CURRENT_TIMESTAMP);")

# Получаем результат сделанного запроса
#results = cursor.fetchall()
#results2 =  cursor.fetchall()

#print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
#print(results2)  # []

abuse={}
nabuse=0


def save_abuse():
	global abuse
	global nabuse
	abfile = open("abuse.txt", "w")
	for n in abuse.values():
		abfile.write(n.encode('cp1251').upper()+'\n')
	abfile.close()
	
def load_abuse():
	global abuse
	global nabuse
	abfile = open("abuse.txt", "r")
	for line in abfile:
		abuse[nabuse]=line.replace('\n','').decode('cp1251').upper()
		print abuse[nabuse]
		nabuse+=1		
	abfile.close()
	nabuse-=1
	
def add_abuse(sa):
	global abuse
	global nabuse
	nabuse+=1
	abuse[nabuse]=sa[2:].upper()
	print abuse[nabuse]
	save_abuse()

def del_abuse(sa):
	global abuse
	global nabuse
	c=0
	for w in abuse.values():
		if w==sa[2:].upper():
			n=c
		c+=1		
	x=abuse.pop(n)
	print abuse
	save_abuse()	
	

def check_abuse(st):
		global abuse
		global nabuse
		res=0
		ts=st.upper()
		for w in abuse.values():
			if ts.find(w)!=-1:
				res+=1
			#print w.decode('cp1251'),' ', ts		
		return res
		
def bot_answer(st):
		
		return 0
		
load_abuse()
	
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID)
def all_messages(message):
	#cursor.execute("insert into mess (id, uid, mess, dop) values (Null,'111', '222', '333');")
	#print(message) is not None
	'''if message.from_user.username is not None:
		s=message.from_user.username+": "+message.text+"\n"
	elif message.from_user.first_name is not None:
		s=message.from_user.first_name+": "+message.text+"\n"
	elif message.from_user.last_name is not None:
		s=message.from_user.last_name+": "+message.text+"\n"		
	'''
	global abuse
	global nabuse
	global conn1
	global OperationalError
	#global time
	#su=s#message.from_user.username+": "+message.text
	#cursor = conn.cursor()
	try:
		conn.execute("insert into mess (id, uid, mess, dop) values (Null,'"+str(message.from_user.id)+"', '"+message.text+"', ' ');")
		conn.commit()
	except OperationalError:
		print "Inserted"
	sd=message.date;
	ss=message.text
	print sd
	print(time.ctime(sd)) 
	print(time.ctime(sd+300))
	if (check_abuse(ss)>0)&(ss[0]!='.'): 
		bot.delete_message(message.chat.id, message.message_id)
		bot.send_message(chat_id=message.chat.id,text= u"Пользователь"+u" ругается матом!!! -> "+ss)
		#bot.kick_chat_member(chat_id=message.chat.id, user_id=message.from_user.id, until_date=None)
		bot.restrict_chat_member(config.token, user_id=message.from_user.id,
			until_date=sd+60, can_send_messages=True,
            can_send_media_messages=False, can_send_other_messages=True)
			
	if ss[0]=='.' :
		bot.delete_message(message.chat.id, message.message_id)
		# это лично боту
		if ss[1]=='+':
			add_abuse(ss)
		elif ss[1]=='-':
			del_abuse(ss)
		elif ss[1]=='!':
			cur = conn1.cursor()
			cur.execute("select ans from mess order by id desc limit 20")
			results = cur.fetchall()
			rs=str("")
			#j=0
			for se in results:
				rs=rs+se[0]+'\n'
				#j+=1
				#print (se)
			cur.close()
			print(rs)
			bot.send_message(chat_id=message.chat.id,text=rs)
		for n in abuse.values():
				print n
'''
@bot.message_handler(func=lambda message: True)
def any_message(message):
    bot.reply_to(message, "Сам {!s}".format(message.text))

@bot.edited_message_handler(func=lambda message: True)
def edit_message(message):
    bot.edit_message_text(chat_id=message.chat.id,
                          text= "Сам {!s}".format(message.text),
                          message_id=message.message_id + 1)
						  
@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if entity.type in ["url", "text_link"]: 
            # Мы можем не проверять chat.id, он проверяется ещё в хэндлере 
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return						  
'''						  
if __name__ == '__main__':
     bot.polling(none_stop=True)
	 
conn.close()	 
'''
d:\PY\bot1>lbot.py
{'forward_from_chat': None, 
'migrate_to_chat_id': None, 
'invoice': None, 
'text': u'222', 
'sticker': None, 

'from_user': 
	{'username': u'Lz42Stas', 
	'first_name': u'Stanislau', 
	'last_name': u'Frantishek', 
	'id': 357390016, 
	'language_code': u'ru-RU'}, 

'pinned_message': None, 
'delete_chat_photo': None, 
'migrate_from_chat_id': None, 
'new_chat_members': None, 
'video': None, 
'left_chat_member': None, 

'chat': 
	{'username': None, 
	'first_name': None, 
	'last_name': None, 
	'description': None,
	'title': u'\u041b\u0438\u0446\u0435\u0439 5 \u0411\u044b\u0445\u043e\u0432', 
	'photo': None, 
	'all_members_are_administrators': False, 
	'invite_link': None, 
	'type': u'group', 
	'id': -273237249}, 

'group_chat_created': None, 
'new_chat_photo': None, 
'forward_date': None, 
'entities': None, 
'supergroup_chat_created': None, 
'photo': None, 
'document': None, 
'forward_from': None, 
'location': None, 
'edit_date': None, 
'content_type': 'text', 
'successful_payment': None, 
'date': 1507203001, 
'new_chat_member': None, 
'voice': None, 
'reply_to_message': None, 
'venue': None, 
'message_id': 182, 
'caption': None, 
'contact': None, 
'channel_chat_created': None, 
'video_note': None,
'audio': None, 
'new_chat_title': None}

'''