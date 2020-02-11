import logging
import boto3
import os
from botocore.exceptions import ClientError
import sys

def upload_file(file_name,bucket,object_name=None):
    #This function uploads local files to a specified bucket within
    #AWS S3.
    
    #The section concatenates the file name onto the end of the
    #specified file path in the S3. This is to ensure that your
    #file in the S3 retains its name and all you have to do for
    #the 3rd argument is type in the directory in the S3
    # i.e. ( BucketFolder/InnerFolder/Finalfolder)
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
        #you will get this error if AWS returns an exception
        print ('File failed to upload!')
        return False

    print ('File Uploaded Successfully!')
    return True

if __name__ == '__main__':
    upload_file(*sys.argv[1:])
  

