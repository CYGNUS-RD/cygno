#!/bin/python3
import boto3
from boto3sts import credentials as creds
import pandas as pd
import os
from boto3.s3.transfer import TransferConfig
ba = False
from optparse import OptionParser
urls = ["https://swift.recas.ba.infn.it/", "https://minio.cloud.infn.it/", "https://s3.cr.cnaf.infn.it:7480/" ]
parser = OptionParser(usage='usage: %prog\t [-ubsv] get/put Key')
parser.add_option('-u','--url', dest='url', type='string', default=urls[2], 
                      help='url ['+urls[2]+'];');
parser.add_option('-b','--storage', dest='storage', action='store_true', default=False, help='BA storage;');
parser.add_option('-v','--verbose', dest='verbose', action="store_true", default=False, help='verbose output;');
(options, args) = parser.parse_args()
verbose = options.verbose
ba = options.storage
url = options.url
print(url)

if ba:
    aws_session = boto3.session.Session(
        aws_access_key_id=os.environ.get('BA_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('BA_SECRET_ACCESS_KEY')
    )

    s3r = aws_session.resource('s3', endpoint_url=urls[0],
                              config=boto3.session.Config(signature_version='s3v4'),verify=True)
    
    s3 = aws_session.client('s3', endpoint_url=urls[0],
                            config=boto3.session.Config(signature_version='s3v4'),verify=True)
else:
    aws_session = creds.assumed_session("dodas")
    s3r = aws_session.resource('s3', endpoint_url=url,
                              config=boto3.session.Config(signature_version='s3v4'),verify=True)
    s3 = aws_session.client('s3', endpoint_url=url,
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
GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)
s3.upload_file('./s3_list.py', Bucket="cygno-data", Key='s3_list.py', Config=config)
# s3.upload_file('./s3_list.py', Bucket='cygno-analysis', Key='test/s3_list.py')
    

#file_db = pd.read_json(file_list)
#print (file_db)
