from aip import AipSpeech


APP_ID = '9957614'
API_KEY = 'mNrTC5wX1WZ1IdgHa01LdiRe'
SECRET_KEY = '6DAr0STmzErbLZHvA1uiIaGzT8ZBFnce'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
a=aipSpeech.asr(get_file_content('abc.wav'), 'wav', 16000, {
    'lan': 'zh',
})
print(a)
# print(a['result'])
# print(a['result'][0])
