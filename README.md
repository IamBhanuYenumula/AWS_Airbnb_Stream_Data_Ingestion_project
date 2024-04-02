# AWS_Airbnb_Stream_Data_Ingestion_project
Building a simulated data pipeline for Airbnb booking data that integrates various AWS services, demonstrating real-time data processing, filtering, and storage

![image](https://github.com/IamBhanuYenumula/AWS_Airbnb_Stream_Data_Ingestion_project/assets/107517757/1e1a71bd-5ade-4783-b8b9-ad5d46559baa)

step 1: Create an Amazon SQS Queue with DLQ
● Created an SQS Standard Queue named AirbnbBookingQueue.
● Setup a Dead Letter Queue (DLQ): Created another SQS queue named
AirbnbBookingDLQ. Configured the AirbnbBookingQueue to send
messages to AirbnbBookingDLQ after 3 unsuccessful delivery attempts

step 2: Creating Producer Lambda Function
● Lambda Function - Producer: Created a Lambda function named
ProduceAirbnbBookingData. This function will generate mock Airbnb
booking data and publish it to AirbnbBookingQueue.

procucer logs: ![image](https://github.com/IamBhanuYenumula/AWS_Airbnb_Stream_Data_Ingestion_project/assets/107517757/1e7f1bf5-05de-4501-a7c3-3717a338a6de)

step 3: Setup EventBridge Pipe
● EventBridge Pipe: Created an EventBridge Pipe to consume messages from
AirbnbBookingQueue. Filter messages where the booking duration is more
than 1 day.
Filtering Logic: Use the startDate and endDate to calculate the booking
duration

enrichment logs:
![image](https://github.com/IamBhanuYenumula/AWS_Airbnb_Stream_Data_Ingestion_project/assets/107517757/d5edfac5-59b4-40da-af9a-47d4c8f4c187)

step 4: Created Destination Lambda Function
● Lambda Function - Consumer: Create a Lambda function named
ProcessFilteredBookings. This function will be triggered by the EventBridge
Pipe and will write the filtered records to an S3 bucket

Destination lambda logs:
![image](https://github.com/IamBhanuYenumula/AWS_Airbnb_Stream_Data_Ingestion_project/assets/107517757/666eeab7-8acb-4299-b011-2e8905b56dc3)

S3_transformed_files:
![image](https://github.com/IamBhanuYenumula/AWS_Airbnb_Stream_Data_Ingestion_project/assets/107517757/7aa75ac4-9bda-43ff-86ed-4297ea2b3e83)



