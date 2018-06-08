# #-*-coding:utf-8-*-
#
# #引入库
import pyaudio
import wave
# import sys
#
# # 播放器
# # 定义数据流块
# CHUNK = 1024
#
# # if len(sys.argv) < 2:
# #     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
# #     sys.exit(-1)
#
# # 只读方式打开wav文件
# wf = wave.open(r'D:\Projects\PyProjects\Project1\output.wav', 'rb')#(sys.argv[1], 'rb')
#
# p = pyaudio.PyAudio()
#
# # 打开数据流
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)
#
# # 读取数据
# data = wf.readframes(CHUNK)
#
# # 播放
# while data != '':
#     stream.write(data)
#     data = wf.readframes(CHUNK)
#
# # 停止数据流
# stream.stop_stream()
# stream.close()
#
# # 关闭 PyAudio
# p.terminate()


import time
import pygame
from aip import AipSpeech

APP_ID = '9957614'
API_KEY = 'mNrTC5wX1WZ1IdgHa01LdiRe'
SECRET_KEY = '6DAr0STmzErbLZHvA1uiIaGzT8ZBFnce'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result  = aipSpeech.synthesis('2017年', 'zh', 1, {
    'vol': 5,
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

#pygame经测试支持mp3，不支持wav格式
file=r'auido.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()

#
# CHUNK = 1024
#
# # if len(sys.argv) < 2:
# #     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
# #     sys.exit(-1)
#
# # 只读方式打开wav文件
# wf = wave.open('auido.mp3', 'rb')#(sys.argv[1], 'rb')
#
# p = pyaudio.PyAudio()
#
# # 打开数据流
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)
#
# # 读取数据
# data = wf.readframes(CHUNK)
#
# # 播放
# while data != '':
#     stream.write(data)
#     data = wf.readframes(CHUNK)
#
# # 停止数据流
# stream.stop_stream()
# stream.close()
#
# # 关闭 PyAudio
# p.terminate()