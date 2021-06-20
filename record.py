# -*- coding: utf-8 -*-
"""
マイクから録音するクラス
"""

import pyaudio
import wave
import os
import threading
import time

class Record():
    def __init__(self, device_index,channels, sample_rate, outfile):
        self.__CHANNELS = channels
        self.__SAMPLE_RATE = sample_rate # サンプルレート
        self.__CHUNK = int(self.__SAMPLE_RATE/4) # 0.25秒ごとに取得する
        self.__FORMAT = pyaudio.paInt16
        self.__DEVICE_INDEX = device_index
        self.__OUTFILE = outfile
        self.__p = pyaudio.PyAudio()
    
    def start(self):
        self.__frames = []
        self.__stream = self.__p.open(format = self.__FORMAT,
            channels = self.__CHANNELS,
            rate = self.__SAMPLE_RATE,
            input =  True,
            input_device_index = self.__DEVICE_INDEX,
            frames_per_buffer = self.__CHUNK)
        
        self.__recording = True
        self.__thread = threading.Thread(target=self.__loop)
        self.__thread.start()

    def __loop(self):
        while(self.__recording == True):
            data = self.__stream.read(self.__CHUNK)
            self.__frames.append(data)
            print ("data size:{}".format(len(data)))

    def stop(self):
        self.__recording = False
        data = b''.join(self.__frames)
        time.sleep(0.1)

        self.__thread.join()
        self.__stream.stop_stream()
        self.__stream.close()

        # save
        tmp_file = "./tmp.wav"
        wf = wave.open(tmp_file, 'wb')
        wf.setnchannels(self.__CHANNELS)
        wf.setsampwidth(self.__p.get_sample_size(self.__FORMAT))
        wf.setframerate(self.__SAMPLE_RATE)
        wf.writeframes(data)
        wf.close()
        # 44.1KHz -> 16KHzへの変換
        os.system("ffmpeg -i ./tmp.wav -ar 16000 {}".format(self.__OUTFILE))
        os.system("rm {}".format(tmp_file))
    
    def __del__(self):
        self.__p.terminate()
