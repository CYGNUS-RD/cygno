#!/bin/python3
from optparse import OptionParser
import requests
import json
parser = OptionParser(usage='usage: <file> <prisigned url file>')
parser.add_option('-v','--verbose', dest='verbose', action="store_true", default=False, help='verbose output;');
(options, args) = parser.parse_args()
verbose = options.verbose

filename_to_upload = args[0]
upload_details_file = args[1]

with open(upload_details_file, "r") as file:
    content = file.read()  # Read the file content
    content = content.replace("'", '"')  # Replace single quotes with double quotes
    upload_details = json.loads(content)  # Parse as JSON
    
with open(filename_to_upload, 'rb') as file_to_upload:
    files = {'file': (filename_to_upload, file_to_upload)}
    upload_response = requests.post(upload_details['url'], data=upload_details['fields'], files=files)

if not (upload_response.status_code == 204):
    print(f"{upload_response.status_code}")