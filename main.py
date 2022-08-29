import telebot
import requests
import json
import datetime
from googletrans import Translator
import CONSTS
import count_week
import saturday

bot = telebot.TeleBot(CONSTS.ANTONIO_TOKEN)
print("bot is launched")


@bot.message_handler(commands=['start'])
def start(message):
    start_message = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nВас вітає бот Дениса @denblackson'


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, CONSTS.help_menu, parse_mode='html')


@bot.message_handler(commands=['week'])
def week(message):
    bot.send_message(message.chat.id, f'Зараз тиждень номер <b>{count_week.get_num_of_week()}</b>', parse_mode='html')


@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
    today_date = datetime.datetime.today().date()
    tomorrow_date = today_date + datetime.timedelta(days=1)
    today_date_of_week = today_date.strftime('%A')
    tomorrow_date_of_week = tomorrow_date.strftime('%A')
    photo = None

    if tomorrow_date_of_week == "Saturday":
        bot.send_photo(message.chat.id, saturday.if_tomorrow_is_saturday())
    else:
        try:
            photo = open(f"photos/Розклад/{count_week.get_num_of_week()} тиждень/{tomorrow_date_of_week}.jpg", 'rb')
            bot.send_photo(message.chat.id, photo)
        except:
            bot.send_message(message.chat.id, "Вольою даною мені звергу, знизу, і побокам, завтра ми будем спати")


@bot.message_handler(commands=['today'])
def today(message):
    today_date = datetime.datetime.today().date()
    today_date_of_week = today_date.strftime('%A')
    photo = None

    if today_date_of_week == "Saturday":
        bot.send_photo(message.chat.id, saturday.if_today_is_saturday())
    else:
        try:
            photo = open(f"photos/Розклад/{count_week.get_num_of_week()} тиждень/{today_date_of_week}.jpg", 'rb')
            bot.send_photo(message.chat.id, photo)
        except:
            bot.send_message(message.chat.id, "Сьогодні йдем на шашлики")
            video = open(f"photos/Sunday.mp4", 'rb')
            bot.send_video(message.chat.id, video)


@bot.message_handler(commands=['time'])
def time(message):
    photo = open('photos/time.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['marks'])
def marks(message):
    photo = open('photos/шкала оцінок.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['codes'])
def tomorrow(message):
    bot.send_message(message.chat.id, "Програмне забезпечення інформаційних систем")
    bot.send_message(message.chat.id, "<b>gb4uzvv</b>", parse_mode='html')

    bot.send_message(message.chat.id, "Основи бізнес-аналізу в програмній інженерії")
    bot.send_message(message.chat.id, "<b>lo5sife</b>", parse_mode='html')
    bot.send_message(message.chat.id, "<b>o7xapzp</b>", parse_mode='html')

    bot.send_message(message.chat.id, "Основи штучного інтелекту")
    bot.send_message(message.chat.id, "<b>jfcwnob</b>", parse_mode='html')

    bot.send_message(message.chat.id, "Аналіз вимог до програмного забезпечення")
    bot.send_message(message.chat.id, "<b>qcupmfk</b>", parse_mode='html')

    # bot.send_message(message.chat.id, "Основи бізнес-аналізу в програмній інженерії")
    # bot.send_message(message.chat.id, "<b>lo5sife</b>", parse_mode='html')


@bot.message_handler(regexp='[0-9+]')
def get_number_for_fact(message):
    try:
        answer = requests.get(f'http://numbersapi.com/{message.text}?json')
        eng_text = json.loads(answer.text)['text']
        print(eng_text)

        translator = Translator()
        ukr_trans = translator.translate(eng_text, dest='uk')
        print(ukr_trans.text)

        bot.send_message(message.chat.id, ukr_trans.text)
    except:
        pass


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "qq", parse_mode='html')


bot.infinity_polling()
