import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
minute = now.minute
hour = now.hour
seconds = now.second
microsecond = now.microsecond
week_day = now.weekday()     # 0-Monday to 6-Sunday

date_of_birth = dt.datetime(year=2005, month=6, day=4, second=1)
print(date_of_birth)