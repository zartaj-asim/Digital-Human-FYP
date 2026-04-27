import speech_recognition as sr
import pyttsx3

def text2speech(data):
    try:
        assert(type(data)==type('str'))
        engine = pyttsx3.init()
        engine.save_to_file(data, 'output.wav')
        engine.runAndWait()

    except Exception as e:
        return f'error {str(e)}, 500'
    return 'All done successfully....'

if __name__ == '__main__':
    data = input('Enter a sentence: ')
    print(text2speech(data))