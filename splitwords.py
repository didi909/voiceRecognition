import pynlpir

# 用于分词并匹配目标词汇，返回true or false
def splitstring(inputstring,targetstring):
    pynlpir.open()
    splitresult=pynlpir.segment(inputstring)

    for x in range(len(splitresult)):
        # 目前采取分词后完全匹配的模式
        if (splitresult[x][0] == targetstring):
            return True
        # print(splitresult[x][0])
    return False

# if (splitstring('武汉票据交易中心','交易中')):
#     print(True)
# else:
#     print(False)
