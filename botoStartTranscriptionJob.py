from __future__ import print_function
import time
from datetime import datetime
import boto3
import sys

def startTranscriptionJob(job_uri,outputBucketName):
    
    transcribe = boto3.client('transcribe')
    now = datetime.now()

    job_name = now.strftime("%m-%d-%Y_%H.%M.%S")

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

job_uri='s3://its-demo-bucket/transcribe-sample.mp3'
outputBucketName='its-demo-bucket'
startTranscriptionJob(job_uri,outputBucketName)

