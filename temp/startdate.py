from datetime import datetime, timedelta
import random


def random_date_generator(start_year):
    
    start_date = datetime(start_year,1,1).date()
    end_date = datetime.today().date()
    calc_days = (end_date - start_date)
    rand_days = random.randint(0,calc_days.days)
    random_start_date = start_date + timedelta(days=rand_days)
    return random_start_date 

my_start_date = random_date_generator(2024)
rand_end_days = random.randint(0,5)
my_end_date = my_start_date + timedelta(days=rand_end_days)

print(my_start_date,rand_end_days)