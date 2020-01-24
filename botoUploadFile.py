import logging
import boto3
import os
from botocore.exceptions import ClientError
import sys

def upload_file(file_name,bucket,object_name=None):
#
#This pulls the filename from the input file path and concactinates it to the object name.
#Currently, it only does it when the 3rd argument is 'None'.
#Need to change this so you can input the file location in the S3 and the script will place
#the file in the right folder in the S3.
#
    if object_name is None:
        tail = os.path.split(file_name)
        object_name = object_name + tail[1]
        #object_name = "LectureAudio/Spring2020/" + tail[1]
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
    
#directory of the local files ~./c/blah/blahblah/audio.mp3
#a1 = input('Input File Location: ')
#name of the S3 bucket (ie: its-demo-bucket)
#a2 = input('Input Bucket Name: ') 
#this is normally the object name in the bucket, but we found that if you set this to
#a directory name, it creates a directory in the S3. This can be used to place the file
#in a specific location in the S3
#a3 = input('Input Bucket Location: ') 

#upload_file(a1,a2,a3)


#bucketName='its-demo-bucket'
#objectName='transcriptionFile.mp3'

#upload_file(a1,bucketName,a2)
#upload_file('/mnt/c/users/jc/desktop/ITS/AWS/Amazon_Transcribe/transcribe-sample.mp3',bucketName,objectName)
