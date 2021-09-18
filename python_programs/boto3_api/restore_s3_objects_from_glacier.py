from __future__ import print_function
import argparse
import boto3
import botocore
import datetime
from datetime import timedelta
import threading

parser = argparse.ArgumentParser(description='Parse command line options.')
parser.add_argument('-sd', nargs=1, required=True)
parser.add_argument('-ed', nargs=1, required=True)

args = parser.parse_args()

startDate = args.sd[0]
endDate = args.ed[0]
startDateObj = datetime.datetime.strptime(startDate, '%Y-%m-%d')
endDateObj = datetime.datetime.strptime(endDate, '%Y-%m-%d')

def Restore(folder):
    print('Begin : ' + folder)
    session = boto3.session.Session()
    s3 = session.resource('s3', aws_access_key_id='abc',
                        aws_secret_access_key='efg')
    bucket = s3.Bucket('sw-prod-kinesis-events')
    for obj_sum in bucket.objects.filter(Prefix=folder):
        try:
            obj = s3.Object(obj_sum.bucket_name, obj_sum.key)
            if obj.restore == None and obj.storage_class != None:
                print(obj_sum.key)
                resp = bucket.meta.client.restore_object(
                    Bucket=obj_sum.bucket_name,
                    Key=obj_sum.key,
                    RestoreRequest={'Days': 30,'GlacierJobParameters': {'Tier': 'Standard'}}
                )
        except botocore.exceptions.ClientError as e:
            print(obj_sum.key)
            print(e)
    print('Finished : ' + folder)

threads = []
while(startDateObj < endDateObj):
    print(startDateObj.strftime('%Y/%m/%d/'))
    folder = startDateObj.strftime('%Y/%m/%d/')

    t = threading.Thread(target=Restore, args=(folder, ))
    threads.append(t)
    t.start()

    newDateObj = startDateObj + timedelta(days=1)
    startDateObj = newDateObj
    startDate = startDateObj.strftime('%Y-%m-%d')

for index, t in enumerate(threads):
    t.join()
