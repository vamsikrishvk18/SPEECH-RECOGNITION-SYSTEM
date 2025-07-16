import speech_recognition as sr

recognizer = sr.Recognizer()

# Use the uploaded filename
filename = list(uploaded.keys())[0]

with sr.AudioFile(filename) as source:
    audio = recognizer.record(source)

try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print("API error:", e)
