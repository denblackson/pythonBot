import datetime

today_date = datetime.datetime.today().date()
tomorrow_date = today_date + datetime.timedelta(days=1)


def if_tomorrow_is_saturday():
    photo = None
    if tomorrow_date == datetime.datetime(year=2022, month=8, day=27).date():
        photo = open(f"../photos/Розклад/2 тиждень/Thursday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=9, day=3).date():
        photo = open(f"../photos/Розклад/2 тиждень/Friday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=9, day=10).date():
        photo = open(f"../photos/Розклад/1 тиждень/Monday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=9, day=17).date():
        photo = open(f"../photos/Розклад/1 тиждень/Tuesday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=9, day=24).date():
        photo = open(f"photos/Розклад/1 тиждень/Wednesday.jpg" 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=10, day=1).date():
        photo = open(f"../photos/Розклад/1 тиждень/Thursday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=10, day=8).date():
        photo = open(f"../photos/Розклад/1 тиждень/Friday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=10, day=15).date():
        photo = open(f"../photos/Розклад/2 тиждень/Monday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=10, day=22).date():
        photo = open(f"../photos/Розклад/2 тиждень/Tuesday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=10, day=29).date():
        photo = open(f"../photos/Розклад/2 тиждень/Wednesday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=11, day=5).date():
        photo = open(f"../photos/Розклад/2 тиждень/Thursday.jpg", 'rb')
    elif tomorrow_date == datetime.datetime(year=2022, month=11, day=12).date():
        photo = open(f"../photos/Розклад/2 тиждень/Friday.jpg", 'rb')
    return photo


def if_today_is_saturday():
    photo = None
    if today_date == datetime.datetime(year=2022, month=8, day=27).date():
        photo = open(f"../photos/Розклад/2 тиждень/Thursday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=9, day=3).date():
        photo = open(f"../photos/Розклад/2 тиждень/Friday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=9, day=10).date():
        photo = open(f"../photos/Розклад/1 тиждень/Monday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=9, day=17).date():
        photo = open(f"../photos/Розклад/1 тиждень/Tuesday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=9, day=24).date():
        photo = open(f"photos/Розклад/1 тиждень/Wednesday.jpg" 'rb')
    elif today_date == datetime.datetime(year=2022, month=10, day=1).date():
        photo = open(f"../photos/Розклад/1 тиждень/Thursday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=10, day=8).date():
        photo = open(f"../photos/Розклад/1 тиждень/Friday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=10, day=15).date():
        photo = open(f"../photos/Розклад/2 тиждень/Monday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=10, day=22).date():
        photo = open(f"../photos/Розклад/2 тиждень/Tuesday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=10, day=29).date():
        photo = open(f"../photos/Розклад/2 тиждень/Wednesday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=11, day=5).date():
        photo = open(f"../photos/Розклад/2 тиждень/Thursday.jpg", 'rb')
    elif today_date == datetime.datetime(year=2022, month=11, day=12).date():
        photo = open(f"../photos/Розклад/2 тиждень/Friday.jpg", 'rb')
    return photo
