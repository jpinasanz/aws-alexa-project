from __future__ import print_function
import time
from datetime import datetime
import boto3
import sys

#This program is designed to page requests to AWS to take a file located in
#an S3 bucket and run a transcription job with the AWS Transcribe service.


def startTranscriptionJob(bucketName,bucketFileDirectory,outputBucketName):
    #creates Transcribe job client
    transcribe = boto3.client('transcribe')
    s3 = boto3.client('s3')
    #creates a dateTime object
    now = datetime.now()
    #returns the filename from the URL input in the argument
    uriFilename = bucketFileDirectory.rsplit('/',1)[1]
    #generates a unique file name for the 
    job_name = uriFilename + '-' + now.strftime("%m-%d-%Y_%H.%M.%S")
    #produce the bucket location for the uri line
    response = s3.get_bucket_location(Bucket=bucketName)
    bucketLocation = response.get('LocationConstraint')
    
    job_uri = "https://"+ bucketName+'.s3-' +bucketLocation +".amazonaws.com/"+ bucketFileDirectory
    print ('\n' +job_uri + '\n')

    transcribe.start_transcription_job(
            TranscriptionJobName= job_name,
            Media={'MediaFileUri': job_uri },
            MediaFormat='mp3',
            LanguageCode='en-US',
            OutputBucketName=outputBucketName
            )

    while True:
        status=transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus']in['COMPLETED', 'FAILED']: break
        print ("Not ready yet...")
        time.sleep(5)
        print(status)

if __name__ == '__main__':
    startTranscriptionJob(*sys.argv[1:])





