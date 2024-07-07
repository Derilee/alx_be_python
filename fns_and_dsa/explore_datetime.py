import datetime
def display_current_datetime():
     current_date = datetime.datetime.now()
     print(f"{current_date.year}-{current_date.month:02}-{current_date.day:02} {current_date.hour}:{current_date.minute}:{current_date.second}")

from datetime import date, timedelta
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
     current_date = date.today()
     delta = timedelta(days=number_of_days)
     future_date = current_date + delta
     print(future_date)
