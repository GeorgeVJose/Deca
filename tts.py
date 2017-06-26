from gtts import gTTS as tts
#from config_contents import get_tts
import sys
def speak(save=True, file_name='./last_output.wav'):
    text = sys.argv[-1]
    lang = 'en-us'
    speech = tts(text, lang)
    if save:
        speech.save(file_name)
    return speech

if __name__=='__main__':
    speak()
