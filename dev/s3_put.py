#!/bin/python3
import boto3
from boto3sts import credentials as creds
import pandas as pd
import os

ba = True
if ba:
    aws_session = boto3.session.Session(
        aws_access_key_id=os.environ.get('ba_access_key_id'),
        aws_secret_access_key=os.environ.get('ba_secret_access_key')
    )

    s3r = aws_session.resource('s3', endpoint_url="https://swift.recas.ba.infn.it/",
                              config=boto3.session.Config(signature_version='s3v4'),verify=True)
    
    s3 = aws_session.client('s3', endpoint_url="https://swift.recas.ba.infn.it/",
                            config=boto3.session.Config(signature_version='s3v4'),verify=True)
else:
    aws_session = creds.assumed_session("dodas")
    s3r = aws_session.resource('s3', endpoint_url="https://minio.cloud.infn.it/",
                              config=boto3.session.Config(signature_version='s3v4'),verify=True)
    s3 = aws_session.client('s3', endpoint_url="https://minio.cloud.infn.it/",
                            config=boto3.session.Config(signature_version='s3v4'),verify=True)

for bucket in s3r.buckets.all():
    print("-->",bucket.name)

# boto3.set_stream_logger(name='botocore')

# sts_client = boto3.client('sts', endpoint_url="https://rgw.cloud.infn.it:443", region_name='')                                                                                
# print(os.getenv('TOKEN'))


# response = sts_client.assume_role_with_web_identity(
#         RoleArn="arn:aws:iam:::role/IAMaccess",
#         RoleSessionName='Bob',
#         DurationSeconds=3600,
#         WebIdentityToken = os.getenv('TOKEN')
#             )
 
# s3 = boto3.client('s3',
#         aws_access_key_id = response['Credentials']['AccessKeyId'],
#         aws_secret_access_key = response['Credentials']['SecretAccessKey'],
#         aws_session_token = response['Credentials']['SessionToken'],
#         endpoint_url="https://rgw.cloud.infn.it:443")

# response = s3.list_objects(Bucket='cygno-data')['Contents']

s3.upload_file('./s3_list.py', Bucket="cygno-data", Key='s3_list.py')
# s3.upload_file('./s3_list.py', Bucket='cygno-analysis', Key='test/s3_list.py')
    

#file_db = pd.read_json(file_list)
#print (file_db)
