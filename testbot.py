import telebot
import requests
import schedule
import time

token = '5033176182:AAGwMqqVH5-yM-1QZoWPR_ULk-YautkwnGY'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Отчет', 'Привет', 'Пока')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
    bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text.lower() == 'отчет':
        if message.chat.id == 181020945:
            bot.send_message(message.chat.id, 'Вам запрещен доступ к данному отчету')
        if message.chat.id != 181020945:
            doc = open('123456.docx', 'rb')
            #bot.send.message(message.chat.id, 'Отчет')
            bot.send_document(message.chat.id, doc)
    else:
        bot.send_message(message.chat.id, 'Я не знаю что Вам ответить!')

print('Идет тест')

bot.polling()
