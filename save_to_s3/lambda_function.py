import json
import boto3
from datetime import datetime
import io
import pandas as pd
import os
import uuid
# from dotenv import load_dotenv

# load_dotenv()

def lambda_handler(event, context):
    
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    today_date = datetime.today().strftime('%Y-%m-%d')
    uniqueID = str(uuid.uuid4())
    print("Event: ", event)
    message = event[0]['message']
    
    if (message == {}):
        return {}
    try:
        obj = s3_client.get_object(Bucket = "airbnb-data-from-lambda", Key = f"date={today_date}/{today_date}_{uniqueID}.csv")
        obj = obj['body'].read()
        obj_str = str(obj, 'utf-8')
        data = io.StringIO(obj_str)
        df = pd.read_csv(data,index_col="bookingId")
        df.loc[message['bookingId']] = [message["userId"],
                                        message["propertyId"],
                                        message["location"],
                                        message["startDate"],
                                        message["endDate"],
                                        message["price"],
                                        message["totalDays"]]
        df.to_csv('/tmp/test.csv', encoding = 'utf-8')
        s3_resource.Bucket("airbnb-data-from-lambda").upload_file('/tmp/test.csv',f"date={today_date}/{today_date}.csv")
        print(df)
    except Exception as e:
        print(str(e))
        df = pd.DataFrame(columns=["bookingId","userId","propertyId","location","startDate","endDate","price","totalDays"])
        df = df.set_index(list(df.columns)[0])
        df.loc[message['bookingId']] = [message["userId"],
                                message["propertyId"],
                                message["location"],
                                message["startDate"],
                                message["endDate"],
                                message["price"],
                                message["totalDays"]]
        df.to_csv('/tmp/test.csv', encoding = 'utf-8')
        s3_resource.Bucket("airbnb-data-from-lambda").upload_file('/tmp/test.csv',f"date={today_date}/{today_date}_{uniqueID}.csv")
        
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'data from sqs is...{event}')
    }

