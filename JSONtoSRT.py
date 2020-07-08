import sys
import os
import json
import datetime
import boto3
from datetime import datetime, timedelta


def format_result(result):
    td = timedelta(seconds=result)
    timestamp = datetime.min + td
    output = timestamp.strftime('%H:%M:%S,%f')[:-3]
    return output


def JSONtoSRT(filename):
    filepath = sys.argv[1]

    # if not os.path.isfile(filepath):
    #     print("File path {} does not exist. Exiting the script.....".format(filepath))
    count = 0
    sequencenum = 0

    #with open(filepath) as f:
        #f = open(filename)
    s3 = boto3.resource('s3')
    f = s3.Object('itsawstest', filename)
    #f = s3.get_object(Bucket="itsawstest", Key= filename)
    #data = json.load(f.get()['Body'])
    file_content = f.get()['Body'].read().decode('utf-8')
    data = json.loads(file_content)
    #data = f["Body"].read().decode()
    print(data)
        #data = json.load(f)
        #f.close()

    of = open("NewSRTFile.srt","w+")

    for (k, v) in data.items():
        # if (k == "jobName"):
        #     print("JobName is: " + str(v))
        #     print('\n')
        # if (k == "accountId"):
        #     print("AccountID is: " + str(v))
        #     print('\n')
        if (k == "results"):
            for item in v['items']:
                sequencenum = sequencenum + 1
                of.write(str(sequencenum) + '\n')
                #Check time litmit for num of captions on one line
                if(type(item.get('start_time')) is not type(None)):
                    of.write(format_result(float(item.get('start_time'))) + " --> " + str(format_result(float(item.get('end_time')))) + '\n')
                    for word in item['alternatives']:
                        if float(word.get('confidence')) > .7 :
                            of.write(str(word.get('content')) + '\n')
                        else:
                            of.write(" 'Unkown Word' " + '\n')
                    of.write('\n')
        # if (k == "status"):
        #     print("Status is: " + str(v))
        #     print('\n')


if __name__ == '__main__':
    JSONtoSRT(*sys.argv[1:])
