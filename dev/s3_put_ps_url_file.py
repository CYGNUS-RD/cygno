#!/bin/python3
import boto3
from boto3sts import credentials as creds
from optparse import OptionParser
import requests
parser = OptionParser(usage='usage: <prisigned url>')
#parser.add_option('-b','--storage', dest='storage', action='store_true', default=False, help='BA storage;');
parser.add_option('-v','--verbose', dest='verbose', action="store_true", default=False, help='verbose output;');
(options, args) = parser.parse_args()
verbose = options.verbose

session = creds.assumed_session("dodas")

s3 = session.client('s3', endpoint_url="https://minio.cloud.infn.it/",
                        config=boto3.session.Config(signature_version='s3v4'),verify=True)

filename_to_upload = 's3_put.py'
bucket_name = 'cygno-analysis'
key_name = 'test.py'

upload_details = s3.generate_presigned_post(bucket_name, key_name)

print(upload_details)

with open(filename_to_upload, 'rb') as file_to_upload:
    files = {'file': (filename_to_upload, file_to_upload)}
    upload_response = requests.post(upload_details['url'], data=upload_details['fields'], files=files)

print(f"Upload response: {upload_response.status_code}")