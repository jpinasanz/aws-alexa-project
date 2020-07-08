from botoUploadFile import *
from botoStartTranscriptionJob import *
from JSONtoSRT import *
from subtitles import *
import boto3

def caption(FileName):
    #upload_file(FileName, "itsawstest", "Test")
    print("11111111")
    #startTranscriptionJob("itsawstest", "Test/" + FileName, "itsawstest")
    print("2222222")

    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket='itsawstest')['Contents']
    latest = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]

    print("333333333")
    JSONtoSRT(latest)
    print("4444444")
    makesubtitle("NewSRTFile.srt", FileName)
    print("5555555")

if __name__ == '__main__':
    caption(*sys.argv[1:])