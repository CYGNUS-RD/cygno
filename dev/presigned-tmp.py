#! /usr/bin/env python3

import boto3
import requests
import urllib.parse

def my_creds(url, verbose):

    with open("/tmp/token","r") as f:
        IAM_TOKEN = f.read().strip()
    
    sts_client = boto3.client('sts',
                              endpoint_url=url,
                              region_name='oidc')
    
    response = sts_client.assume_role_with_web_identity(
            RoleArn="arn:aws:iam::cygno:role/IAMaccess",
            RoleSessionName='Bob',
            DurationSeconds=3600,
            WebIdentityToken=IAM_TOKEN)
    

    if verbose: 
        print(f"{response['Credentials']['AccessKeyId']=}\n{response['Credentials']['SecretAccessKey']=}")
    return response

def my_client(credentials, url, verbose):
    client = boto3.client('s3',
                            aws_access_key_id = credentials['Credentials']['AccessKeyId'],
                            aws_secret_access_key = credentials['Credentials']['SecretAccessKey'],
                            aws_session_token = credentials['Credentials']['SessionToken'],
                            endpoint_url=url,
                            region_name='oidc')
    return client

def  main(fun, key, url, bucket, session, verbose):

    credentials = my_creds(url, verbose)
    s3 = my_client(credentials, url, verbose)
    
    if fun == "get":
        url_out = s3.generate_presigned_url('get_object', 
                                        Params={'Bucket': bucket,
                                                'Key': key}, 
                                        ExpiresIn=604800)
    elif fun == "put":
        url_out = s3.generate_presigned_post(bucket, key, ExpiresIn=1036800)
    else:
        url_out = ''
        
    print(url_out)

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser(usage='usage: %prog\t [-ubsv] get/put Key')
    parser.add_option('-u','--url', dest='url', type='string', default='https://minio.cloud.infn.it/', 
                      help='url [https://minio.cloud.infn.it/];');
    parser.add_option('-b','--bucket', dest='bucket', type='string', default='cygno-analysis', 
                      help='bucket [cygno-analysis];');
    parser.add_option('-s','--session', dest='session', type='string', default='dodas', 
                      help='shot name [dodas];');
    parser.add_option('-v','--verbose', dest='verbose', action="store_true", default=False, help='verbose output;');
    (options, args) = parser.parse_args()
    
    if len(args) < 2:
        print(args, len(args))
        parser.error("incorrect number of arguments")

    else:
        main(args[0], args[1], options.url, options.bucket, options.session, options.verbose)
