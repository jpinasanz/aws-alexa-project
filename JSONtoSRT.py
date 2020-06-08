import sys
import os
import json
import datetime
from datetime import datetime, timedelta

def format_result(result):
    td = timedelta(seconds=result)
    timestamp = datetime.min + td
    output = timestamp.strftime('%H:%M:%S,%f')[:-3]
    return output


def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting the script.....".format(filepath))
    count = 0
    sequencenum = 0

    with open(filepath) as f:
        f = open('Test.json')
        data = json.load(f)
        f.close()

        of = open("Output.srt","w+")

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
    main()
