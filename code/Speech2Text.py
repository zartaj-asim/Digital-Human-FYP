import speech_recognition as sr

def speech2text(filename):
    assert('.wav'==filename[-4:])

    with open(filename, 'rb') as audio_file:
        audio_data = audio_file.read()

    recognizer = sr.Recognizer()
    try:
        # Specify the sample_width and frame_rate based on the audio file properties
        audio = sr.AudioData(audio_data, sample_rate=20000, sample_width=2)

        text = recognizer.recognize_google(audio)
        return f'transcription: {text}'
    except sr.UnknownValueError:
        return 'error: Unable to recognize speech'
    except sr.RequestError:
        return 'error: Error in speech recognition service'

if __name__ == '__main__':
    filename = '.\output.wav'
    print(speech2text(filename))