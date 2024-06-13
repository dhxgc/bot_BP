import telebot
from telebot import types

bot = telebot.TeleBot("7230309509:AAE1ZBCOxy7MxoSP6nMWah4VG7oE6D1F9_c")

# ID администратора, которому будут отправляться жалобы/предложения
ADMIN_CHAT_ID = '-1002236974516'

# Счетчик заявок
ticket_counter = 0

# Словарь для хранения активных заявок
active_tickets = {}

# Главное меню
def send_main_menu(message):
    main_menu_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = types.KeyboardButton('Отправить жалобу/предложение')
    main_menu_markup.add(item)
    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=main_menu_markup)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    send_main_menu(message)

# Обработчик нажатия кнопки "Отправить жалобу/предложение"
@bot.message_handler(func=lambda message: message.text == 'Отправить жалобу/предложение')
def handle_complaint(message):
    msg = bot.send_message(message.chat.id, "Пожалуйста, напишите вашу жалобу или предложение.")
    bot.register_next_step_handler(msg, receive_complaint)

# Обработчик получения жалобы/предложения
def receive_complaint(message):
    global ticket_counter
    ticket_counter += 1
    ticket_id = ticket_counter
    complaint_text = message.text
    user_id = message.from_user.id
    active_tickets[ticket_id] = user_id
    # Отправка подтверждения пользователю
    bot.send_message(message.chat.id, f"Ваша заявка №{ticket_id} принята.")
    # Отправка жалобы администратору
    bot.send_message(ADMIN_CHAT_ID, f"Новая заявка №{ticket_id} от пользователя {message.from_user.username} (ID: {user_id}):\n{complaint_text}")

# Обработчик ответа от администратора
@bot.message_handler(func=lambda message: message.reply_to_message and message.chat.id == int(ADMIN_CHAT_ID))
def handle_admin_response(message):
    try:
        original_message = message.reply_to_message.text
        ticket_id = int(original_message.split('№')[1].split(' ')[0])  # Извлечение номера заявки
        response_text = message.text
        user_id = active_tickets.pop(ticket_id)
        # Отправка ответа пользователю
        bot.send_message(user_id, f"Ответ на вашу заявку №{ticket_id}:\n{response_text}")
    except Exception as e:
        bot.send_message(ADMIN_CHAT_ID, f"Произошла ошибка при обработке ответа: {str(e)}")


bot.polling()