
import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        output=True,
        rate=wf.getframerate(),
        channels=wf.getnchannels(),
        format=pa.get_format_from_width(wf.getsampwidth())
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

r = sr.Recognizer()

def init_speech():
    print('Listening...')
    play_audio('./audios/wet.wav')

    with sr.Microphone() as source:
        print('Say something')
        audio = r.listen(source)

    play_audio('./audios/suppressed.wav')

    command = ''

    try:
        command = r.recognize_google(audio)
    except:
        print('Could\'nt understand you, bro.')

    print("Your command:")
    print(command)

init_speech()