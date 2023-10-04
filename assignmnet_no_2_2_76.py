'''
Name : Thorat Pranav Padmakar 
Roll No: 76
Assignment No :02
Title: BOW and TF-IDF using Gensim Library
'''

import gensim
from gensim import corpora
from gensim.utils import simple_preprocess


import numpy as np
from gensim import *



text1 = ["""Gensim is a free open-source Python library for representing documents as semantic vectors,
           as efficiently and painlessly as possible. Gensim is designed 
           to process raw, unstructured digital texts using unsupervised machine learning algorithms."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)




text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("\n\nDictionary : \n\n\n")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("\n\nTF-IDF Vector:\n\n\n")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])



from gensim.models.word2vec import Word2Vec
from multiprocessing import cpu_count
import gensim.downloader as api


data=[
    "This is a sentenece",
    "another  example sentence",
    "word embedding are useful",
    "word2vec is apopular model"
]
tok_data=[sentence.split()for sentence in data]

w2v_model = Word2Vec(tok_data, min_count = 0, workers=cpu_count())
sim_word=w2v_model.wv.most_similar('word')
print("\n\n\nWord2Vec : \n\n")
for word,score in sim_word:
    print(f"{word}: {score}")



'''
OUTPUT:


 The dictionary has: 29 tokens

{'Gensim': 0, 'Python': 1, 'a': 2, 'algorithms.': 3, 'and': 4, 'as': 5, 'designed': 6, 'digital': 7, 'documents': 8, 'efficiently': 9, 'for': 10, 'free': 11, 'is': 12, 'learning': 13, 'library': 14, 'machine': 15, 'open-source': 16, 'painlessly': 17, 'possible.': 18, 'process': 19, 'raw,': 20, 'representing': 21, 'semantic': 22, 'texts': 23, 'to': 24, 'unstructured': 25, 'unsupervised': 26, 'using': 27, 'vectors,': 28}


Dictionary : 



[['be', 1], ['better', 1], ['but', 1], ['can', 1], ['excellent', 1], ['food', 1], ['is', 1], ['service', 1], ['the', 2]]
[['food', 1], ['is', 1], ['service', 1], ['the', 2], ['always', 1], ['and', 1], ['delicious', 1], ['loved', 1]]
[['food', 1], ['service', 1], ['the', 2], ['and', 1], ['mediocre', 1], ['terrible', 1], ['was', 2]]


TF-IDF Vector:



[['be', 0.43], ['better', 0.43], ['but', 0.43], ['can', 0.43], ['excellent', 0.43], ['food', 0.09], ['is', 0.21], ['service', 0.09], ['the', 0.18]]
[['food', 0.11], ['is', 0.26], ['service', 0.11], ['the', 0.21], ['always', 0.52], ['and', 0.26], ['delicious', 0.52], ['loved', 0.52]]
[['food', 0.08], ['service', 0.08], ['the', 0.16], ['and', 0.2], ['mediocre', 0.39], ['terrible', 0.39], ['was', 0.78]]   


Word2Vec : 


sentenece: 0.11117951571941376
another: 0.1088901162147522
is: 0.09291724115610123
embedding: 0.00484249135479331
apopular: -0.0027540253940969706
word2vec: -0.013679751195013523
This: -0.02546103298664093
useful: -0.028491031378507614
a: -0.04090546816587448
are: -0.05774581804871559'''