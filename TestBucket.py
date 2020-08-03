import boto3

def test():
    # session = boto3.session.Session()
    # s3 = session.resource('s3')
    # s3_bucket_name = 'itsawstest'
    # objects = s3.Bucket(s3_bucket_name).objects.all()
    # for object in objects:
    #     print(object)

    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket='itsawstest')['Contents']
    latest = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][-1]
    print(latest)


if __name__ == '__main__':
    test()