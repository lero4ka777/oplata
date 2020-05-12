import telebot
bot = telebot.TeleBot('1140907948:AAHv4G8wJFV7jJBf0lPsiHx7w_xFnOdDjVw');
import random
from telebot import types
 
 
@bot.message_handler(commands=['start'])
def welcome(message):
    print("Добрый день!");
    

 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("👑Что такое VIP доступ?👑")
    item2 = types.KeyboardButton("💰Оплата через QIWI💰")
    item3 = types.KeyboardButton("💰Купить VIP лично у Админа💰")
    
 
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    
 
    bot.send_message(message.chat.id, "Эй покажи прибыль, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы забрать твою прибыль.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '👑Что такое VIP доступ?👑':
           bot.send_message(message.chat.id, 'Смотри, Vip доступ имеет такие возможности как. \n\nМожно делат все что угодно. \nЕсть 20 фото 10 видео') 
        
    if message.chat.type == 'private':
        if message.text == '💰Оплата через QIWI💰':
           bot.send_message(message.chat.id, 'Оплатить можно так. \nВот счет для оплаты. Marina_bot')
           
    if message.chat.type == 'private':
        if message.text == '💰Купить VIP лично у Админа💰':
           bot.send_message(message.chat.id, 'Оплатить можно так. \nВот <b>пидор</b> <b>{1.first_name}</b>  на админа @probiz777'.format(message.from_user, bot.get_me()),
               parse_mode='html')

        
 
    
 
# RUN
bot.polling(none_stop=True)
