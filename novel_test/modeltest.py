import gensim

# 读入训练好的模型
model = gensim.models.Word2Vec.load('戮仙.model')

# 我们来找找和范闲类似的人物
print('===============和杜铁剑类似的人物=================')
for s in model.most_similar(positive=['杜铁剑'])[:5]:
    print(s)
print('\n\n')
print('===============和黄明类似的人物=================')
for s in model.most_similar(positive=['黄明'])[:5]:
    print(s)
print('\n\n')
print('================与沈石相关的人物================')
for s in model.most_similar(positive=['沈石'])[:5]:
    print(s)
print('\n\n')
print('===============云霓徒弟=================')
for s in model.most_similar(positive=['云霓'])[:5]:
    print(s)
print('\n\n')
print('===============和甘泽类似的人物=================')
for s in model.most_similar(positive=['甘泽'])[:5]:
    print(s)
print('\n\n')
