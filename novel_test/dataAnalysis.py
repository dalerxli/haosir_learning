# -*- coding:UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
import gensim
from wordcloud import WordCloud
with open('name.txt','r', encoding='utf-8') as fr:
    names=list(set(words.strip() for words in fr.readlines()))
with open('戮仙.txt', 'r', encoding='utf-8') as f:
    content = list(line.strip() for line in f.readlines())
tags = jieba.analyse.extract_tags(' '.join(content), topK=20, withWeight=True)
def find_pepple_showup_cont(num=10):
    novel = ''.join(content)
    showup_counts = []
    for name in names:
        showup_counts.append([name, novel.count(name)])
    showup_counts.sort(key=lambda v: v[1], reverse=True)
    result= showup_counts[:num]
    show = pd.DataFrame(result, columns=['names', 'counts'])
    return(show)

def makebar(show):
    # 设置中文子字体(特别注意)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 展示的姓名和数据
    data = list(show.counts)
    index = list(show.names)
    # 绘制直方图
    plt.bar(range(len(data)), data, tick_label=index)
    plt.xlabel('出现的人物')
    plt.ylabel('出现的次数')
    plt.title('戮仙人物出现频次图')
    # 利用结巴分词来进行关键词查找
    plt.savefig('test.png')
    plt.show()



def makewordcloud():
    print('关键词:')
    for k, v in tags:
        print('关键词：{}   权重：{:.3f}'.format(k, v))

    # 利用关键词制作图云：
    font = r'C:\Windows\Fonts\simfang.ttf'
    txt = ''.join([v + ',' for v, x in tags])
    wordcloud = WordCloud(background_color='white',font_path=font, max_font_size=40).generate(txt)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    wordcloud.to_file('wordcloud.jpg')
    return tags
def makemodel():
    for tag, x in tags:
        jieba.add_word(tag)

    # 将小说中的姓名加入结巴分词的关键词
    for name in names:
        jieba.add_word(name)

    # 加入中文停用词列表
    with open('stopwords.txt', 'r',encoding='utf-8') as f:
        STOPWORD = [word.strip() for word in f.readlines()]

    # 开始进行分词
    print('开始进行分词。。。。')
    # 我们期待的分词结果是保存着小说每一句话的分词结果
    # 即一个二元数组，这将方便我们一会进行模型的训练
    sentence = []
    for line in content:
        seg_list = list(jieba.cut(line, cut_all=False))
        unique_list = []
        # 开始去除停用词
        for seg in seg_list:
            if seg not in STOPWORD:
                unique_list.append(seg)
        sentence.append(unique_list)
    print('分词完毕')
    # 开始训练模型
    # Gensim中的Word2Vec期望的输入是经过分词的 句子列表。即是一个包含句子分词结果的二维数组
    print('开始训练模型。。。这个时间很长，去喝杯咖啡吧')
    model = gensim.models.Word2Vec(
        sentence, size=100, min_count=4, workers=4)
    print('训练完毕。正在将模型保存到本地')
    model.save('戮仙.model')
    print('Okey ')
if __name__=="__main__":
    shows=find_pepple_showup_cont()
    tags=makewordcloud()
    makemodel()