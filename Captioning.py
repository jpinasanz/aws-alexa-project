from botoUploadFile import *
from botoStartTranscriptionJob import *
from srt import *
import boto3
import os
from PushToMediasite import send
# The filename is the name of the video to caption in mediasite
def caption(FileName):
    path, file = os.path.split(FileName)
    os.chdir(path)
    #Upload the file into Amazon s3 itsawstest bucket
    print("started Captioning job")
    upload_file(file, "itsawstest", "Test")
    f=open("/home/ec2-user/testfolder/creationLog.txt","a")
    f.write("uploaded file")
    # Amazon will transcribe the file located at Test/Filename. Creates JSON File
    startTranscriptionJob("itsawstest", "Test/" + file, "itsawstest")
    print("started transcription job")
    # sorts the s3 bucket by newest uploaded and grabs that JSON File
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket='itsawstest')['Contents']
    latest = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]
    print("transcription job complete")
    #Converts the JSON File to an SRT one
    realname=file[:-3]

    JSONtoSRT(latest,realname)
    print("finished transcription job")
    ogfile=file
    manifestPath=file.replace('.mp4','.manifest')
    srtPath=ogfile.replace('.mp4','.srt')
    send('/home/sftp_user/'+manifestPath,'/home/ec2-user/testfolder/srtOutput/'+srtPath)

    try:
        if os.path.isfile("/home/ec2-user/testfolder/srtOutput/" + srtPath):
            os.unlink("/home/ec2-user/testfolder/srtOutput/" + srtPath)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % ("/home/ec2-user/testfolder/srtOutput/" + srtPath, e))

    try:
        if os.path.isfile('/home/sftp_user/' + manifestPath):
            os.unlink('/home/sftp_user/' + manifestPath)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % ('/home/sftp_user/' + manifestPath, e))

    try:
        if os.path.isfile(FileName):
            os.unlink(FileName)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (FileName, e))
if __name__ == '__main__':
    caption(*sys.argv[1:])
