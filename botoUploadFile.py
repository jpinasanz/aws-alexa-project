import logging
import boto3
from botocore.exceptions import ClientError

def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client=boto3.client('s3')
    #s3 = boto3.client('s3')
    try:
       response=s3_client.upload_file(file_name,bucket,object_name)
       #s3.upload_file(file_name,'its-demo-bucket','LectureAudio/'.object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True



bucketName='its-demo-bucket'
objectName='transcriptionFile.mp3'

upload_file('/mnt/c/users/jc/desktop/ITS/AWS/Amazon_Transcribe/transcribe-sample.mp3',bucketName,objectName)
