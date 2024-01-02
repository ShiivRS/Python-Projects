import speech_recognition as sr


AUDIO_FILE=("harvard.wav")

r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)

try:
    print("Audio file contains:")
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("google speech recognition didnt understand audio")

except sr.RequestError:
    print("Couldnt get results from speech recognition")
