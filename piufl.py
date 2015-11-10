# -*- coding: utf-8 -*-
""" piufl.py

This python example sends file contents to the PI Connector for UFL REST endpoint

The syntax is: python piufl.py REST-URL file

Parameters:
    rest-ufl - The Address specified in the Data Source configuration of the Connector
    file - Data file to be processed by the Connector 
	
Example:
    python piufl.py https://<server>:5460/connectordata/devices devices.csv

	"""
import argparse
import requests
import json
import sys

### Process arguments

parser = argparse.ArgumentParser(description='POST file contents to PI Connector for UFL')
parser.add_argument('resturl',
                        help='REST endpoint address')
parser.add_argument('file', 
                   help='Data file to be POST-ed')

args = parser.parse_args()


### Read the file contents

try:
	fh = open(args.file,"r")
	data = fh.read()
	fh.close()
	data = ''.join(data)
except:
	print("Unexpected error: ", sys.exc_info()[1])
	sys.exit(1)

### PUT the file to the REST endpoint

try:
	headers = {'content-type': 'text/html','Accept': 'text/plain'}
	request = requests.put(args.resturl, data=data, verify=False)
	print(request.text)
	print(request.status_code)
except:
	print("Unexpected error: ", sys.exc_info()[1])
	sys.exit(1)