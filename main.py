from calendar import weekday
from sqlite3 import Date
import telebot
import requests
import json
import datetime
from googletrans import Translator
import count_week
from saturday_handler import saturday_week_day


#   TOKENS
# region
ANTONIO_TOKEN = "5733089302:AAH9YPC_Ts6czskJa6pHHc-ukbtd2CBAC6s"
TEST_BOT_TOKEN = "5769706294:AAHMx-hYxE2tv5A8UbuwnkeOePUva2dE5mE"
# endregion


bot = telebot.TeleBot(TEST_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, "Вас вітає бот Дениса @denblackson", parse_mode='html')


@bot.message_handler(commands=['help'])
def get_help(message):
    help_menu = """
    /tomorrow    - щоб отримати розклад на завтра(суботи включно)\n\n/codes    - щоб отримати коди класів\n\n/week    - щоб отримати номер навчального тижня
    \n\n/time  - щоб отримати розклад дзвінків\n\n/marks -  шкала оцінювання\n\n/today - розклад на сьогодні(суботи включно)
    
    \n\nвідправ <u><b>будь-яке</b></u> число, щоб отримати цікавий факт
    """
    bot.send_message(message.chat.id,
                     help_menu,
                     parse_mode='html')  # -    , parse_mode='html'


@bot.message_handler(commands=['week'])
def week(message):
    bot.send_message(message.chat.id, f'Зараз тиждень номер <b>{count_week.get_num_of_week()}</b>', parse_mode='html')


def sent_photo(message, date : datetime.date):
    today_date = date.date()
    tomorrow_date = today_date + datetime.timedelta(days=1)
    today_date_of_week = today_date.strftime('%A')
    tomorrow_date_of_week = tomorrow_date.strftime('%A')
    photo = None

    if tomorrow_date_of_week == "Saturday":
        week_day = saturday_week_day(tomorrow_date)
        photo = open(f"photos/Розклад/{week_day[0]} тиждень/{week_day[1]}.jpg", 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        try:
            photo = open(f"photos/Розклад/{count_week.get_num_of_week()} тиждень/{tomorrow_date_of_week}.jpg", 'rb')
            # print(f"photos/Розклад/{num_of_week} тиждень/П'ятниця.jpg")
            bot.send_photo(message.chat.id, photo)
        except:
            bot.send_message(message.chat.id, "Вольою даною мені звергу, знизу, і побокам, завтра ми будем спати")
            
            bot.send_message(message.chat.id, "Сьогодні йдем на шашлики")
            video = open(f"photos/Sunday.mp4", 'rb')
            bot.send_video(message.chat.id, video)

@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
    today_date = datetime.datetime.today().date()
    tomorrow_date = today_date + datetime.timedelta(days=1)
    sent_photo(message, tomorrow_date)

@bot.message_handler(commands=['today'])
def today(message):
    today_date = datetime.datetime.today().date()
    sent_photo(message, today_date)

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
    codes = """
    Програмне забезпечення інформаційних систем - <b>gb4uzvv</b>
    Основи бізнес-аналізу в програмній інженерії - <b>lo5sife</b>, <b>o7xapzp</b>
    Основи штучного інтелекту - <b>jfcwnob</b>
    Аналіз вимог до програмного забезпечення - <b>qcupmfk</b>
    """                                          

    bot.send_message(message.chat.id, codes, parse_mode='html')
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
