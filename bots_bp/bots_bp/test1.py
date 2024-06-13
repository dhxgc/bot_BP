#from functions import *
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
from config import *

API_TOKEN = token
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):

    #Возвращение в главное меню
    if message.text == '/start':
        send_hello_message(message)
        send_main_menu(message)

    
    elif message.text == 'Назад':
        send_main_menu(message)

    #Вывод первого меню "Контакты"
    elif message.text == 'Контакты':
        send_submenu1_contacts(message)
    elif message.text == 'Группа Вконтакте':
        bot.reply_to(message, "vk.com/vdvt_ru")
    elif message.text == 'Канал в Telegram':
        bot.reply_to(message, "t.me/vdoh_vdoh/")
    elif message.text == 'Сайт Вдохновителей':
        bot.reply_to(message, "вдохновители.рф")


    #Вывод второго меню "О нас"
    elif message.text == 'О нас':
        send_info_about(message)

    #Вывод третьего меню "Мероприятия"
    elif message.text == 'Мероприятия':
        send_info_about_event(message)
    
    elif message.text == 'Часто задаваемые вопросы':
        send_info_about_question(message)

    #Если пользователь вводит какое-то говно
    else:
        bot.send_message(message.chat.id, "Я не знаю такой команды!")


def send_chat_id(message):
    __chat_id = message.chat.id
    bot.send_message(message.chat.id, __chat_id)

def send_hello_message (message):
    bot.send_message(message.chat.id, "👋Привет!\n\n🤖Я - бот-помощник команды Вдохновителей.\n\nЯ могу:\n - предоставить информацию о ближайших мероприятиях\n - предоставить ссылки на наши группы\n - связать тебя c представителями, куда ты сможешь задать интересующий тебя вопрос.")
    send_audio_hello_message(message)
    send_chat_id(message)

def send_audio_hello_message(message):
    voice_message_file = open('test1.ogg', 'rb')
    bot.send_voice(message.chat.id, voice_message_file)
    voice_message_file.close()

#Главное меню при старте
def send_main_menu(message):
    #bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    #bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    main_menu_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item1 = types.KeyboardButton('Контакты')
    item2 = types.KeyboardButton('О нас')
    item3 = types.KeyboardButton('Мероприятия')
    item4 = types.KeyboardButton('Часто задаваемые вопросы')
    item5 = types.KeyboardButton('Стать участником')

    main_menu_markup.row(item1, item2)
    main_menu_markup.row(item5)
    main_menu_markup.row(item4, item3)

    bot.send_message(message.chat.id, "Выберите то, что вас интересует", reply_markup=main_menu_markup)  

def send_submenu1_contacts(message):
    submenu_markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    subitem1 = types.KeyboardButton('Группа Вконтакте')
    subitem2 = types.KeyboardButton('Канал в Telegram')
    subitem3 = types.KeyboardButton('Сайт Вдохновителей')
    back_item = types.KeyboardButton('Назад')
    submenu_markup.row(subitem1, subitem2)
    submenu_markup.row(subitem3, back_item)
    bot.send_message(message.chat.id, "Выберите то, что вас интересует", reply_markup=submenu_markup)

def send_info_about(message):
    bot.send_message(message.chat.id, '«Вдохновители» - Всероссийское движение и Лаборатория Смысловых решений.\n\nВ движении состоят более 180 Вдохновителей - это эксперты, предприниматели, учёные и лидеры различных направлений, которые передают свой опыт в наших флагманских проектах:\n\n🧬«Маршрут Вдохновения»;\n🧬«Очаг Вдохновения»;\n🧬«Смена Вдохновения» и другие.\n\nДвижение организовано при поддержке Министерства просвещения Российской Федерации и Народного Фронта.\n\n💥Давайте вдохновлять вместе!')


def send_info_about_event(message):
    # Создаем inline клавиатуру с тремя кнопками для сайтов
    markup_kbrd = types.InlineKeyboardMarkup()
    btn_site1 = types.InlineKeyboardButton(text='Всероссийский форум\nмолодых предпринимателей «Амур»', url='https://vk.com/vdvt_ru?w=wall-204603458_4384')
    btn_site2 = types.InlineKeyboardButton(text='«Наши Люди»:\nцикл лекций о великих Созидателях', url='https://vk.com/vdvt_ru?w=wall-204603458_4381')
    btn_site3 = types.InlineKeyboardButton(text='', url='https://www.example3.com') ############################
    markup_kbrd.row(btn_site1)
    markup_kbrd.row(btn_site2)
    markup_kbrd.row(btn_site3)
    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, '"Вдохновители" проводят разнообразные мероприятия, направленные на вдохновение, обучение и развитие участников. В рамках этих мероприятий участники имеют возможность общаться с лидерами различных областей, участвовать в познавательных мастер-классах, обмениваться опытом и расширять круг общения.\
\n\nОсновные виды мероприятий, которые могут проводиться "Вдохновителями", включают:\n\
🧬Лекции и семинары: Проведение мотивационных лекций, образовательных семинаров, где спикеры делятся своим опытом и знаниями с участниками.\n\
🧬Мастер-классы: Организация практических занятий и мастер-классов по различным тематикам для развития навыков и умений.\n\
🧬Конференции: Проведение конференций, где собираются профессионалы из разных областей для обмена опытом и обсуждения актуальных вопросов.\n\
🧬Тренинги и интенсивы: Организация обучающих тренингов и интенсивных программ для глубокого погружения в определенную тематику.\n\
🧬Круглые столы и дискуссии: Проведение круглых столов, дискуссий и панельных обсуждений по различным актуальным темам.\n\
🧬Спортивные и тимбилдинг мероприятия: Организация спортивных мероприятий, тимбилдингов и корпоративных мероприятий для укрепления командного духа.\n\
\nЭти мероприятия помогают участникам расширить кругозор, обогатиться новыми знаниями, найти вдохновение, найти мотивацию для достижения своих целей и укрепить контакты в профессиональном сообществе.', reply_markup=markup_kbrd)

def send_info_about_question(message):
    bot.send_message(message.chat.id, "⁉️ Для чего ты нужен?\n\n✅ Я предоставляю базовую информацию о движении Вдохновители, могу связать вас с администратором бота, или проинформировать о предстоящих событиях.")
    bot.send_message(message.chat.id, "⁉️ Чем ты отличаешься от других ботов?\n\n✅ Помимо кнопок, меню и обычного текста я умею распозновать то, что вы скажете в голосовом сообщении! Правда, нужно говорить именно то, что описано в правилах использования голосового ввода.... Но я скоро научусь понимать любые ваши фразы!")
    markup_kbrd = types.InlineKeyboardMarkup()
    btn_site1 = types.InlineKeyboardButton(text='Статья для новый Вдохновителей', url='')
    markup_kbrd.row(btn_site1)

bot.polling(none_stop=True)