import pyaudio
import wave
import sys
from aip import AipSpeech
import time
import pygame
import 自动语音识别及语音交互.functions as functions

# 1.记录语音 - recording 通过PyAudio模块实现
# 2.语音转文本 - speechToText 通过百度语音识别实现
# 3.文本解释 - getAnswer 自定义的词汇和功能库
# 4.文本转语音&语音播放 - textToSpeech 百度语音合成+pygame播放器 

# 已知bug：
# 1.如果是打开网页，语音正确识别以后，就去打开网页了，这时候仍会调用语音合成，但是output是none，所以语音自动读上一个语音文件(输出语音文件名是固定的)

#新功能：
# 1.词语切割
# 2.多次交互

#需要优化的点：
# 1.需要先转换为语音文件-文本-转义-文本-语音文件，是否可以避免掉语音文件的生成
# 2.录音收音的间隔是定死了的，不灵活，且如果需要长时间收音的话不支持



#定义百度API
APP_ID = '9957614'
API_KEY = 'mNrTC5wX1WZ1IdgHa01LdiRe'
SECRET_KEY = '6DAr0STmzErbLZHvA1uiIaGzT8ZBFnce'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

class autoSpeech:
    def __init__(self,wavfilepath):
        # wavfilepath 包括文件名，可为相对路径或绝对路径，文件名最好不要用数字开头，否则存在字符转义的问题
        self.wavfilepath=wavfilepath
    def recording(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1  #百度语音要求单声道
        RATE = 11025
        RECORD_SECONDS = 5
        # WAVE_OUTPUT_FILENAME = self.wavfilepath
        # WAVE_OUTPUT_FILENAME = "D:\output.wav" #可以是相对路径或绝对路径

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(self.wavfilepath, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        # wf.writeframes("".join(frames))
        wf.close()

    def getSpeechContent(self):
        # 读取文件
        with open(self.wavfilepath, 'rb') as fp:
            return fp.read()

    def speechToText(self):
        # 识别本地文件
        textFromSpeech=aipSpeech.asr(self.getSpeechContent(), 'wav', 16000, {'lan': 'zh',})
        # 最后一个字符是中文逗号，需要截取
        textString = textFromSpeech['result'][0][:-1]
        return textString

    def getAnswer(self,inputText):
        if (inputText == '北京科技馆'):
            outputText = '北京时间'
        elif (inputText == '湖北武汉'):
            outputText = '中国'
        elif (inputText == '公司'):
            outputText = '武汉票据交易中心'
        elif (inputText == '服务器139'):
            outputText = '服务器监控'
        elif (inputText == '时间'):
            outputText = functions.getCurrentTime()
        elif (inputText == '百度一下'):
            outputText = functions.searchengine('http://www.baidu.com')
        elif (inputText == '退出程序'):
            print('程序结束')
            sys.exit()
        else:
            outputText = '语音未识别，请重新输入'
        print(inputText)
        print(outputText)
        return outputText

    def textToSpeech(self,textNeedTransfer):
        result  = aipSpeech.synthesis(textNeedTransfer, 'zh', 1, {
            'vol': 8,
        })

        # 识别正确返回语音二进制，并生产语音文件
        # 识别错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open('audio.mp3', 'wb') as f:
                f.write(result)

        # 播放语音文件,pygame支持mp3，不支持wav
        file='audio.mp3'
        pygame.mixer.init()
        print("播放音乐1")
        track = pygame.mixer.music.load(file)

        pygame.mixer.music.play()
        time.sleep(5)
        pygame.mixer.music.stop()


# 1.记录语音 - recording
# 2.语音转文本 - speechToText
# 3.文本解释 - getAnswer
# 4.文本转语音&语音播放 - textToSpeech

a=autoSpeech('abc.wav')
a.recording()
# a.speechToText()
# a.getAnswer(a.speechToText())
a.textToSpeech(a.getAnswer(a.speechToText()))