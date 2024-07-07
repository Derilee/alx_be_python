import datetime
def display_current_datetime():
     current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     print(current_date)

from datetime import date, timedelta
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
     current_date = date.today()
     delta = timedelta(days=number_of_days)
     future_date = current_date + delta
     print(future_date)
