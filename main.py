import telebot
import requests
import json
import datetime
from googletrans import Translator

#   TOKENS
# region
ANTONIO_TOKEN = "5733089302:AAH9YPC_Ts6czskJa6pHHc-ukbtd2CBAC6s"
TEST_BOT_TOKEN = "5769706294:AAHMx-hYxE2tv5A8UbuwnkeOePUva2dE5mE"
# endregion


bot = telebot.TeleBot(ANTONIO_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.send_message(message.chat.id, "Вас вітає бот Дениса @denblackson", parse_mode='html')


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id,
                     '/tomorrow    - щоб отримати розклад на завтра\n\n/codes    - щоб отримати коди класів\n\n/week    - щоб отримати номер навчального тижня'
                     '\n\n/time  - щоб отримати розклад дзвінків\n\n/marks -  шкала оцінювання\n\n/today - розклад на сьогодні'
                     ''
                     '\n\nвідправ <u><b>будь-яке</b></u> число, щоб отримати цікавий факт',
                     parse_mode='html')  # -    , parse_mode='html'


# region
# bot.send_message(message.chat.id, '/codes    - щоб отримати коди класів')
# bot.send_message(message.chat.id, '/week    - щоб отримати номер навчального тижня')
# bot.send_message(message.chat.id, "відправ <u><b>будь-яке</b></u> число, щоб отримати цікавий факт",parse_mode='html')
# endregion


@bot.message_handler(commands=['week'])
def week(message):
    datetime_now = datetime.datetime.now()
    datetime_september = datetime.datetime(year=2022, month=9, day=1)
    result = datetime_now - datetime_september
    count_number_of_week = (result.days / 7) % 2
    num_of_week = None
    if count_number_of_week == 0:
        num_of_week = 1
    else:
        num_of_week = 2
    bot.send_message(message.chat.id, f'Зараз тиждень номер <b>{num_of_week}</b>', parse_mode='html')


@bot.message_handler(commands=['tomorrow'])
def tomorrow(message):
    datetime_now = datetime.datetime.now()
    datetime_september = datetime.datetime(year=2022, month=9, day=1)
    result = datetime_now - datetime_september
    count_number_of_week = (result.days / 7) % 2
    num_of_week = None
    if count_number_of_week == 0:
        num_of_week = 1
    else:
        num_of_week = 2
    today_date = datetime.datetime.today()
    tomorrow_date = today_date + datetime.timedelta(days=1)
    photo = open(f"photos/Розклад/{num_of_week} тиждень/{tomorrow_date.strftime('%A')}.jpg", 'rb')
    # print(f"photos/Розклад/{num_of_week} тиждень/П'ятниця.jpg")
    bot.send_photo(message.chat.id, photo)


@bot.message_handler(commands=['today'])
def tomorrow(message):
    datetime_now = datetime.datetime.now()
    datetime_september = datetime.datetime(year=2022, month=9, day=1)
    result = datetime_now - datetime_september
    count_number_of_week = (result.days / 7) % 2
    num_of_week = None
    if count_number_of_week == 0:
        num_of_week = 1
    else:
        num_of_week = 2
    today_date = datetime.datetime.today()

    photo = open(f"photos/Розклад/{num_of_week} тиждень/{today_date.strftime('%A')}.jpg", 'rb')
    #               photos/Розклад/2 тиждень/Mondey.jpg
    bot.send_photo(message.chat.id, photo)


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

    # bot.send_message(message.chat.id, "Основи бізнес-аналізу в програмній інженерії")
    # bot.send_message(message.chat.id, "<b>lo5sife</b>", parse_mode='html')


# <a>agb4uzvv</a>
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
