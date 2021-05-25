
import pyaudio
import wave

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

play_audio('./audios/acoustic-Bass-C2.wav')