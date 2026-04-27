import requests
import speech_recognition as sr
import pyttsx3
from playsound import playsound 

def text2speech(data):
    try:
        file = 'output.wav'
        assert(type(data)==type('str'))
        engine = pyttsx3.init()
        engine.save_to_file(data, file)
        engine.runAndWait()

    except Exception as e:
        return f'error {str(e)}, 500'
    return file

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

def query(payload):
    response = requests.post("https://api-inference.huggingface.co/models/Qiliang/bart-large-cnn-samsum-ChatGPT_v3", headers={"Authorization": "Bearer {Add your token}"}, json=payload)
    return response.json()

def In2out_text(in_text):
    output = query({
        "inputs": in_text,
    })
    file = text2speech(data=output[0]['generated_text'])
    playsound(file)
    return 0


if __name__ =='__main__':
    text = input("Enter your input: ")
    In2out_text(in_text=text)
