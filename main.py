import telebot
# import requests
# import json
import datetime
# from googletrans import Translator
import CONSTS
import count_week
import saturday
import time
import del_mess

bot = telebot.TeleBot(CONSTS.ANTONIO_TOKEN)
print("bot is launched")

today_date = datetime.datetime.today().date()
tomorrow_date = today_date + datetime.timedelta(days=1)


@bot.message_handler(commands=['start'])
def start(message):
    start_message = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nВас вітає бот Дениса @denblackson'
    bot.send_message(message.chat.id, start_message, parse_mode='html')
    del_mess.thread_sleep(10)
    try:
        bot.delete_message(message.chat.id, int(message.message_id))
        bot.delete_message(message.chat.id, int(message.message_id) + 1)
    except:
        pass


@bot.message_handler(commands=['help'])
def get_help(message):
    bot.send_message(message.chat.id, CONSTS.help_menu, parse_mode='html')
    del_mess.thread_sleep(14)
    try:
        bot.delete_message(message.chat.id, int(message.message_id))
        bot.delete_message(message.chat.id, int(message.message_id) + 1)
    except:
        pass


@bot.message_handler(commands=['week'])
def get_week_num(message):
    bot.send_message(message.chat.id, f'Зараз тиждень номер <b>{count_week.get_num_of_week(today_date)}</b>',
                     parse_mode='html')
    del_mess.thread_sleep(5)
    try:
        bot.delete_message(message.chat.id, int(message.message_id))
        bot.delete_message(message.chat.id, int(message.message_id) + 1)
    except:
        pass


@bot.message_handler(commands=['tomorrow'])
def get_schedule_on_tomorrow(message):
    tomorrow_date_of_week = tomorrow_date.strftime('%A')
    photo = None
    if tomorrow_date_of_week == "Saturday":
        print(tomorrow_date_of_week)
        bot.send_photo(message.chat.id, saturday.if_tomorrow_is_saturday())
        del_mess.thread_sleep(30)
        try:
            bot.delete_message(message.chat.id, int(message.message_id))
            bot.delete_message(message.chat.id, int(message.message_id) + 1)
        except:
            pass

    else:
        try:
            photo = open(
                f"photos/Розклад/{count_week.get_num_of_week(tomorrow_date)} тиждень/{tomorrow_date_of_week}.jpg", 'rb')
            bot.send_photo(message.chat.id, photo)
            photo.close()
            del_mess.thread_sleep(30)
            try:
                bot.delete_message(message.chat.id, int(message.message_id))
                bot.delete_message(message.chat.id, int(message.message_id) + 1)
            except:
                pass

        except:
            bot.send_message(message.chat.id, "Вольою даною мені звергу, знизу, і побокам, завтра ми будем спати")
            del_mess.thread_sleep(10)
            try:
                bot.delete_message(message.chat.id, int(message.message_id))
                bot.delete_message(message.chat.id, int(message.message_id) + 1)
            except:
                pass


@bot.message_handler(commands=['today'])
def get_schedule_on_today(message):
    today_date_of_week = today_date.strftime('%A')
    if today_date_of_week == "Saturday":
        bot.send_photo(message.chat.id, saturday.if_today_is_saturday())
        del_mess.thread_sleep(30)
        try:
            bot.delete_message(message.chat.id, int(message.message_id))
            bot.delete_message(message.chat.id, int(message.message_id) + 1)
        except:
            pass
    else:
        try:
            photo = open(f"photos/Розклад/{count_week.get_num_of_week(today_date)} тиждень/{today_date_of_week}.jpg",
                         'rb')
            bot.send_photo(message.chat.id, photo)
            del_mess.thread_sleep(30)
            photo.close()
            try:
                bot.delete_message(message.chat.id, int(message.message_id))
                bot.delete_message(message.chat.id, int(message.message_id) + 1)
            except:
                pass
        except:
            bot.send_message(message.chat.id, "Сьогодні йдем на шашлики")
            video = open(f"photos/Sunday.mp4", 'rb')
            bot.send_video(message.chat.id, video)
            video.close()
            del_mess.thread_sleep(10)
            try:
                bot.delete_message(message.chat.id, int(message.message_id))
                bot.delete_message(message.chat.id, int(message.message_id) + 1)
                bot.delete_message(message.chat.id, int(message.message_id) + 2)
            except:
                pass


@bot.message_handler(commands=['time'])
def get_time_schedule(message):
    photo = open('photos/time.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    del_mess.thread_sleep(20)
    try:
        bot.delete_message(message.chat.id, int(message.message_id))
        bot.delete_message(message.chat.id, int(message.message_id) + 1)
    except:
        pass


@bot.message_handler(commands=['marks'])
def get_marks_criterion(message):
    photo = open('photos/шкала оцінок.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
    photo.close()
    del_mess.thread_sleep(15)
    try:
        bot.delete_message(message.chat.id, int(message.message_id))
        bot.delete_message(message.chat.id, int(message.message_id) + 1)
    except:
        pass


@bot.message_handler(commands=['codes'])
def get_codes(message):
    bot.send_message(message.chat.id, CONSTS.codes, parse_mode='html')
    del_mess.thread_sleep(30)
    try:
        bot.delete_message(message.chat.id, int(message.message_id))
        bot.delete_message(message.chat.id, int(message.message_id) + 1)
    except:
        pass


# @bot.message_handler(regexp='[0-9+]')
# def get_interesting_fact(message):
#     try:
#         answer = requests.get(f'http://numbersapi.com/{message.text}?json')
#         eng_text = json.loads(answer.text)['text']
#         print(eng_text)
#         translator = Translator()
#         ukr_trans = translator.translate(eng_text, dest='uk')
#         print(ukr_trans.text)
#         bot.send_message(message.chat.id, ukr_trans.text)
#     except:
#         pass


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "qq", parse_mode='html')


bot.infinity_polling()
