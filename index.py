# -*- coding: utf-8 -*-

import os
from record import Record
from switch import Switch
from audio import Audio
from lex_bot import LexBot

POOL_ID = "ap-northeast-1:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
REGION = "ap-northeast-1"

lex_bot = LexBot(POOL_ID, REGION)

CHANNELS = 1
SAMPLE_RATE = 44100
DEVICE_INDEX = 0
WAVE_FILE = "./out.wav"

record = Record(DEVICE_INDEX, CHANNELS, SAMPLE_RATE, WAVE_FILE)
audio = Audio()

def on():
    print("start recording.")
    record.start()

def off():
    print("stop recording")
    record.stop()
    lex_bot.post_content(WAVE_FILE)

    audio.play(WAVE_FILE)
    os.system("rm {}".format(WAVE_FILE))

Switch(on, off)

del record

