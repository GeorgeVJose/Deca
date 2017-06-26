#!/usr/bin/env python
import houndify
import sys
from config_contents import *
import time
import os


client = houndify.TextHoundClient("test_user")
print "Enter the query : "
query = raw_input()

start = time.time()
response = client.query(query)
stop = time.time()

print "Response : ",response['AllResults'][0]['WrittenResponse']
print "Time : {} \n".format(stop-start)
cmd_line = 'python3 tts.py "{}"'.format(response['AllResults'][0]['SpokenResponseLong'])
print cmd_line

os.system(cmd_line)

  # for key in response.keys():
  #     print key," :  ", response[key]
