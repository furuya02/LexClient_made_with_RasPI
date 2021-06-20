
# -*- coding: utf-8 -*-
"""
スイッチを制御するクラス
"""
import RPi.GPIO as GPIO
import time

# スイッチ制御クラス
class Switch:
    def __init__(self, on, off):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(15,GPIO.OUT)
        GPIO.setup(14,GPIO.IN)
        self.__on = on
        self.__off = off
        self.__loop()
    
    def __loop(self):
        status = 'off'
        count = 9999                                                   
        while True:
            if(GPIO.input(14) == GPIO.HIGH):
                # OFF状態をLEDで表示する
                GPIO.output(15,GPIO.LOW)
                if(status == 'on'):
                    status = 'off'
                    count = 0
                else:
                    count += 1
            else:
                # ON状態をLEDで表示する
                GPIO.output(15,GPIO.HIGH)
                if(status == 'off'):
                    status = 'on'
                    count = 0
                else:
                    count += 1
            if(count == 5): # 状態変が0.25sec継続した場合、スイッチ変化のコールバックを起動する
                if(status == 'on'):
                    self.__on()
                else:
                    self.__off()
            time.sleep(0.05)