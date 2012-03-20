# lifted from http://stackoverflow.com/questions/2046663/record-output-sound-in-python

import pyaudio
import wave

def record(output_filename, record_secs=20, chunk=1024, channels=1, rate=11025):
    p = pyaudio.PyAudio()
    channel_map = (0, 1)
    stream_info = pyaudio.PaMacCoreStreamInfo(
        flags = pyaudio.PaMacCoreStreamInfo.paMacCorePlayNice,
        channel_map = channel_map)

    stream = p.open(format=pyaudio.paInt16,
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
    return p

    # data = ''.join(all_chunks)
    # wf = wave.open(output_filename, 'wb')
    # wf.setnchannels(channels)
    # wf.setsampwidth(p.get_sample_size(format))
    # wf.setframerate(rate)
    # wf.writeframes(data)
    # wf.close()
