### Dates ###

from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()

year = datetime(2023,1,1)

def print_date(date):
    print(now.day)
    print(now.year)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(date.timestamp())

print_date(now)

from datetime import time

