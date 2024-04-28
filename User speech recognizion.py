import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = "audio_file.wav"  # Replace with the path to your audio file

# Recognize speech from the audio file
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

    # Perform speech recognition
    try:
        text = recognizer.recognize_google(audio_data)
        print("Recognized speech:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
