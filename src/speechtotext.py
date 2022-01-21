import speech_recognition as sr
import time
from record_audio import record_voice
from recordaudio import recordvoice
from predict import *
import warnings
warnings.filterwarnings("ignore")


def speech2text():
    audio = recordvoice()
    with open('speech.wav', 'wb') as f:
        f.write(audio.get_wav_data())
    filename = "speech.wav"
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        query = r.recognize_google(audio_data,language='en-in')
        print(query)
    return query


if __name__ == '__main__':
    speech2text()
