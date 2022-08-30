import datetime


def add_weekday(weekday: tuple):
    weekday_list = [weekday[0], weekday[1]]
    weekday_list[1] += 1

    if weekday_list[1] == 5:
        weekday_list[1] = 0
        weekday_list[0] += 1

    if weekday_list[0] == 3:
        weekday_list[0] = 1

    return weekday_list[0], weekday_list[1]


def saturday_week_day(saturday: datetime.date):
    first_saturday = datetime.datetime(2022, 8, 27)

    n_saturday = (saturday.timetuple().tm_yday - first_saturday.timetuple().tm_yday) // 7

    first_saturday_value = (2, 3)

    for _ in range(n_saturday):
        first_saturday_value = add_weekday(first_saturday_value)

    return first_saturday_value[0], datetime.date(2022, 8, first_saturday_value[1] + 1).strftime('%A')


today_date = datetime.datetime.today().date()
tomorrow_date = today_date + datetime.timedelta(days=1)
print(saturday_week_day(tomorrow_date))
