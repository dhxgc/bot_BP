

from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *
import telebot

bot = token


@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Начать заниматься']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Наша группа спорта']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['О нас']])
    bot.send_message(m.chat.id, 'Выберите действие', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'Начать заниматься':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Зал']])
        keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Улица']])
        bot.send_message(message.chat.id, 'Выберите кнопку')
    elif message.text == 'Наша группа спорта':
        bot.send_message(message.chat.id, 'Сслыка на группу')
    elif message.text == 'О нас':
        bot.send_message(message.chat.id, 'FQ')

bot.polling()