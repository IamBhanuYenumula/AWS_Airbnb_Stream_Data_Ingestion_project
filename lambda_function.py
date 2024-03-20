import json
import random
import uuid
from datetime import datetime,timedelta


def random_date_generator(start_year):
    
    start_date = datetime(start_year,1,1).date()
    end_date = datetime.today().date()
    calc_days = (end_date - start_date)
    rand_days = random.randint(0,calc_days.days)
    random_start_date = start_date + timedelta(days=rand_days)
    return random_start_date 

def lambda_handler(event, context):

    # Variables assignment
    city_list = ["Hyderabad","Pune","Indore","Banglour","Mumbai"]
    country = "India"
    diff_days = random.randint(0,5)
    booking_id = uuid.uuid4()
    user_id = random.randint(10,100)
    property_id = random.randint(10,100)
    city = random.choice(city_list)
    startdate = random_date_generator(2024)
    enddate = startdate + timedelta(days=diff_days)
    usd = diff_days*60
    amount = "$"+ str(usd)

    i = 0
    while i<10:
        data = {"bookingId": booking_id,
                "userId": user_id,
                "propertyId": property_id,
                "location": city +"'" + country,
                "startDate": startdate,
                "endDate": enddate,
                "price": amount
                }
        print(data)
        i += 1


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


