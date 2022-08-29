import datetime
def get_num_of_week():
    datetime_september = datetime.datetime(year=2022, month=8, day=22)
    num_of_week_in_year = datetime.datetime(year=2022, month=8, day=29).isocalendar().week
    week = None

    if num_of_week_in_year % 2 ==0:
      week = "2"
    else:
     week = "1"
    return week

print(get_num_of_week())