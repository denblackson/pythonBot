import datetime

datetime.datetime.today()

# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.today().weekday())
d1 = datetime.datetime.today()
print(f"today is {d1}")
d2 = d1 + datetime.timedelta(days=1)
print(f"tomorrow is {d2}")

print(d2 -d1)

print(d1.strftime('%A %d'))
#((Datetime.Now-Datetime(1 сентря)).Days/7)%2

print('<------------------------------------------>')
#region
datetime_now = datetime.datetime.now()
datetime_september = datetime.datetime(year=2022, month=9, day=1)
result = datetime_now - datetime_september
count_number_of_week= (result.days / 7) % 2
print(f"count_week {count_number_of_week}")
if count_number_of_week == 0:
    print("1 неділя")
else:
    print('2 неділя')

#endregion
print('<------------------------------------------>\n\n')

#region
#photo = open("photos/Розклад/2 тиждень/П'ятниця.jpg", 'rb')

 # 2 неділя
photo = open(f"photos/Розклад/{int(count_number_of_week)+1} тиждень/П'ятниця.jpg", 'rb')
print(photo)
#endregion