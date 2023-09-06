'''
Assignment no 1:
Name:Thorat Pranav Padmakar
Batch:B4
Roll no: 76
Title: "Text Pre-processing using NLP operations : Perform Sentence detection ,
        Tokenization, Lemmatization , Part of speech tagging"
'''
#import library
import spacy

#load dictionary
nlp = spacy.load("en_core_web_sm")

#sample input
conference_help_text = (
    "Today is Krishna Janmastami"
    " Protector of the universe"
    " One of from Tridev "
    " and am doing fast "
)

#sentence Detection
about_doc = nlp(conference_help_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")


#Tokenization
about_doc = nlp(conference_help_text)

for token in about_doc:
    print (token, token.idx)



#lemmatization
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")




#part of speech tagging
about_doc = nlp(conference_help_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

#output:
'''
------Sentence DEtection------
Today is Krishna Janmastami Protector...

------Tokenization------

Today 0
is 6
Krishna 9
Janmastami 17
Protector 28
of 38
the 41
universe 45
One 54
of 58
from 61
Tridev 66
  73
and 74
am 78
doing 81
fast 87

-----Lemmatization-----

               Today : today
                  is : be
                 One : one
                  am : be
               doing : do

------Part of Speech Tagging-----               
               
TOKEN: Today
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: is
=====
TAG: VBZ        POS: AUX
EXPLANATION: verb, 3rd person singular present

TOKEN: Krishna
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Janmastami
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: Protector
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN: of
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET
EXPLANATION: determiner

TOKEN: universe
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: One
=====
TAG: CD         POS: NUM
EXPLANATION: cardinal number

TOKEN: of
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: from
=====
TAG: IN         POS: ADP
EXPLANATION: conjunction, subordinating or preposition

TOKEN: Tridev
=====
TAG: NNP        POS: PROPN
EXPLANATION: noun, proper singular

TOKEN:  
=====
TAG: _SP        POS: SPACE
EXPLANATION: whitespace

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: conjunction, coordinating

TOKEN: am
=====
TAG: VBP        POS: AUX
EXPLANATION: verb, non-3rd person singular present

TOKEN: doing
=====
TAG: VBG        POS: VERB
EXPLANATION: verb, gerund or present participle

TOKEN: fast
=====
TAG: RB         POS: ADV
EXPLANATION: adverb
'''