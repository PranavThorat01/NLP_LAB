'''
Assignment no 2:
Name:Thorat Pranav Padmakar
Batch:B4
Roll no: 76
Title: "Assignment on bag of words (BOW) using Gensim library "
'''
from gensim.utils import simple_preprocess
from gensim import corpora

#text2 = open('sample_text.txt', encoding ='utf-8')
text2 = input()

tokens2 =[]
for line in text2.split('.'):  #read().
  tokens2.append(simple_preprocess(line, deacc = True))

g_dict1 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

'''g_dict1.add_documents(tokens2)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)
'''
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens2]
print("Bag of Words : ", g_bow)


'''
OutPut:

Gensim is a free open-source Python library for representing documents as semantic vectors, as efficiently and painlessly as possible. Gensim is designed to process raw, unstructured digital texts using unsupervised machine learning algorithms.
The dictionary has: 29 tokens

{'and': 0, 'as': 1, 'documents': 2, 'efficiently': 3, 'for': 4, 'free': 5, 'gensim': 6, 'is': 7, 'library': 8, 'open': 9, 'painlessly': 10, 'possible': 11, 'python': 12, 'representing': 13, 'semantic': 14, 'source': 15, 'vectors': 16, 'algorithms': 17, 'designed': 18, 'digital': 19, 'learning': 20, 'machine': 21, 'process': 22, 'raw': 23, 'texts': 24, 'to': 25, 'unstructured': 26, 'unsupervised': 27, 'using': 28}
Bag of Words :  [[(0, 1), (1, 3), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1)], [(6, 1), (7, 1), (17, 1), (18, 1), (19, 1), (20, 1), (21, 1), (22, 1), (23, 1), (24, 1), (25, 1), (26, 1), (27, 1), (28, 1)], []]

'''