# -*- coding: utf-8 -*-
"""
Amazon Lexにアクセスするクラス
"""

from cognito import createSession # CognitoのPoolIdでSessionを取得する
import wave

class LexBot:
    def __init__(self, pool_id, region):
        
        session = createSession(pool_id, region)
        self.__client = session.client('lex-runtime', region_name=region)
        self.__alias = "$LATEST"
        self.__username = "raspi_client"
        self.__bot_name = "OrderFlowers_jaJP"

    def post_content(self, audio_file):
        f = open(audio_file, 'rb')
        response= self.__client.post_content(
                botName = self.__bot_name,
                botAlias = self.__alias,
                userId = self.__username,
                inputStream=f,
                accept='audio/pcm',
                contentType="audio/l16; rate=16000; channels=1")
        print(response)
        audio_stream = response['audioStream'].read()
        response['audioStream'].close()
        f = wave.open(audio_file, 'wb')
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(16000)
        f.setnframes(0)
        f.writeframesraw(audio_stream)
        f.close()
    
    # テキスト使用する場合
    # def post_text(self, text):
    #     response = self.__client.post_text(
    #         botName = self.__bot_name,
    #         botAlias = self.__alias,
    #         userId = self.__username,
    #         inputText=text)
    #     print(response)

