# coding:utf-8
from wordcloud import WordCloud
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from scipy.misc import imread
import re

def createText():
    record_file = open('./data/refund.txt', 'r', encoding='utf-8')
    ignore_file = open('./data/ignore_word.txt','r', encoding='utf-8')

    # strip()去除字符前面的空格
    line_list = []
    for line in record_file:
        if line.isspace():
            continue
        if re.match(r'(\d{4}-\d{1,2}-\d{1,2})',line[:10]) is not None:
            continue
        line_list.append(line.strip())

    stop_words = set(line.strip() for line in ignore_file)

    word_list = []

    for line in line_list:
        word_map = pseg.cut(line)
        for word, type in word_map:
            if word not in stop_words and (type == 'n' or type == 'v'):
                word_list.append(word)

    ignore_file.close()
    record_file.close()

    return ' '.join(word_list)

def createCloud(text):
    # mask_img = imread('./IMG.JPG')
    wordCloud = WordCloud(font_path='./simhei.ttf', background_color='#fff',width=1600,height=800,max_words=100,scale=2).generate(text)
    plt.imshow(wordCloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    txt = createText()
    createCloud(txt)
