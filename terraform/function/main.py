import json
import boto3


def file_handler(event, context):
    s3 = boto3.resource('s3')
    src_bucket = s3.Bucket("s3-start")

    for obj in src_bucket.objects.filter(Prefix=''):
        copy_source = {'Bucket': "s3-start", 'Key': obj.key}

        dst_file_name = obj.key
        s3.meta.client.copy(copy_source, "s3-finish", dst_file_name)
