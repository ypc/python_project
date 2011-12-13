#coding=utf8
#把一堆单词数据放在字典里，返回值是元组
dict_word = {'north': ('direction','north'),
            'south': ('direction','south'),
            'east': ('direction','east'),
            'go': ('verb','go'),
            'kill': ('verb','kill'),
            'eat': ('verb','eat'),
            'the': ('stop','the'),
            'in': ('stop','in'),
            'of': ('stop','of'),
            'bear': ('noun','bear'),
            'princess': ('noun','princess')}

#测试这个列表项是不是数字
def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(stuff):
    words = stuff.split()
    #返回格式要求是列表，所以定义一个空列表，将需要返回的内容加到里面
    result = []
    for word in words:
        if word in dict_word:
            result.append(dict_word[word])
            #如果是数字，创建一个新元组，添加到列表中
        elif convert_number(word):
            number_add = ('number',int(word))
            result.append(number_add)
        #创建都不匹配的返回信息
        else:
            error_add = ('error',word)
            result.append(error_add)
    return result
