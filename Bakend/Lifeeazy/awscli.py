#
# import boto3
#
# s3 = boto3.client('s3')
# s3.download_file('vfy-transcribe-test-s3', 's3file_txt','Token.PNG')
import os
import boto3
import botocore

files = ['passwd.png']

bucket = 'vfydevexperiments'

s3 = boto3.resource('s3')

for file in files:
    try:
        s3.Bucket(bucket).download_file(file, os.path.basename(file))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

 #aws s3 cp /home/vfy8/#hai_txt s3://vfydevexperiments/#hai_txt