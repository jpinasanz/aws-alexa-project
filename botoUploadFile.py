import logging
import boto3
import sys
import os
from botocore.exceptions import ClientError

def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        tail = os.path.split(file_name)
        object_name = tail[1]
        print ("file name is: ", object_name)

    s3_client=boto3.client('s3')

    try:
       response=s3_client.upload_file(file_name,bucket,object_name)

    except ClientError as e:
        logging.error(e)
        print ('File failed to upload!')
        return False
    print ('File Uploaded Successfully!')
    return True

a1 = input('Input File Location: ')
a2 = input('Input Bucket Name: ')
#a3 = input('Input File Name: ')
a3 = None

upload_file(a1,a2,a3)


#bucketName='its-demo-bucket'
#objectName='transcriptionFile.mp3'

#upload_file(a1,bucketName,a2)
#upload_file('/mnt/c/users/jc/desktop/ITS/AWS/Amazon_Transcribe/transcribe-sample.mp3',bucketName,objectName)
