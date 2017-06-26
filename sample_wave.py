#!/usr/bin/env python
import wave
import houndify
import sys
import time

# The code below will demonstrate how to use streaming audio through Hound
#
if __name__ == '__main__':
  BUFFER_SIZE = 512

  class MyListener(houndify.HoundListener):
    def onPartialTranscript(self, transcript):
      print "Partial transcript: " + transcript
    def onFinalResponse(self, response):
      print "Final response: " + str(response)
    def onError(self, err):
      print "Error: " + str(err)

  client = houndify.StreamingHoundClient("test_user")

  print "Opening audio"
  print sys.argv[1]
  for fname in sys.argv[1:]:
    print "============== %s ===================" % fname
    audio = wave.open(fname)
    if audio.getsampwidth() != 2:
      print "%s: wrong sample width (must be 16-bit)" % fname
      break
    if audio.getframerate() != 8000 and audio.getframerate() != 16000:
      print "%s: unsupported sampling frequency (must be either 8 or 16 khz)" % fname
      break
    if audio.getnchannels() != 1:
      print "%s: must be single channel (mono)" % fname
      break

    client.setSampleRate(audio.getframerate())
    samples = audio.readframes(BUFFER_SIZE)
    finished = False

    client.start(MyListener())
    while not finished:
      finished = client.fill(samples)
      time.sleep(0.032)     ## simulate real-time so we can see the partial transcripts
      samples = audio.readframes(BUFFER_SIZE)
      if len(samples) == 0:
        break
    client.finish()
