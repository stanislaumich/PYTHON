import telebot
from telebot import types

TOKEN = '461381865:AAE_JFutn1dFHOg6Rl7qdTgkXqzTjjHJpuo'
bot = telebot.TeleBot(TOKEN)

with open('./SH.txt', 'r') as file:
    BOOK = file.read() 

def pages_keyboard(start, stop):

    keyboard = types.InlineKeyboardMarkup()
    btns = []
    if start > 0: btns.append(types.InlineKeyboardButton(
        text='<-', callback_data='to_{}'.format(start - 700)))
    if stop < len(BOOK): btns.append(types.InlineKeyboardButton(
        text='->', callback_data='to_{}'.format(stop)))
    keyboard.add(*btns)
    return keyboard 

@bot.message_handler(commands=['start'])
def start(m):

    bot.send_message(m.chat.id, BOOK[:700], parse_mode='Markdown',
        reply_markup=pages_keyboard(0, 700))

@bot.callback_query_handler(func=lambda c: c.data)
def pages(c):

    bot.edit_message_text(
        chat_id=c.message.chat.id,
        message_id=c.message.message_id,
        text=BOOK[int(c.data[3:]):int(c.data[3:]) + 700],
        parse_mode='Markdown',
        reply_markup=pages_keyboard(int(c.data[3:]), 
            int(c.data[3:]) + 700))

bot.polling()