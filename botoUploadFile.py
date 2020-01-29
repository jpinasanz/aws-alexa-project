import logging
import boto3
import os
from botocore.exceptions import ClientError
import sys

#This program is designed to take in a local file specified by a directory,
#the name of an AWS S3 bucket that you have access to, and the file location
#within that S3 where you want to place the file.


def upload_file(file_name,bucket,object_name=None):

    if object_name is None:
        tail = os.path.split(file_name)
        object_name = object_name + tail[1]
        print ("file name is: ", object_name)
    else:
        tail = os.path.split(file_name)
        object_name = object_name + '/' + tail[1]
        print("file name is: ", object_name)

    #Calls S3 service, sets it to 's3_client'
    s3_client=boto3.client('s3')

    #The actual function call to 'upload_file'
    try:
       response=s3_client.upload_file(file_name,bucket,object_name)

    except ClientError as e:
        logging.error(e)
        print ('File failed to upload!')
        return False
    print ('File Uploaded Successfully!')
    return True

if __name__ == '__main__':
    upload_file(*sys.argv[1:])
  

