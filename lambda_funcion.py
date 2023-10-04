import json
import boto3
import time
import csv
import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    
    bucket_name = 'bucket-prueba-udla'
    file_name = 'bank.csv'
    dir_file = '/tmp/' + file_name
    s3 = boto3.resource('s3')
    s3.meta.client.download_file(bucket_name, file_name, dir_file)

    # Transform Data      
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S" )

    line_count = 0
    
    with open(dir_file, mode='r') as csv_file:
        data_csv = csv.reader(csv_file,delimiter=';')

        # Transform
        for row in data_csv:
            line_count += 1
            if line_count == 1:
                pass
            else:      
                #print(row)
                print(row[0],row[1],row[5],timestamp)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
