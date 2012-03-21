# lifted from http://stackoverflow.com/questions/2046663/record-output-sound-in-python

import pyaudio
import wave
import subprocess
import struct

def record(output_filename, record_secs=20, chunk=1024, channels=1, rate=44100):
    p = pyaudio.PyAudio()
    channel_map = (0, 1)
    stream_info = pyaudio.PaMacCoreStreamInfo(
        flags = pyaudio.PaMacCoreStreamInfo.paMacCorePlayNice,
        channel_map = channel_map)
    format = pyaudio.paInt16

    stream = p.open(format=format,
                    rate=rate,
                    input=True,
                    input_host_api_specific_stream_info=stream_info,
                    channels=channels)

    all_chunks = []
    for i in range(0, rate / chunk * record_secs):
            data = stream.read(chunk)
            all_chunks.append(data)
    stream.close()
    p.terminate()

    data = ''.join(all_chunks)
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(data)
    wf.close()

def get_samples_from_file(filename):
    p = subprocess.Popen([
        'ffmpeg',
        '-i', filename,
        '-ac', '1',
        '-ar', '11025',
        '-f', 's16le',
        '-t', '30',
        '-ss', '0',
        '-',
    ], stdout=subprocess.PIPE, stderr=None)

    samples = []

    while True:
        sample = p.stdout.read(2)
        if sample == '':
            break
        samples.append(struct.unpack('h', sample)[0] / 32768.0)

    return samples
