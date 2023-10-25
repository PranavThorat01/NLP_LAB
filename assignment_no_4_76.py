from nltk.util import ngrams
n=1
sent='i am student of sanjivani college of engineering college'
print("Unigram of single sentence : \n")
unigram=ngrams(sent.split(),n)

for item in unigram:
    print(item)

print("\n\n***********************\n\n")

def generate_grams(s, n) :
    arr = []
    for i in range(0, len(s)-n+1) :
        temp = ""
        for j in range(0,n) :
            temp += s[i+j]
            temp += " "
        arr.append(temp)
    print(arr)
        
sentence = 'One of the tell-tale signs of cheating on your Spanish homework is that grammatically, it’s a mess. Many languages don’t allow for straight translation and have different orders for sentence structure, which translation services used to overlook. But, they’ve come a long way. With NLP, online translators can translate languages more accurately and present grammatically-correct results. This is infinitely helpful when trying to communicate with someone in another language. Not only that, but when translating from another language to your own, tools now recognize the language based on inputted text and translate it.'
print("Bigram of paragraph : \n")
print("Sample Output for n = 2 and given sentence is :")
generate_grams(sentence.split(), 2)

print("\n\n***********************\n\n")



from nltk import ngrams
print("Bigram of txt file : \n")
file = open("/home/exam/Documents/NLP_LAB/sample_text.txt")
for i in file.readlines():
    cumulative = i
    sentences = i.split(".")
    counter = 0
    for sentence in sentences:
        print("For sentence", counter + 1, ", trigrams are: ")
        trigrams = ngrams(sentence.split(" "), 3)
        for grams in trigrams:
            print(grams)
        counter += 1
        print()
     

'''
Output:

Unigram of single sentence : 

('i',)
('am',)
('student',)
('of',)
('sanjivani',)
('college',)
('of',)
('engineering',)
('college',)


***********************


Bigram of paragraph : 

Sample Output for n = 2 and given sentence is :
['One of ', 'of the ', 'the tell-tale ', 'tell-tale signs ', 'signs of ', 'of cheating ', 'cheating on ', 'on your ', 'your Spanish ', 'Spanish homework ', 'homework is ', 'is that ', 'that grammatically, ', 'grammatically, it’s ', 'it’s a ', 'a mess. ', 'mess. Many ', 'Many languages ', 'languages don’t ', 'don’t allow ', 'allow for ', 'for straight ', 'straight translation ', 'translation and ', 'and have ', 'have different ', 'different orders ', 'orders for ', 'for sentence ', 'sentence structure, ', 'structure, which ', 'which translation ', 'translation services ', 'services used ', 'used to ', 'to overlook. ', 'overlook. But, ', 'But, they’ve ', 'they’ve come ', 'come a ', 'a long ', 'long way. ', 'way. With ', 'With NLP, ', 'NLP, online ', 'online translators ', 'translators can ', 'can translate ', 'translate languages ', 'languages more ', 'more accurately ', 'accurately and ', 'and present ', 'present grammatically-correct ', 'grammatically-correct results. ', 'results. This ', 'This is ', 'is infinitely ', 'infinitely helpful ', 'helpful when ', 'when trying ', 'trying to ', 'to communicate ', 'communicate with ', 'with someone ', 'someone in ', 'in another ', 'another language. ', 'language. Not ', 'Not only ', 'only that, ', 'that, but ', 'but when ', 'when translating ', 'translating from ', 'from another ', 'another language ', 'language to ', 'to your ', 'your own, ', 'own, tools ', 'tools now ', 'now recognize ', 'recognize the ', 'the language ', 'language based ', 'based on ', 'on inputted ', 'inputted text ', 'text and ', 'and translate ', 'translate it. ']


***********************


Bigram of txt file : 

For sentence 1 , trigrams are: 
('Gensim', 'is', 'a')
('is', 'a', 'free')
('a', 'free', 'open-source')
('free', 'open-source', 'Python')
('open-source', 'Python', 'library')
('Python', 'library', 'for')
('library', 'for', 'representing')
('for', 'representing', 'documents')
('representing', 'documents', 'as')
('documents', 'as', 'semantic')
('as', 'semantic', 'vectors,')
('semantic', 'vectors,', 'as')
('vectors,', 'as', 'efficiently')
('as', 'efficiently', 'and')
('efficiently', 'and', 'painlessly')
('and', 'painlessly', 'as')
('painlessly', 'as', 'possible')

For sentence 2 , trigrams are: 
('', 'Gensim', 'is')
('Gensim', 'is', 'designed')
('is', 'designed', 'to')
('designed', 'to', 'process')
('to', 'process', 'raw,')
('process', 'raw,', 'unstructured')
('raw,', 'unstructured', 'digital')
('unstructured', 'digital', 'texts')
('digital', 'texts', 'using')
('texts', 'using', 'unsupervised')
('using', 'unsupervised', 'machine')
('unsupervised', 'machine', 'learning')
('machine', 'learning', 'algorithms')

'''     