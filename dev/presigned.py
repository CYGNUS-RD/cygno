#! /usr/bin/env python3

import boto3
import requests
from boto3sts import credentials as creds
import urllib.parse

def  main(fun, key, url, bucket, session, verbose):

    session = creds.assumed_session(session, endpoint=url,verify=True)
    
    s3 = session.client('s3', endpoint_url=url, config=boto3.session.Config(signature_version='s3v4'), verify=True)
    
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
