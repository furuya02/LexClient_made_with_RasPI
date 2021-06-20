
# -*- coding: utf-8 -*-
"""
WAVファルを再生するクラス
"""

import simpleaudio as sa

class Audio:
    def play(self, wav_file):
        print("audio start")
        wave_obj = sa.WaveObject.from_wave_file(wav_file)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print("audio finish.")
