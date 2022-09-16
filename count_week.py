import datetime


def get_num_of_week(date):
    #datetime_september = datetime.datetime(year=2022, month=8, day=22)
    num_of_week_in_year = date.isocalendar().week
    # num_of_week_in_year = datetime.datetime.now().date().isocalendar().week

    week = None
    if num_of_week_in_year % 2 == 0:
        week = "2"
    else:
        week = "1"
    return week



