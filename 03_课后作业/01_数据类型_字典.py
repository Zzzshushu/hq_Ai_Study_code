"""import string

# 输入文本
text = str(input("请输入文本："))

# 1. 转换为小写
text = text.lower()

# 2. 去除标点符号
for char in string.punctuation:
    text = text.replace(char, '')

# 3. 分割成单词列表
words = text.split()

# 4. 统计单词频率
freq_dict = {}
for word in words:
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

# 5. 输出结果
print(freq_dict)"""
from operator import invert

origin_dict={'a':1,'b':2,'c':1,'d':3,'e':2}

inverted_dict={}
for key,value in origin_dict.items():
    if value not in inverted_dict:
        inverted_dict[value] = [key]
    elif value in inverted_dict:
        inverted_dict[value].append(key)
print(inverted_dict)
