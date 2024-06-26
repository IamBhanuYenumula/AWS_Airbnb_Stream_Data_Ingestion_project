import json
import random
import uuid
from datetime import datetime,timedelta
import boto3

sqs_client=boto3.client('sqs')
sqs_url="https://sqs.us-east-2.amazonaws.com/381492279969/AirbnbBookingQueue"

def random_data_generator():  
    start_date = datetime(2024,1,1).date()
    end_date = datetime.today().date()
    calc_days = (end_date - start_date)
    rand_days = random.randint(0,calc_days.days)
    random_start_date = start_date + timedelta(days=rand_days)
    city_list = ["Hyderabad","Pune","Indore","Banglour","Mumbai"]
    country = "India"
    diff_days = random.randint(0,5)
    booking_id = uuid.uuid4()
    user_id = random.randint(10,100)
    property_id = random.randint(10,100)
    city = random.choice(city_list)
    startdate = random_start_date
    enddate = startdate + timedelta(days=diff_days)
    usd = diff_days*60
    amount = "$"+ str(usd)
    total_days = enddate - startdate
    total_days = total_days.days

    data = {"bookingId": str(booking_id),
            "userId": user_id,
            "propertyId": property_id,
            "location": city +"'" + country,
            "startDate": startdate.isoformat(),
            "endDate": enddate.isoformat(),
            "price": amount,
            "totalDays":total_days
            }
    return data

def lambda_handler(event, context):

    i = 0
    while i<10:
        data = random_data_generator()
        print(data)
        sqs_client.send_message(QueueUrl=sqs_url,
                                MessageBody=json.dumps(data))
        i += 1

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


