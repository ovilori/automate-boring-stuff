from datetime import datetime, timedelta
from dateutil.parser import parse
print(datetime.now().replace(microsecond=0))
sorted_date = datetime.now().strftime('%Y_%m_%d_%I_%M_%S_%p')
print(sorted_date)
""" a = '2/28/2021'
day_one = parse(a)
day_one =  day_one.date()
print(type(day_one))
print(day_one)
print(type(day_one))
next_day = timedelta(days=1)
day_two = day_one + next_day
print(day_two)
print(type(day_two))
 """