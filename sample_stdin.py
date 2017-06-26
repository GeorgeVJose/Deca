#!/usr/bin/env python

import houndify
import sys

if __name__ == '__main__':
  class MyListener(houndify.HoundListener):
    def onPartialTranscript(self, transcript):
      print "Partial transcript: " + transcript
    def onFinalResponse(self, response):
      print "Final response: " + str(response)
    def onError(self, err):
      print "Error: " + str(err)

  client = houndify.StreamingHoundClient("test_user")

  BUFFER_SIZE = 512
  samples = sys.stdin.read(BUFFER_SIZE)
  finished = False
  client.start(MyListener())
  while not finished:
    finished = client.fill(samples)
    samples = sys.stdin.read(BUFFER_SIZE)
    if len(samples) == 0:
      break
  client.finish()
